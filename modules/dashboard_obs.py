"""
Dashboard de Observabilidade — Emotion Platform v21.0
Relatório completo do sistema
"""
import os
import psutil
from datetime import datetime
from modules.metricas import metricas
from modules.saude import verificar_saude_sistema

def gerar_relatorio_obs() -> dict:
    saude = verificar_saude_sistema()
    resumo = metricas.resumo()
    return {
        "timestamp": datetime.now().isoformat(),
        "versao": "21.0 ULTIMATE",
        "saude": saude,
        "metricas": resumo,
        "qualidade": {
            "taxa_sucesso_pct": round(100 - resumo["taxa_erro_pct"], 2),
            "performance": "excelente" if resumo["tempo_medio_ms"] < 500
                          else "boa" if resumo["tempo_medio_ms"] < 1500
                          else "lenta",
            "carga": "baixa" if resumo["cpu_pct"] < 30
                    else "media" if resumo["cpu_pct"] < 70
                    else "alta"
        }
    }

def imprimir_relatorio():
    r = gerar_relatorio_obs()
    m = r["metricas"]
    s = r["saude"]["sistema"]
    q = r["qualidade"]
    print(f"""
{'═'*50}
  OBSERVABILIDADE — {r['timestamp'][:16]}
{'═'*50}
  🏥 Saúde:        {r['saude']['status'].upper()}
  ⚡ Performance:  {q['performance'].upper()}
  📊 Carga:        {q['carga'].upper()}
{'─'*50}
  📈 Requests:     {m['requests_total']} total | {m['taxa_erro_pct']}% erro
  ⏱️  Tempo médio:  {m['tempo_medio_ms']}ms
  👥 Usuários:     {m['usuarios_ativos_sessao']} ativos
  🧠 CPU:          {s['cpu_pct']}%
  💾 Memória:      {s['memoria_pct']}%
  💿 Disco:        {s['disco_pct']}%
{'─'*50}
  🎭 Top emoções:  {m['top_emocoes'][:3]}
  🤖 IA chamadas:  {m['ia_chamadas']}
{'═'*50}
""")
