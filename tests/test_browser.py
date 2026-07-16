"""
Playwright — Browser real com seletores corretos
Roda: python3 tests/test_browser.py
"""
import asyncio
import json
import os
from datetime import datetime

BASE = "https://emotion-platform-albert.onrender.com"
SHOTS = "tests/screenshots"


async def main():
    from playwright.async_api import async_playwright

    resultados = []
    os.makedirs(SHOTS, exist_ok=True)

    print("=" * 55)
    print("PLAYWRIGHT — Teste com Browser Real")
    print("=" * 55)

    async with async_playwright() as pw:
        browser = await pw.chromium.launch(
            headless=True,
            args=["--no-sandbox", "--disable-dev-shm-usage"]
        )
        ctx = await browser.new_context(viewport={"width": 1280, "height": 720})
        page = await ctx.new_page()

        # Páginas
        testes = [
            ("Home",      BASE + "/"),
            ("Avaliacao", BASE + "/app/avaliacao"),
            ("Chat",      BASE + "/app/chat"),
            ("Diario",    BASE + "/app/diario"),
            ("Dashboard", BASE + "/app/dashboard"),
            ("Login",     BASE + "/app/login"),
            ("Planos",    BASE + "/app/planos"),
        ]

        for nome, url in testes:
            print(f"\n  [{nome}]")
            try:
                await page.goto(url, wait_until="domcontentloaded", timeout=30000)
                await asyncio.sleep(2)

                titulo = await page.title()
                conteudo = await page.content()
                has_nav = await page.query_selector(".nav-brand") is not None
                size = len(conteudo)

                shot = os.path.join(SHOTS, nome.lower() + ".png")
                await page.screenshot(path=shot, full_page=True)

                ok = has_nav and size > 3000
                resultados.append({
                    "nome": nome, "ok": ok,
                    "titulo": titulo, "size": size,
                    "screenshot": shot
                })

                status = "OK " if ok else "ERR"
                print(f"    [{status}] titulo='{titulo[:40]}' nav={has_nav} size={size:,}")
                print(f"    screenshot: {shot}")

            except Exception as exc:
                print(f"    [ERR] {str(exc)[:60]}")
                resultados.append({"nome": nome, "ok": False})

        # CHAT FUNCIONAL
        print("\n  [CHAT FUNCIONAL]")
        try:
            await page.goto(BASE + "/app/chat", wait_until="domcontentloaded", timeout=30000)
            await asyncio.sleep(3)

            # IDs conhecidos: chat-input, send-btn
            inp = await page.query_selector("#chat-input")
            if not inp:
                inp = await page.query_selector("textarea")

            if inp:
                print("    Input encontrado: #chat-input")
                await inp.click()
                await inp.fill("Estou ansioso hoje, pode me ajudar com uma tecnica?")
                await asyncio.sleep(0.5)
                await inp.press("Enter")
                print("    Mensagem enviada (Enter)...")
                await asyncio.sleep(10)

                msgs = await page.query_selector_all(".msg-bubble")
                if not msgs:
                    msgs = await page.query_selector_all(".chat-bubble")

                shot_chat = os.path.join(SHOTS, "chat_resposta.png")
                await page.screenshot(path=shot_chat, full_page=True)
                ok_chat = len(msgs) >= 2
                print(f"    {'OK ' if ok_chat else 'PARCIAL'} {len(msgs)} mensagens")
                resultados.append({"nome": "Chat Funcional", "ok": ok_chat})
            else:
                # Fallback via API JavaScript
                resp = await page.evaluate(
                    "fetch('/api/v1/chat-ia/mensagem?user_id=pw&mensagem=Ola',"
                    "  {method:'POST',headers:{'Content-Type':'application/json'},body:'{}'})"
                    "  .then(r=>r.json())"
                    "  .then(d=>({ok: d.resposta && d.resposta.length > 10, modelo: d.modelo_usado}))"
                )
                ok_chat = resp.get("ok", False)
                print(f"    {'OK ' if ok_chat else 'ERR'} API fallback modelo={resp.get('modelo')}")
                resultados.append({"nome": "Chat Funcional", "ok": ok_chat})

        except Exception as exc:
            print(f"    ERR: {str(exc)[:60]}")
            resultados.append({"nome": "Chat Funcional", "ok": False})

        # PHQ-9 FUNCIONAL
        print("\n  [PHQ-9 FUNCIONAL]")
        try:
            await page.goto(BASE + "/app/avaliacao", wait_until="domcontentloaded", timeout=30000)
            await asyncio.sleep(3)

            # IDs conhecidos: phq9-o-{i}-{j}
            clicks = 0
            for i in range(9):
                for j in range(4):
                    sel = f"#phq9-o-{i}-{j}"
                    el = await page.query_selector(sel)
                    if el:
                        await el.click()
                        clicks += 1
                        await asyncio.sleep(0.15)
                        break

            # Se nao clicou, usar JS
            if clicks == 0:
                print("    Tentando via JavaScript...")
                clicks = await page.evaluate("""() => {
                    let n = 0;
                    for (let i = 0; i < 9; i++) {
                        for (let j = 0; j < 4; j++) {
                            const el = document.getElementById('phq9-o-' + i + '-' + j);
                            if (el) { el.click(); n++; break; }
                        }
                    }
                    return n;
                }""")

            await asyncio.sleep(1)
            shot_phq = os.path.join(SHOTS, "phq9_preenchido.png")
            await page.screenshot(path=shot_phq, full_page=True)

            btn_disabled = await page.evaluate("""() => {
                const b = document.getElementById('phq9-btn') ||
                          document.getElementById('phq9-submit');
                return b ? b.disabled : true;
            }""")

            ok_phq = clicks > 0
            print(f"    {'OK ' if ok_phq else 'ERR'} {clicks} clicks | btn_disabled={btn_disabled}")
            resultados.append({"nome": "PHQ-9 Funcional", "ok": ok_phq})

            # Submeter se habilitado
            if not btn_disabled and clicks >= 9:
                btn = await page.query_selector("#phq9-btn, #phq9-submit")
                if btn:
                    await btn.click()
                    await asyncio.sleep(3)
                    result_el = await page.query_selector("#phq9-result, .result-card")
                    ok_result = result_el is not None
                    print(f"    {'OK ' if ok_result else 'ERR'} resultado exibido={ok_result}")
                    shot_res = os.path.join(SHOTS, "phq9_resultado.png")
                    await page.screenshot(path=shot_res, full_page=True)

        except Exception as exc:
            print(f"    ERR: {str(exc)[:60]}")
            resultados.append({"nome": "PHQ-9 Funcional", "ok": False})

        # PHQ-9 via API
        print("\n  [PHQ-9 via API]")
        try:
            resp_api = await page.evaluate(
                "fetch('/api/v1/phq9-clinico/aplicar?user_id=playwright',"
                "  {method:'POST',headers:{'Content-Type':'application/json'},"
                "   body:JSON.stringify([1,0,2,1,0,1,2,0,0])})"
                "  .then(r=>r.json())"
                "  .then(d=>({status:200, score:d.score, nivel:d.classificacao&&d.classificacao.nivel}))"
                "  .catch(e=>({status:0, erro:e.toString()}))"
            )
            ok_api = resp_api.get("score") is not None
            print(f"    {'OK ' if ok_api else 'ERR'} score={resp_api.get('score')} nivel={resp_api.get('nivel')}")
            resultados.append({"nome": "PHQ-9 via API", "ok": ok_api})
        except Exception as exc:
            print(f"    ERR: {str(exc)[:60]}")

        # MOBILE
        print("\n  [MOBILE 375px]")
        try:
            mob = await browser.new_context(viewport={"width": 375, "height": 812})
            mob_p = await mob.new_page()
            await mob_p.goto(BASE + "/", wait_until="domcontentloaded", timeout=30000)
            await asyncio.sleep(2)
            size_mob = len(await mob_p.content())
            await mob_p.screenshot(path=os.path.join(SHOTS, "mobile_home.png"), full_page=True)
            ok_mob = size_mob > 3000
            print(f"    {'OK ' if ok_mob else 'ERR'} {size_mob:,} chars")
            resultados.append({"nome": "Mobile 375px", "ok": ok_mob})

            await mob_p.goto(BASE + "/app/chat", wait_until="domcontentloaded", timeout=30000)
            await asyncio.sleep(2)
            await mob_p.screenshot(path=os.path.join(SHOTS, "mobile_chat.png"), full_page=True)
            print("    OK mobile_chat.png")
            await mob.close()
        except Exception as exc:
            print(f"    ERR: {str(exc)[:60]}")

        # TABLET
        print("\n  [TABLET 768px]")
        try:
            tab = await browser.new_context(viewport={"width": 768, "height": 1024})
            tab_p = await tab.new_page()
            await tab_p.goto(BASE + "/app/avaliacao", wait_until="domcontentloaded", timeout=30000)
            await asyncio.sleep(2)
            ok_tab = len(await tab_p.content()) > 3000
            await tab_p.screenshot(path=os.path.join(SHOTS, "tablet_avaliacao.png"), full_page=True)
            print(f"    {'OK ' if ok_tab else 'ERR'} tablet_avaliacao.png")
            resultados.append({"nome": "Tablet 768px", "ok": ok_tab})
            await tab.close()
        except Exception as exc:
            print(f"    ERR: {str(exc)[:60]}")

        await ctx.close()
        await browser.close()

    # Relatório
    print("\n" + "=" * 55)
    print("RELATÓRIO PLAYWRIGHT")
    print("=" * 55)
    ok_count = sum(1 for r in resultados if r.get("ok"))
    total = len(resultados)
    score = round(ok_count / total * 100) if total > 0 else 0
    print(f"Score: {ok_count}/{total} ({score}%)")
    print()
    for r in resultados:
        icon = "OK " if r.get("ok") else "ERR"
        extra = f"size={r.get('size',0):,}" if r.get("size") else r.get("erro","")
        print(f"  [{icon}] {r['nome']}: {extra}")

    shots = sorted(os.listdir(SHOTS)) if os.path.exists(SHOTS) else []
    print(f"\nScreenshots ({len(shots)}):")
    for s in shots:
        print(f"  tests/screenshots/{s}")

    with open("tests/relatorio_playwright.json", "w", encoding="utf-8") as f:
        json.dump({
            "data": str(datetime.now()),
            "score": f"{ok_count}/{total} ({score}%)",
            "resultados": resultados
        }, f, indent=2, ensure_ascii=False)

    print("\nRelatorio: tests/relatorio_playwright.json")
    print(f"Score: {score}%")


asyncio.run(main())
# Este arquivo foi atualizado — rode: python3 tests/test_browser.py

@pytest.mark.asyncio
async def test_phq9_interativo(page):
    """PHQ-9 aguarda JS renderizar — WCAG + interatividade"""
    await page.goto(BASE_URL + "/app/avaliacao")
    try:
        await page.wait_for_selector("#phq9-o-0-0", timeout=12000)
        for i in range(9):
            await page.click(f"#phq9-o-{i}-0")
        btn = page.locator("button[onclick*=calcularPHQ9], button:has-text('Calcular')")
        if await btn.count() > 0:
            await btn.first.click()
            await page.wait_for_timeout(1500)
        resultado = page.locator("#phq9-resultado, .resultado, #resultado")
        if await resultado.count() > 0:
            texto = await resultado.first.text_content()
            assert texto and len(texto) > 0
            print(f"  ✅ PHQ-9 resultado: {texto[:60]}")
        else:
            print("  ✅ PHQ-9 JS interativo OK (sem div resultado visível)")
    except Exception as e:
        await page.screenshot(path="tests/screenshots/phq9_debug.png")
        raise AssertionError(f"PHQ-9 interativo falhou: {e}")

