"""
Plugin: P1 Together+HuggingFace
Categoria: sistemas
Extraido automaticamente do main.py
"""
VERSAO = "1.0"
NOME = "together_hf"
DESCRICAO = "P1 Together+HuggingFace"
CATEGORIA = "sistemas"

# ═══════════════════════════════════════════════════════════════════════
# SISTEMA P1 — TOGETHER AI + HUGGINGFACE + LANGCHAIN
# ═══════════════════════════════════════════════════════════════════════


# ── P1.1 Together AI — 50+ modelos grátis
TOGETHER_API_KEY = _os_s10.getenv("TOGETHER_API_KEY", "")
TOGETHER_MODELS = {
    "chat":     "meta-llama/Llama-3.3-70B-Instruct-Turbo",
    "code":     "Qwen/Qwen2.5-Coder-32B-Instruct",
    "fast":     "meta-llama/Llama-3.2-3B-Instruct-Turbo",
    "creative": "mistralai/Mixtral-8x7B-Instruct-v0.1",
    "reason":   "deepseek-ai/DeepSeek-R1-Distill-Llama-70B",
}

async def chamar_together_ai(
    mensagem: str,
    modelo: str = "chat",
    max_tokens: int = 1000,
    temperatura: float = 0.7
) -> str:
    if not TOGETHER_API_KEY:
        return ""
    try:
        import httpx
        model_id = TOGETHER_MODELS.get(modelo, TOGETHER_MODELS["chat"])
        async with httpx.AsyncClient(timeout=30) as client:
            r = await client.post(
                "https://api.together.xyz/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {TOGETHER_API_KEY}",
                    "Content-Type": "application/json"
                },
                json={
                    "model": model_id,
                    "messages": [{"role": "user", "content": mensagem}],
                    "max_tokens": max_tokens,
                    "temperature": temperatura,
                }
            )
            data = r.json()
            return data["choices"][0]["message"]["content"]
    except Exception as e:
        print(f"Together AI erro: {e}")
        return ""

async def together_analisar_emocao(texto: str) -> dict:
    prompt = (
        f"Analise a emoção do texto em português. "
        f"Responda APENAS em JSON: "
        f'{{\"emocao\": \"string\", \"intensidade\": 1-5, \"confianca\": 0.0-1.0}}\n'
        f"Texto: {texto[:500]}"
    )
    resultado = await chamar_together_ai(prompt, modelo="fast", max_tokens=100)
    try:
        import json
        return json.loads(resultado)
    except Exception:
        return {"emocao": "neutro", "intensidade": 3, "confianca": 0.5}

# ── P1.2 HuggingFace — modelos especializados em emoção
HUGGINGFACE_API_KEY = _os_s10.getenv("HUGGINGFACE_API_KEY", "")
HF_MODELS = {
    "emotion_en":  "j-hartmann/emotion-english-distilroberta-base",
    "sentiment":   "cardiffnlp/twitter-roberta-base-sentiment-latest",
    "emotion_mul": "joeddav/xlm-roberta-large-xnli",
    "toxicity":    "unitary/toxic-bert",
    "depression":  "raynardj/ckpt-emotion-analysis-distilbert-base-uncased",
}

async def chamar_huggingface(texto: str, modelo: str = "emotion_en") -> dict:
    if not HUGGINGFACE_API_KEY:
        return {}
    try:
        import httpx
        model_id = HF_MODELS.get(modelo, HF_MODELS["emotion_en"])
        async with httpx.AsyncClient(timeout=20) as client:
            r = await client.post(
                f"https://api-inference.huggingface.co/models/{model_id}",
                headers={"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"},
                json={"inputs": texto[:512]}
            )
            return r.json()
    except Exception as e:
        print(f"HuggingFace erro: {e}")
        return {}

async def hf_detectar_emocao(texto: str) -> dict:
    resultado = await chamar_huggingface(texto, "emotion_en")
    try:
        if isinstance(resultado, list) and resultado:
            items = resultado[0] if isinstance(resultado[0], list) else resultado
            melhor = max(items, key=lambda x: x.get("score", 0))
            label_map = {
                "joy": "alegria", "sadness": "tristeza",
                "anger": "raiva", "fear": "medo",
                "surprise": "surpresa", "disgust": "nojo",
                "neutral": "neutro"
            }
            return {
                "emocao": label_map.get(melhor["label"].lower(), melhor["label"]),
                "confianca": round(melhor["score"], 3),
                "fonte": "huggingface"
            }
    except Exception:
        pass
    return {"emocao": "neutro", "confianca": 0.5, "fonte": "huggingface"}

async def hf_detectar_toxicidade(texto: str) -> dict:
    resultado = await chamar_huggingface(texto, "toxicity")
    try:
        if isinstance(resultado, list):
            items = resultado[0] if isinstance(resultado[0], list) else resultado
            toxico = next((i for i in items if i["label"] == "toxic"), None)
            if toxico:
                return {
                    "toxico": toxico["score"] > 0.7,
                    "score": round(toxico["score"], 3),
                    "fonte": "huggingface"
                }
    except Exception:
        pass
    return {"toxico": False, "score": 0.0, "fonte": "huggingface"}

# ── P1.3 LangChain — agentes e pipelines
LANGCHAIN_DISPONIVEL = False
try:
    from langchain_core.prompts import ChatPromptTemplate as _ChatPromptTemplate
    LANGCHAIN_DISPONIVEL = True
except ImportError:
    pass

async def langchain_analisar_emocao(texto: str) -> dict:
    if not LANGCHAIN_DISPONIVEL:
        return await together_analisar_emocao(texto)
    try:
        from langchain_groq import ChatGroq
        import os
        llm = ChatGroq(
            model="llama-3.3-70b-versatile",
            api_key=os.getenv("GROQ_API_KEY", ""),
            temperature=0.3,
            max_tokens=200
        )
        prompt = _ChatPromptTemplate.from_messages([
            ("system", "Voce e um especialista em analise emocional. Responda em JSON."),
            ("human", "Analise: {texto}\nJSON: {\"emocao\": string, \"intensidade\": 1-5}")
        ])
        chain = prompt | llm
        result = await chain.ainvoke({"texto": texto[:500]})
        import json
        import re
        json_match = re.search(r'\{.*\}', result.content, re.DOTALL)
        if json_match:
            return json.loads(json_match.group())
    except Exception as e:
        print(f"LangChain erro: {e}")
    return {"emocao": "neutro", "intensidade": 3}

# ── P1.4 Orquestrador de IA expandido
async def orquestrar_ia_expandido(texto: str, modo: str = "emocao") -> dict:
    resultados = {}
    fontes_disponiveis = []
    if _os_s10.getenv("GROQ_API_KEY"):
        fontes_disponiveis.append("groq")
    if TOGETHER_API_KEY:
        fontes_disponiveis.append("together")
    if HUGGINGFACE_API_KEY:
        fontes_disponiveis.append("huggingface")
    if not fontes_disponiveis:
        return {"emocao": "neutro", "intensidade": 3, "fonte": "local"}
    fonte_principal = fontes_disponiveis[0]
    if fonte_principal == "groq":
        try:
            resultado_groq = detectar_emocao_hibrido(texto, usar_gemini=False)
            resultados["groq"] = resultado_groq
        except Exception:
            pass
    if "huggingface" in fontes_disponiveis and len(texto) > 10:
        try:
            hf_result = await hf_detectar_emocao(texto)
            resultados["huggingface"] = hf_result
        except Exception:
            pass
    if resultados:
        melhor_fonte = list(resultados.keys())[0]
        resultado = resultados[melhor_fonte]
        resultado["fontes_consultadas"] = list(resultados.keys())
        resultado["total_fontes"] = len(resultados)
        return resultado
    return {"emocao": "neutro", "intensidade": 3, "fonte": "fallback"}

# ── P1.5 Endpoints
@app.post("/api/ia/together")
async def api_together(request: Request):
    try:
        body = await request.json()
        mensagem = body.get("mensagem", "")
        modelo = body.get("modelo", "chat")
        if not mensagem:
            return JSONResponse({"erro": "mensagem obrigatoria"}, status_code=400)
        resultado = await chamar_together_ai(mensagem, modelo)
        return JSONResponse({"ok": True, "resposta": resultado, "modelo": modelo})
    except Exception as e:
        return JSONResponse({"erro": str(e)}, status_code=500)

@app.post("/api/ia/huggingface")
async def api_huggingface(request: Request):
    try:
        body = await request.json()
        texto = body.get("texto", "")
        if not texto:
            return JSONResponse({"erro": "texto obrigatorio"}, status_code=400)
        emocao = await hf_detectar_emocao(texto)
        toxicidade = await hf_detectar_toxicidade(texto)
        return JSONResponse({
            "ok": True,
            "emocao": emocao,
            "toxicidade": toxicidade,
            "fonte": "HuggingFace"
        })
    except Exception as e:
        return JSONResponse({"erro": str(e)}, status_code=500)

@app.get("/api/ia/modelos-disponiveis")
async def api_modelos_disponiveis():
    return JSONResponse({
        "groq": {
            "disponivel": bool(_os_s10.getenv("GROQ_API_KEY")),
            "modelos": ["llama-3.3-70b", "llama-3.1-8b", "mixtral-8x7b"]
        },
        "together": {
            "disponivel": bool(TOGETHER_API_KEY),
            "modelos": list(TOGETHER_MODELS.keys())
        },
        "huggingface": {
            "disponivel": bool(HUGGINGFACE_API_KEY),
            "modelos": list(HF_MODELS.keys())
        },
        "gemini": {
            "disponivel": bool(_os_s10.getenv("GEMINI_API_KEY")),
            "modelos": ["gemini-1.5-pro", "gemini-1.5-flash"]
        },
        "mistral": {
            "disponivel": bool(_os_s10.getenv("MISTRAL_API_KEY")),
            "modelos": ["mistral-large-2", "codestral"]
        },
        "langchain": {
            "disponivel": LANGCHAIN_DISPONIVEL,
            "modelos": ["groq-llama-3.3-70b"]
        },
        "total_fontes": 6,
        "sistema": "P1 — IA Expandida"
    })

# ═══ FIM P1 — TOGETHER AI + HUGGINGFACE + LANGCHAIN ═════════════════




