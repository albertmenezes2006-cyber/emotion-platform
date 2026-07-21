#!/usr/bin/env python3
"""
Teste Visual Completo com Playwright
Testa design, UX, mobile, cliques, formulários
TUDO pelo terminal
"""
import asyncio
import os
from pathlib import Path

VERDE   = "\033[92m"
AMARELO = "\033[93m"
VERMELHO= "\033[91m"
AZUL    = "\033[94m"
RESET   = "\033[0m"
NEGRITO = "\033[1m"

BASE = "https://emotion-platform-albert.onrender.com"
ok = 0; warn = 0; erro = 0
resultados = []

def log_ok(msg):
    global ok; ok += 1
    print(f"  {VERDE}✅ {msg}{RESET}")
    resultados.append(f"OK: {msg}")

def log_warn(msg):
    global warn; warn += 1
    print(f"  {AMARELO}⚠️  {msg}{RESET}")
    resultados.append(f"WARN: {msg}")

def log_erro(msg):
    global erro; erro += 1
    print(f"  {VERMELHO}❌ {msg}{RESET}")
    resultados.append(f"ERRO: {msg}")

def secao(titulo):
    print(f"\n{NEGRITO}{AZUL}{'='*55}{RESET}")
    print(f"{NEGRITO}{AZUL}  {titulo}{RESET}")
    print(f"{NEGRITO}{AZUL}{'='*55}{RESET}")

# Criar pasta screenshots
Path("screenshots").mkdir(exist_ok=True)

async def testar():
    from playwright.async_api import async_playwright

    async with async_playwright() as p:
        # ══════════════════════════════════════════
        secao("1. DESKTOP — Chrome")
        # ══════════════════════════════════════════
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            viewport={"width": 1280, "height": 720},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/108.0"
        )
        page = await context.new_page()

        # Capturar erros JS
        erros_js = []
        page.on("pageerror", lambda e: erros_js.append(str(e)))
        page.on("console", lambda m: erros_js.append(m.text) if m.type == "error" and "google" not in m.text.lower() else None)

        # Testar páginas principais
        paginas = [
            ("/",             "Landing"),
            ("/app/login",    "Login"),
            ("/app/dashboard","Dashboard"),
            ("/app/chat",     "Chat"),
            ("/app/diario",   "Diario"),
            ("/sobre",        "Sobre"),
            ("/app/planos",   "Planos"),
            ("/faq",          "FAQ"),
        ]

        for rota, nome in paginas:
            try:
                erros_js.clear()
                resp = await page.goto(BASE + rota, wait_until="networkidle", timeout=30000)

                # Screenshot
                await page.screenshot(
                    path=f"screenshots/desktop_{nome.lower()}.png",
                    full_page=True
                )

                # Verificar
                status = resp.status if resp else 0
                titulo = await page.title()
                altura = await page.evaluate("document.body.scrollHeight")
                largura = await page.evaluate("document.body.scrollWidth")
                tem_conteudo = altura > 200

                if status == 200 and tem_conteudo and not erros_js:
                    log_ok(f"Desktop {nome}: {status} | {largura}x{altura}px | '{titulo[:30]}'")
                elif status == 200 and erros_js:
                    log_warn(f"Desktop {nome}: OK mas com erros JS: {erros_js[0][:50]}")
                else:
                    log_erro(f"Desktop {nome}: status={status} altura={altura}")

            except Exception as e:
                log_erro(f"Desktop {nome}: {str(e)[:60]}")

        await context.close()

        # ══════════════════════════════════════════
        secao("2. MOBILE — iPhone 12")
        # ══════════════════════════════════════════
        iphone = p.devices["iPhone 12"]
        context_mobile = await browser.new_context(**iphone)
        page_mobile = await context_mobile.new_page()

        paginas_mobile = [
            ("/",          "Landing"),
            ("/app/login", "Login"),
            ("/app/chat",  "Chat"),
        ]

        for rota, nome in paginas_mobile:
            try:
                resp = await page_mobile.goto(BASE + rota, wait_until="networkidle", timeout=30000)
                await page_mobile.screenshot(
                    path=f"screenshots/mobile_{nome.lower()}.png"
                )
                altura = await page_mobile.evaluate("document.body.scrollHeight")
                log_ok(f"Mobile iPhone {nome}: {resp.status} | altura={altura}px")
            except Exception as e:
                log_erro(f"Mobile iPhone {nome}: {str(e)[:60]}")

        await context_mobile.close()

        # ══════════════════════════════════════════
        secao("3. MOBILE — Android Samsung")
        # ══════════════════════════════════════════
        android = p.devices["Galaxy S9+"]
        context_android = await browser.new_context(**android)
        page_android = await context_android.new_page()

        try:
            resp = await page_android.goto(BASE + "/", wait_until="networkidle", timeout=30000)
            await page_android.screenshot(path="screenshots/android_home.png")
            log_ok(f"Android Samsung Home: {resp.status}")
        except Exception as e:
            log_erro(f"Android: {str(e)[:60]}")

        await context_android.close()

        # ══════════════════════════════════════════
        secao("4. UX REAL — Login completo")
        # ══════════════════════════════════════════
        context_ux = await browser.new_context(
            viewport={"width": 1280, "height": 720}
        )
        page_ux = await context_ux.new_page()
        erros_login = []
        page_ux.on("pageerror", lambda e: erros_login.append(str(e)))

        try:
            await page_ux.goto(BASE + "/app/login", wait_until="networkidle", timeout=30000)
            await page_ux.screenshot(path="screenshots/ux_login_antes.png")

            # Verificar se campos existem
            email_field = await page_ux.query_selector("#login-email")
            senha_field = await page_ux.query_selector("#login-senha")
            btn_login = await page_ux.query_selector("button[onclick*='fazer_login']")

            if email_field and senha_field:
                log_ok("Campos de login encontrados!")

                # Preencher formulário
                await email_field.fill("albertmenezes2006@gmail.com")
                await senha_field.fill("senha123")
                await page_ux.screenshot(path="screenshots/ux_login_preenchido.png")
                log_ok("Formulário preenchido!")

                # Clicar no botão
                if btn_login:
                    await btn_login.click()
                    await page_ux.wait_for_timeout(3000)
                    await page_ux.screenshot(path="screenshots/ux_login_depois.png")

                    url_atual = page_ux.url
                    if "dashboard" in url_atual:
                        log_ok(f"Login OK! Redirecionou para: {url_atual}")
                    else:
                        log_warn(f"Login: URL atual = {url_atual}")
                else:
                    # Tentar Enter
                    await senha_field.press("Enter")
                    await page_ux.wait_for_timeout(3000)
                    url_atual = page_ux.url
                    if "dashboard" in url_atual:
                        log_ok(f"Login OK via Enter! → {url_atual}")
                    else:
                        log_warn(f"Login via Enter: {url_atual}")
            else:
                log_erro("Campos de login NÃO encontrados!")
                # Ver o HTML da página
                content = await page_ux.content()
                inputs = await page_ux.query_selector_all("input")
                log_warn(f"Inputs encontrados: {len(inputs)}")

            if erros_login:
                log_warn(f"Erros JS no login: {erros_login[0][:80]}")

        except Exception as e:
            log_erro(f"UX Login: {str(e)[:80]}")

        # ══════════════════════════════════════════
        secao("5. UX — Cadastro novo usuário")
        # ══════════════════════════════════════════
        try:
            await page_ux.goto(BASE + "/app/login", wait_until="networkidle", timeout=30000)

            # Clicar na aba Criar conta
            tab_cadastro = await page_ux.query_selector(".tab:nth-child(2), [onclick*='cadastro']")
            if not tab_cadastro:
                tab_cadastro = await page_ux.query_selector("[onclick*='cadastro']")

            if tab_cadastro:
                await tab_cadastro.click()
                await page_ux.wait_for_timeout(1000)
                await page_ux.screenshot(path="screenshots/ux_cadastro.png")
                log_ok("Aba cadastro clicada!")

                # Preencher cadastro
                import random, string
                email_novo = f"teste_{''.join(random.choices(string.ascii_lowercase, k=4))}@teste.com"

                nome_field = await page_ux.query_selector("#cad-nome")
                email_field = await page_ux.query_selector("#cad-email")
                senha_field = await page_ux.query_selector("#cad-senha")

                if nome_field and email_field and senha_field:
                    await nome_field.fill("Teste Playwright")
                    await email_field.fill(email_novo)
                    await senha_field.fill("senha123")
                    await page_ux.screenshot(path="screenshots/ux_cadastro_preenchido.png")
                    log_ok(f"Cadastro preenchido: {email_novo}")

                    btn_cad = await page_ux.query_selector("button[onclick*='fazer_cadastro']")
                    if btn_cad:
                        await btn_cad.click()
                        await page_ux.wait_for_timeout(3000)
                        url_atual = page_ux.url
                        await page_ux.screenshot(path="screenshots/ux_cadastro_depois.png")
                        if "dashboard" in url_atual:
                            log_ok(f"Cadastro OK! → {url_atual}")
                        else:
                            log_warn(f"Cadastro: URL = {url_atual}")
                else:
                    log_warn("Campos de cadastro não encontrados")
            else:
                log_warn("Aba cadastro não encontrada")

        except Exception as e:
            log_erro(f"UX Cadastro: {str(e)[:80]}")

        # ══════════════════════════════════════════
        secao("6. UX — Chat IA real")
        # ══════════════════════════════════════════
        try:
            await page_ux.goto(BASE + "/app/chat", wait_until="networkidle", timeout=30000)
            await page_ux.screenshot(path="screenshots/ux_chat.png")

            # Procurar campo de mensagem
            msg_field = await page_ux.query_selector("#chat-input")
            if msg_field:
                await msg_field.fill("Olá! Estou testando o sistema.")
                await page_ux.screenshot(path="screenshots/ux_chat_digitando.png")
                log_ok("Campo de chat encontrado e preenchido!")

                btn_enviar = await page_ux.query_selector("button[onclick*='enviar'], button[type='submit']")
                if btn_enviar:
                    await btn_enviar.click()
                    await page_ux.wait_for_timeout(5000)
                    await page_ux.screenshot(path="screenshots/ux_chat_resposta.png")
                    log_ok("Mensagem enviada! Screenshot salvo.")
            else:
                log_warn("Campo de chat não encontrado (pode precisar de login)")

        except Exception as e:
            log_warn(f"UX Chat: {str(e)[:60]}")

        # ══════════════════════════════════════════
        secao("7. PERFORMANCE VISUAL — Lighthouse básico")
        # ══════════════════════════════════════════
        context_perf = await browser.new_context(
            viewport={"width": 1280, "height": 720}
        )
        page_perf = await context_perf.new_page()

        paginas_perf = ["/", "/app/login", "/sobre"]
        for rota in paginas_perf:
            try:
                inicio = asyncio.get_event_loop().time()
                resp = await page_perf.goto(BASE + rota, wait_until="load", timeout=30000)
                fim = asyncio.get_event_loop().time()
                tempo = round((fim - inicio) * 1000)

                # Métricas de performance
                metrics = await page_perf.evaluate("""() => {
                    const nav = performance.getEntriesByType('navigation')[0];
                    return {
                        domContentLoaded: Math.round(nav.domContentLoadedEventEnd),
                        loadComplete: Math.round(nav.loadEventEnd),
                        firstPaint: Math.round(performance.getEntriesByName('first-paint')[0]?.startTime || 0)
                    }
                }""")

                dom = metrics.get('domContentLoaded', 0)
                load = metrics.get('loadComplete', 0)
                fp = metrics.get('firstPaint', 0)

                if load < 3000:
                    log_ok(f"Perf {rota}: DOM={dom}ms Load={load}ms FP={fp}ms ✅")
                elif load < 5000:
                    log_warn(f"Perf {rota}: DOM={dom}ms Load={load}ms FP={fp}ms (lento)")
                else:
                    log_erro(f"Perf {rota}: muito lento! Load={load}ms")

            except Exception as e:
                log_warn(f"Perf {rota}: {str(e)[:50]}")

        await context_perf.close()

        # ══════════════════════════════════════════
        secao("8. ACESSIBILIDADE VISUAL REAL")
        # ══════════════════════════════════════════
        context_a11y = await browser.new_context(viewport={"width": 1280, "height": 720})
        page_a11y = await context_a11y.new_page()

        try:
            await page_a11y.goto(BASE + "/", wait_until="networkidle", timeout=30000)

            # Verificar acessibilidade via JavaScript
            a11y = await page_a11y.evaluate("""() => {
                const imgs = document.querySelectorAll('img');
                const btns = document.querySelectorAll('button');
                const links = document.querySelectorAll('a');
                const inputs = document.querySelectorAll('input');
                const headings = document.querySelectorAll('h1,h2,h3');

                return {
                    imgs_total: imgs.length,
                    imgs_sem_alt: [...imgs].filter(i => !i.alt).length,
                    btns_total: btns.length,
                    btns_sem_label: [...btns].filter(b => !b.textContent.trim() && !b.getAttribute('aria-label')).length,
                    links_total: links.length,
                    inputs_total: inputs.length,
                    headings: headings.length,
                    tem_h1: document.querySelector('h1') !== null,
                    lang: document.documentElement.lang,
                    title: document.title
                }
            }""")

            log_ok(f"Imagens: {a11y['imgs_total']} total, {a11y['imgs_sem_alt']} sem alt")
            log_ok(f"Botões: {a11y['btns_total']} total, {a11y['btns_sem_label']} sem label")
            log_ok(f"Links: {a11y['links_total']}")
            log_ok(f"Headings: {a11y['headings']} | H1: {a11y['tem_h1']}")
            log_ok(f"Lang: {a11y['lang']} | Title: {a11y['title'][:40]}")

            if a11y['imgs_sem_alt'] > 0:
                log_warn(f"{a11y['imgs_sem_alt']} imagens sem alt text!")
            if a11y['btns_sem_label'] > 0:
                log_warn(f"{a11y['btns_sem_label']} botões sem label!")

        except Exception as e:
            log_warn(f"A11y: {str(e)[:60]}")

        await context_a11y.close()
        await browser.close()

    # ══════════════════════════════════════════
    secao("9. SCREENSHOTS GERADOS")
    # ══════════════════════════════════════════
    screenshots = list(Path("screenshots").glob("*.png"))
    log_ok(f"{len(screenshots)} screenshots gerados!")
    for ss in sorted(screenshots):
        size = ss.stat().st_size // 1024
        log_ok(f"  → {ss.name} ({size}KB)")

    # ══════════════════════════════════════════
    secao("RESUMO FINAL VISUAL")
    # ══════════════════════════════════════════
    total = ok + warn + erro
    pct_ok   = (ok   / total * 100) if total else 0
    pct_warn = (warn / total * 100) if total else 0
    pct_erro = (erro / total * 100) if total else 0

    print(f"\n  {VERDE}✅ OK:       {ok:3d}  ({pct_ok:.0f}%){RESET}")
    print(f"  {AMARELO}⚠️  Warnings: {warn:3d}  ({pct_warn:.0f}%){RESET}")
    print(f"  {VERMELHO}❌ Erros:    {erro:3d}  ({pct_erro:.0f}%){RESET}")

    score = int(pct_ok)
    print(f"\n  {NEGRITO}📊 SCORE VISUAL FINAL: {score}%{RESET}")

    if score >= 90:
        print(f"  {VERDE}{NEGRITO}🚀 Design e UX excelentes!{RESET}")
    elif score >= 70:
        print(f"  {AMARELO}{NEGRITO}⚡ Bom! Pequenos ajustes visuais.{RESET}")
    else:
        print(f"  {VERMELHO}{NEGRITO}🔧 Design precisa de atenção.{RESET}")

    print(f"\n  📸 Screenshots em: ~/emotion_platform/screenshots/")
    print(f"  {AZUL}{'='*55}{RESET}\n")

asyncio.run(testar())
