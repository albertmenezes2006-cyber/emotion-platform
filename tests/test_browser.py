"""
Playwright — Browser real
Roda: python3 tests/test_browser.py
"""
import asyncio, json, os
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

        # Desktop
        ctx = await browser.new_context(viewport={"width": 1280, "height": 720})
        page = await ctx.new_page()

        testes = [
            ("Home",       BASE + "/"),
            ("Avaliacao",  BASE + "/app/avaliacao"),
            ("Chat",       BASE + "/app/chat"),
            ("Diario",     BASE + "/app/diario"),
            ("Dashboard",  BASE + "/app/dashboard"),
            ("Login",      BASE + "/app/login"),
            ("Planos",     BASE + "/app/planos"),
        ]

        for nome, url in testes:
            print(f"\n  [{nome}] {url}")
            try:
                await page.goto(url, wait_until="domcontentloaded", timeout=30000)
                await asyncio.sleep(2)

                titulo = await page.title()
                conteudo = await page.content()
                has_nav = await page.query_selector(".nav-brand") is not None
                has_footer = await page.query_selector(".footer, footer") is not None
                size = len(conteudo)

                shot = f"{SHOTS}/{nome.lower()}.png"
                await page.screenshot(path=shot, full_page=True)

                ok = has_nav and size > 3000
                resultados.append({
                    "nome": nome, "ok": ok,
                    "titulo": titulo, "size": size,
                    "nav": has_nav, "footer": has_footer,
                    "screenshot": shot
                })

                status = "✅" if ok else "❌"
                print(f"    {status} titulo='{titulo[:40]}' nav={has_nav} footer={has_footer} size={size:,}")
                print(f"    📸 {shot}")

            except Exception as e:
                print(f"    ❌ Erro: {str(e)[:60]}")
                resultados.append({"nome": nome, "ok": False, "erro": str(e)[:80]})

        # Teste funcional Chat
        print("\n  [FUNCIONAL] Enviando mensagem no Chat IA...")
        try:
            await page.goto(BASE + "/app/chat", wait_until="domcontentloaded", timeout=30000)
            await asyncio.sleep(2)

            inp = await page.query_selector("#chat-input, .chat-textarea, textarea")
            if inp:
                await inp.fill("Estou ansioso hoje, pode me ajudar?")
                await asyncio.sleep(0.5)
                btn = await page.query_selector("#send-btn, .send-btn")
                if btn:
                    await btn.click()
                    print("    ⏳ Aguardando resposta IA (12s)...")
                    await asyncio.sleep(12)

            msgs = await page.query_selector_all(".msg-bubble, .chat-bubble")
            shot_chat = f"{SHOTS}/chat_resposta.png"
            await page.screenshot(path=shot_chat, full_page=True)
            ok_chat = len(msgs) >= 2
            print(f"    {'✅' if ok_chat else '⚠️'} {len(msgs)} mensagens | 📸 chat_resposta.png")
            resultados.append({"nome": "Chat Funcional", "ok": ok_chat})
        except Exception as e:
            print(f"    ❌ Chat erro: {str(e)[:60]}")

        # Teste funcional PHQ-9
        print("\n  [FUNCIONAL] Clicando opções do PHQ-9...")
        try:
            await page.goto(BASE + "/app/avaliacao", wait_until="domcontentloaded", timeout=30000)
            await asyncio.sleep(2)

            clicks = 0
            for i in range(9):
                opt = await page.query_selector(f"#phq9-o-{i}-1")
                if opt:
                    await opt.click()
                    clicks += 1
                    await asyncio.sleep(0.15)

            shot_phq = f"{SHOTS}/phq9_preenchido.png"
            await page.screenshot(path=shot_phq, full_page=True)
            print(f"    {'✅' if clicks > 0 else '⚠️'} {clicks}/9 opções clicadas | 📸 phq9_preenchido.png")
            resultados.append({"nome": "PHQ-9 Funcional", "ok": clicks > 0})
        except Exception as e:
            print(f"    ❌ PHQ-9 erro: {str(e)[:60]}")

        # Mobile
        print("\n  [MOBILE] Testando em iPhone (375px)...")
        try:
            mob_ctx = await browser.new_context(viewport={"width": 375, "height": 812})
            mob_page = await mob_ctx.new_page()
            await mob_page.goto(BASE + "/", wait_until="domcontentloaded", timeout=30000)
            await asyncio.sleep(2)
            size_mob = len(await mob_page.content())
            shot_mob = f"{SHOTS}/mobile_home.png"
            await mob_page.screenshot(path=shot_mob, full_page=True)
            ok_mob = size_mob > 3000
            print(f"    {'✅' if ok_mob else '❌'} Mobile: {size_mob:,} chars | 📸 mobile_home.png")
            resultados.append({"nome": "Mobile 375px", "ok": ok_mob})
            await mob_ctx.close()
        except Exception as e:
            print(f"    ❌ Mobile: {str(e)[:60]}")

        # Tablet
        print("\n  [TABLET] Testando em iPad (768px)...")
        try:
            tab_ctx = await browser.new_context(viewport={"width": 768, "height": 1024})
            tab_page = await tab_ctx.new_page()
            await tab_page.goto(BASE + "/app/avaliacao", wait_until="domcontentloaded", timeout=30000)
            await asyncio.sleep(2)
            shot_tab = f"{SHOTS}/tablet_avaliacao.png"
            await tab_page.screenshot(path=shot_tab, full_page=True)
            ok_tab = len(await tab_page.content()) > 3000
            print(f"    {'✅' if ok_tab else '❌'} Tablet | 📸 tablet_avaliacao.png")
            resultados.append({"nome": "Tablet 768px", "ok": ok_tab})
            await tab_ctx.close()
        except Exception as e:
            print(f"    ❌ Tablet: {str(e)[:60]}")

        await ctx.close()
        await browser.close()

    # Relatório
    print("\n" + "=" * 55)
    print("RELATÓRIO PLAYWRIGHT")
    print("=" * 55)
    ok_count = sum(1 for r in resultados if r.get("ok"))
    total = len(resultados)
    print(f"Score: {ok_count}/{total}")
    for r in resultados:
        icon = "✅" if r.get("ok") else "❌"
        extra = f"size={r.get('size',0):,}" if r.get("size") else r.get("erro","")
        print(f"  {icon} {r['nome']}: {extra}")

    shots = os.listdir(SHOTS) if os.path.exists(SHOTS) else []
    print(f"\n📸 {len(shots)} screenshots em {SHOTS}/")
    for s in sorted(shots):
        print(f"   • {s}")

    with open("tests/relatorio_playwright.json", "w", encoding="utf-8") as f:
        json.dump({
            "data": str(datetime.now()),
            "score": f"{ok_count}/{total}",
            "resultados": resultados
        }, f, indent=2, ensure_ascii=False)

    print(f"\n📄 Relatório: tests/relatorio_playwright.json")

asyncio.run(main())
