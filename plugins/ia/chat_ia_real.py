"""Plugin: Chat IA Real v5 — com retry, cache e rotação de modelos"""
from plugins.plugin_base import PluginBase
from fastapi import APIRouter, HTTPException
from datetime import datetime
from plugins.db_manager import SimpleDB
import os, uuid, json, logging, time

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/v1/chat-ia", tags=["ia"])
_conversas = SimpleDB("chat_ia_v5")

# Cache simples para evitar rate limit
_cache = {}
_cache_ttl = 300  # 5 minutos

SYSTEM = (
    "Voce e um assistente de saude mental empatico da EmotionAI. "
    "Responda SEMPRE em portugues brasileiro de forma acolhedora. "
    "Use tecnicas de TCC, DBT e Mindfulness. "
    "Em crises: diga CVV 188 e SAMU 192. "
    "Maximo 200 palavras. NAO substitua profissionais."
)

CRISIS_WORDS = [
    "suicidio","suicídio","me matar","nao quero viver",
    "nao quero mais","acabar com tudo","me machucar","me machucar"
]

RESPOSTAS_INTELIGENTES = [
    # (palavras_chave, resposta)
    (["ansio","nervos","panico","pânico"], 
     "Entendo que voce esta sentindo ansiedade agora. Vamos fazer a respiracao 4-7-8 juntos:\n\n"
     "1. Expire todo o ar pela boca\n"
     "2. Inspire pelo nariz contando **4 segundos**\n"
     "3. Segure o ar por **7 segundos**\n"
     "4. Expire lentamente por **8 segundos**\n\n"
     "Repita 4 vezes. Isso ativa o sistema nervoso parassimpatico e reduz a ansiedade em minutos. "
     "Como voce esta se sentindo agora?"),
    
    (["trist","choran","chorar","deprim","sem energia","cansad"],
     "Sinto muito que voce esteja passando por isso. 💙 A tristeza e uma emocao valida e "
     "temporaria, mesmo quando parece que nao vai passar.\n\n"
     "Algumas coisas que podem ajudar agora:\n"
     "• Tome uma agua gelada\n"
     "• Saia para caminhar 10 minutos (mesmo dentro de casa)\n"
     "• Ligue para alguem de confianca\n\n"
     "Me conta mais: o que esta acontecendo em sua vida?"),
    
    (["respiracao","respiração","4-7-8","respira"],
     "**Tecnica de Respiracao 4-7-8** 🌬️\n\n"
     "Sente-se confortavelmente. Vamos comecar:\n\n"
     "**Passo 1:** Expire completamente pela boca (som de whoosh)\n"
     "**Passo 2:** Feche a boca, inspire pelo nariz: 1... 2... 3... **4**\n"
     "**Passo 3:** Segure o ar: 1... 2... 3... 4... 5... 6... **7**\n"
     "**Passo 4:** Expire pela boca fazendo som: 1... 2... 3... 4... 5... 6... 7... **8**\n\n"
     "Isso e 1 ciclo. Repita mais 3 vezes. Quer tentar agora?"),
    
    (["dormir","insonia","insônia","nao consigo dormir","nao durmo"],
     "Dificuldades para dormir sao muito comuns e afetam muito o bem-estar. 😴\n\n"
     "**Dicas baseadas em evidencias:**\n"
     "• Mantenha horario fixo (mesmo fins de semana)\n"
     "• Evite telas 1h antes de dormir (ative modo noite)\n"
     "• Quarto escuro, fresco (18-20°C) e silencioso\n"
     "• Tecnica 4-7-8 ajuda a adormecer\n"
     "• Evite cafeina apos as 14h\n\n"
     "O que costuma passar pela sua cabeca quando tenta dormir?"),
    
    (["mindf","meditac","meditaç","atenção plena"],
     "**Mindfulness** e a pratica de estar presente no momento atual, sem julgamentos. 🧘\n\n"
     "**Exercicio rapido (2 minutos):**\n"
     "1. Sente-se ou deite confortavelmente\n"
     "2. Feche os olhos\n"
     "3. Respire naturalmente\n"
     "4. Observe: o que voce **sente** no corpo? O que voce **ouve**?\n"
     "5. Quando pensamentos vierem, apenas observe e volte a respiracao\n\n"
     "Praticar 5-10 minutos por dia ja traz beneficios comprovados pela ciencia!"),
    
    (["raiva","irritad","bravo","com raiva","muito nervoso"],
     "A raiva e uma emocao valida — ela nos avisa que algo importante foi violado. 😤\n\n"
     "**Para agora:**\n"
     "• Afaste-se da situacao por 10 minutos\n"
     "• Respire fundo 10 vezes\n"
     "• Beba agua gelada\n"
     "• Escreva o que esta sentindo (nao precisa enviar)\n\n"
     "**Lembre:** voce pode sentir raiva SEM agir com raiva.\n\n"
     "O que aconteceu que te deixou assim?"),
    
    (["motivacao","motivação","desanimo","desânimo","sem vontade","procrastin"],
     "Falta de motivacao e muito mais comum do que parece, e geralmente e sinal de que "
     "algo precisa de atencao. 💪\n\n"
     "**Tecnica do menor passo:**\n"
     "Em vez de pensar na tarefa toda, pergunte: qual e o menor passo possivel que eu "
     "poderia dar agora? (pode ser abrir um documento, se levantar, beber agua)\n\n"
     "**Ciencia diz:** a acao vem ANTES da motivacao, nao o contrario. "
     "Comece pequeno e a motivacao aparece.\n\n"
     "O que voce esta precisando fazer e nao consegue comecar?"),
    
    (["sozinho","sozinha","solidao","solidão","sem amigos","ninguem"],
     "Sentir-se sozinho e uma das experiencias mais dolorosas que existem. 💙 "
     "E importante reconhecer isso.\n\n"
     "Conexoes humanas sao fundamentais para a saude mental. Algumas ideias:\n"
     "• Grupos de interesse (clubes, voluntariado, cursos)\n"
     "• Apps de conexao social saudavel\n"
     "• Terapia em grupo\n"
     "• Animais de estimacao\n\n"
     "Ha alguem — mesmo distante — com quem voce poderia entrar em contato hoje?"),
    
    (["tcc","terapia cognitiva","pensamento automatico","distorcao"],
     "**TCC (Terapia Cognitivo-Comportamental)** e uma das abordagens mais eficazes "
     "e estudadas na psicologia. 🧠\n\n"
     "**Base:** nossos pensamentos afetam nossas emocoes, que afetam nossos comportamentos.\n\n"
     "**Exemplo pratico:**\n"
     "Situacao: amigo nao responde mensagem\n"
     "Pensamento automatico: 'ele me odeia'\n"
     "Emocao: tristeza, ansiedade\n"
     "Comportamento: se isolar\n\n"
     "A TCC ensina a identificar e questionar esses pensamentos. "
     "Posso te ensinar uma tecnica agora?"),
    
    (["ajuda","socorro","nao sei o que fazer","perdido","perdida"],
     "Estou aqui para te ajudar. 💙 E muito corajoso buscar apoio.\n\n"
     "Me conta: o que esta acontecendo? Quanto mais detalhes voce compartilhar, "
     "mais posso te ajudar de forma especifica.\n\n"
     "Se for urgente:\n"
     "• **CVV: 188** (24h, gratuito)\n"
     "• **SAMU: 192**\n"
     "• Procure um CAPS ou UBS"),
    
    (["obrigado","obrigada","valeu","ajudou","melhor"],
     "Fico muito feliz em poder ajudar! 🌟 Cuidar da saude mental e um ato de coragem "
     "e amor proprio.\n\n"
     "Continue praticando as tecnicas que conversamos. Lembre que:\n"
     "• Pequenas acoes diarias fazem grande diferenca\n"
     "• Buscar ajuda profissional e sempre uma opcao valida\n"
     "• Voce nao esta sozinho nessa jornada 💙\n\n"
     "Ha mais alguma coisa em que posso te ajudar?"),
]

def _fallback_inteligente(mensagem: str) -> str:
    baixo = mensagem.lower()
    for palavras, resposta in RESPOSTAS_INTELIGENTES:
        if any(p in baixo for p in palavras):
            return resposta
    return (
        "Estou aqui para te ouvir e apoiar. 💙\n\n"
        "Me conta mais sobre o que esta sentindo ou passando. "
        "Quanto mais voce compartilhar, melhor posso te ajudar de forma personalizada.\n\n"
        "Lembre: em emergencias, o CVV (188) esta disponivel 24h gratuitamente."
    )

def _get_cache_key(mensagem: str) -> str:
    return mensagem.lower().strip()[:50]

def _check_cache(key: str):
    if key in _cache:
        ts, resp, modelo = _cache[key]
        if time.time() - ts < _cache_ttl:
            return resp, modelo + " (cache)"
    return None, None

def _set_cache(key: str, resp: str, modelo: str):
    _cache[key] = (time.time(), resp, modelo)
    # Limitar cache a 100 entradas
    if len(_cache) > 100:
        oldest = min(_cache.keys(), key=lambda k: _cache[k][0])
        del _cache[oldest]

async def _tentar_ia(mensagem: str, modelo_pref: str = "auto") -> tuple:
    """Tenta múltiplos modelos com timeout reduzido"""
    import httpx
    
    msgs = [
        {"role": "system", "content": SYSTEM},
        {"role": "user", "content": mensagem}
    ]
    
    # Definir ordem baseada na preferência
    if modelo_pref == "mistral":
        ordem = ["mistral", "openrouter", "gemini", "groq"]
    elif modelo_pref == "groq":
        ordem = ["groq", "mistral", "openrouter", "gemini"]
    elif modelo_pref == "gemini":
        ordem = ["gemini", "mistral", "openrouter", "groq"]
    else:
        # Auto: tentar todos, começando pelo que tem menos issues
        ordem = ["mistral", "openrouter", "gemini", "groq"]
    
    for modelo_id in ordem:
        try:
            if modelo_id == "mistral":
                key = os.getenv("MISTRAL_API_KEY","")
                if not key: continue
                async with httpx.AsyncClient(timeout=15) as c:
                    r = await c.post(
                        "https://api.mistral.ai/v1/chat/completions",
                        headers={"Authorization": "Bearer " + key},
                        json={"model":"mistral-small-latest","messages":msgs,
                              "max_tokens":300,"temperature":0.7}
                    )
                    if r.status_code == 200:
                        t = r.json()["choices"][0]["message"]["content"].strip()
                        if t: return t, "mistral-small"
                    elif r.status_code == 429:
                        logger.warning("Mistral rate limit — tentando proximo")
                        continue
                        
            elif modelo_id == "openrouter":
                key = os.getenv("OPENROUTER_API_KEY","")
                if not key: continue
                async with httpx.AsyncClient(timeout=20) as c:
                    r = await c.post(
                        "https://openrouter.ai/api/v1/chat/completions",
                        headers={
                            "Authorization": "Bearer " + key,
                            "HTTP-Referer": "https://emotion-platform-albert.onrender.com"
                        },
                        json={"model":"meta-llama/llama-3.1-8b-instruct:free",
                              "messages":msgs,"max_tokens":300}
                    )
                    if r.status_code == 200:
                        t = r.json()["choices"][0]["message"]["content"].strip()
                        if t: return t, "llama-3.1-8b"
                        
            elif modelo_id == "gemini":
                key = os.getenv("GEMINI_API_KEY","")
                if not key: continue
                prompt = SYSTEM + "\n\nUsuario: " + mensagem
                url = ("https://generativelanguage.googleapis.com/v1beta/"
                       "models/gemini-1.5-flash:generateContent?key=" + key)
                async with httpx.AsyncClient(timeout=15) as c:
                    r = await c.post(url, json={
                        "contents":[{"parts":[{"text":prompt}]}],
                        "generationConfig":{"maxOutputTokens":300,"temperature":0.7}
                    })
                    if r.status_code == 200:
                        t = r.json()["candidates"][0]["content"]["parts"][0]["text"].strip()
                        if t: return t, "gemini-1.5-flash"
                        
            elif modelo_id == "groq":
                key = os.getenv("GROQ_API_KEY","")
                if not key: continue
                async with httpx.AsyncClient(timeout=15) as c:
                    r = await c.post(
                        "https://api.groq.com/openai/v1/chat/completions",
                        headers={"Authorization": "Bearer " + key},
                        json={"model":"llama3-8b-8192","messages":msgs,
                              "max_tokens":300,"temperature":0.7}
                    )
                    if r.status_code == 200:
                        t = r.json()["choices"][0]["message"]["content"].strip()
                        if t: return t, "groq/llama3-8b"
                    elif r.status_code == 429:
                        logger.warning("Groq rate limit")
                        
        except Exception as e:
            logger.debug(f"{modelo_id} error: {e}")
            continue
    
    return None, None


class ChatIaRealPlugin(PluginBase):
    name = "chat_ia_real"
    version = "5.0.0"
    description = "Chat IA v5 — retry + cache + fallback inteligente"
    category = "ia"

    def setup(self, app):
        app.include_router(router)
        logger.info("[chat_ia_real v5] OK")

    def health_check(self):
        return {
            "status": "healthy",
            "versao": "5.0.0",
            "cache_entries": len(_cache),
            "modelos": {
                "mistral": bool(os.getenv("MISTRAL_API_KEY")),
                "openrouter": bool(os.getenv("OPENROUTER_API_KEY")),
                "gemini": bool(os.getenv("GEMINI_API_KEY")),
                "groq": bool(os.getenv("GROQ_API_KEY")),
            }
        }


@router.get("/modelos/disponiveis")
async def modelos_disponiveis():
    return {"modelos": [
        {"id":"auto","nome":"Auto (melhor disponivel)","disponivel":True,"velocidade":"variavel"},
        {"id":"mistral","nome":"Mistral Small","disponivel":bool(os.getenv("MISTRAL_API_KEY")),"velocidade":"rapida"},
        {"id":"openrouter","nome":"OpenRouter LLaMA3","disponivel":bool(os.getenv("OPENROUTER_API_KEY")),"velocidade":"media"},
        {"id":"gemini","nome":"Google Gemini Flash","disponivel":bool(os.getenv("GEMINI_API_KEY")),"velocidade":"rapida"},
        {"id":"groq","nome":"Groq LLaMA3","disponivel":bool(os.getenv("GROQ_API_KEY")),"velocidade":"muito_rapida"},
        {"id":"fallback","nome":"Respostas terapeuticas","disponivel":True,"velocidade":"instantanea"},
    ]}


@router.post("/mensagem")
async def enviar_mensagem(
    user_id: str = "anonimo",
    mensagem: str = "",
    historico_conversa: list = None,
    modelo: str = "auto"
):
    if not mensagem or len(mensagem.strip()) < 1:
        raise HTTPException(400, "Mensagem vazia")

    mensagem = mensagem.strip()
    
    # Verificar cache
    cache_key = _get_cache_key(mensagem)
    resp_cache, modelo_cache = _check_cache(cache_key)
    if resp_cache:
        logger.info(f"Cache hit: {cache_key[:30]}")
        return {
            "conversa_id": str(uuid.uuid4())[:8],
            "user_id": user_id,
            "mensagem": mensagem,
            "resposta": resp_cache,
            "modelo_usado": modelo_cache,
            "alerta_crise": False,
            "timestamp": datetime.utcnow().isoformat(),
        }
    
    # Tentar IA real
    resposta, modelo_usado = await _tentar_ia(mensagem, modelo)
    
    # Se IA falhou, usar fallback inteligente
    if not resposta:
        resposta = _fallback_inteligente(mensagem)
        modelo_usado = "fallback"
        logger.info(f"Usando fallback para: {mensagem[:50]}")
    else:
        # Cachear resposta da IA
        _set_cache(cache_key, resposta, modelo_usado)
    
    # Detectar crise
    is_crisis = any(w in mensagem.lower() for w in CRISIS_WORDS)
    if is_crisis:
        resposta = "🚨 CVV: 188 (24h gratuito) | SAMU: 192\n\n" + resposta
        logger.warning(f"CRISE: user={user_id}")
    
    # Salvar
    try:
        _conversas.create(
            nome="Chat " + user_id, user_id=user_id,
            valor=modelo_usado or "?",
            dados=json.dumps({
                "msg": mensagem[:150],
                "resp": resposta[:150],
                "modelo": modelo_usado
            }),
            categoria="crise" if is_crisis else "normal"
        )
    except Exception:
        pass
    
    return {
        "conversa_id": str(uuid.uuid4())[:8],
        "user_id": user_id,
        "mensagem": mensagem,
        "resposta": resposta,
        "modelo_usado": modelo_usado,
        "alerta_crise": is_crisis,
        "timestamp": datetime.utcnow().isoformat(),
        "recursos_emergencia": {"cvv":"188","samu":"192"} if is_crisis else None
    }


@router.get("/historico/{user_id}")
async def historico(user_id: str, limite: int = 20):
    convs = _conversas.list(user_id=user_id, limite=limite)
    return {"total": len(convs), "conversas": convs}


plugin = ChatIaRealPlugin()
