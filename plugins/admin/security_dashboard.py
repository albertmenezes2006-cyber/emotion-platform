"""Dashboard visual de segurança"""
import os
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from plugins.plugin_base import PluginBase

router = APIRouter(prefix="/admin", tags=["Admin"])

@router.get("/security", response_class=HTMLResponse, include_in_schema=False)
async def security_dashboard():
    html = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Segurança — EmotionAI Admin</title>
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:-apple-system,sans-serif;background:#0f172a;color:#e2e8f0;padding:20px;min-height:100vh}
.container{max-width:1400px;margin:0 auto}
h1{font-size:28px;margin-bottom:5px;background:linear-gradient(135deg,#6366f1,#ec4899);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.subtitle{color:#94a3b8;margin-bottom:30px;font-size:14px}
.stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:20px;margin-bottom:30px}
.stat{background:#1e293b;border-radius:12px;padding:20px;border-left:4px solid #6366f1}
.stat.danger{border-color:#ef4444}
.stat.warning{border-color:#f59e0b}
.stat.success{border-color:#10b981}
.stat-label{color:#94a3b8;font-size:12px;text-transform:uppercase;letter-spacing:1px}
.stat-value{font-size:36px;font-weight:800;margin-top:5px}
.section{background:#1e293b;border-radius:12px;padding:25px;margin-bottom:20px}
.section h2{font-size:18px;margin-bottom:15px;display:flex;align-items:center;gap:10px}
.table{width:100%;border-collapse:collapse}
.table th{text-align:left;padding:12px;background:#0f172a;color:#94a3b8;font-size:12px;text-transform:uppercase}
.table td{padding:12px;border-bottom:1px solid #334155;font-size:14px}
.table tr:hover{background:#0f172a}
.badge{padding:4px 10px;border-radius:20px;font-size:11px;font-weight:600}
.badge-danger{background:rgba(239,68,68,0.2);color:#ef4444}
.badge-success{background:rgba(16,185,129,0.2);color:#10b981}
.badge-warning{background:rgba(245,158,11,0.2);color:#f59e0b}
.btn{padding:6px 14px;border-radius:6px;font-size:12px;font-weight:600;cursor:pointer;border:none;color:white}
.btn-danger{background:#ef4444}
.btn-danger:hover{background:#dc2626}
.empty{text-align:center;padding:40px;color:#64748b}
.reload{position:fixed;bottom:20px;right:20px;background:#6366f1;color:white;padding:10px 20px;border-radius:50px;font-size:12px;box-shadow:0 4px 20px rgba(99,102,241,0.4)}
.mini{color:#64748b;font-size:11px;margin-top:4px}
.ip{font-family:monospace;background:#0f172a;padding:2px 6px;border-radius:4px;font-size:12px}
</style>
</head>
<body>
<div class="container">
  <h1>🛡️ Segurança em Tempo Real</h1>
  <p class="subtitle">Atualiza automaticamente a cada 30 segundos</p>
  
  <div class="stats" id="stats">
    <div class="stat"><div class="stat-label">Carregando...</div></div>
  </div>
  
  <div class="section">
    <h2>🛑 IPs Bloqueados</h2>
    <div id="bloqueados"><p class="empty">Carregando...</p></div>
  </div>
  
  <div class="section">
    <h2>⚠️ IPs Suspeitos (24h)</h2>
    <div id="suspeitos"><p class="empty">Carregando...</p></div>
  </div>
  
  <div class="section">
    <h2>📋 Últimas Tentativas</h2>
    <div id="eventos"><p class="empty">Carregando...</p></div>
  </div>
</div>

<div class="reload" id="reload">🔄 Atualizando em <span id="timer">30</span>s</div>

<script>
let timer = 30;

function tempo(iso){
  if(!iso) return "-";
  const d = new Date(iso);
  return d.toLocaleString("pt-BR");
}

function tempoRel(iso){
  if(!iso) return "-";
  const diff = (new Date() - new Date(iso)) / 1000;
  if(diff < 60) return Math.floor(diff) + "s atrás";
  if(diff < 3600) return Math.floor(diff/60) + "min atrás";
  if(diff < 86400) return Math.floor(diff/3600) + "h atrás";
  return Math.floor(diff/86400) + "d atrás";
}

async function desbloquear(ip){
  if(!confirm("Desbloquear IP " + ip + "?")) return;
  const r = await fetch("/api/v1/security/desbloquear/" + ip, {method:"POST"});
  const d = await r.json();
  if(d.status === "ok"){
    alert("✅ IP desbloqueado!");
    carregar();
  } else {
    alert("❌ Erro ao desbloquear");
  }
}

async function carregar(){
  try {
    const r = await fetch("/api/v1/security/dashboard?limite=30");
    const d = await r.json();
    
    // Stats
    const totalBloq = (d.ips_bloqueados || []).length;
    const totalSusp = (d.ips_suspeitos || []).length;
    const falhas = d.falhas_24h || 0;
    const eventos = (d.eventos_recentes || []).length;
    
    document.getElementById("stats").innerHTML = `
      <div class="stat ${totalBloq > 0 ? "danger" : "success"}">
        <div class="stat-label">IPs Bloqueados</div>
        <div class="stat-value">${totalBloq}</div>
      </div>
      <div class="stat ${totalSusp > 0 ? "warning" : "success"}">
        <div class="stat-label">IPs Suspeitos</div>
        <div class="stat-value">${totalSusp}</div>
      </div>
      <div class="stat ${falhas > 10 ? "danger" : falhas > 0 ? "warning" : "success"}">
        <div class="stat-label">Falhas 24h</div>
        <div class="stat-value">${falhas}</div>
      </div>
      <div class="stat success">
        <div class="stat-label">Eventos Registrados</div>
        <div class="stat-value">${eventos}</div>
      </div>
    `;
    
    // Bloqueados
    if((d.ips_bloqueados || []).length === 0){
      document.getElementById("bloqueados").innerHTML = "<p class='empty'>✅ Nenhum IP bloqueado no momento</p>";
    } else {
      let html = "<table class='table'><tr><th>IP</th><th>Motivo</th><th>Bloqueado</th><th>Expira</th><th>Ação</th></tr>";
      d.ips_bloqueados.forEach(b => {
        html += `<tr>
          <td><span class="ip">${b.ip}</span></td>
          <td>${b.motivo}</td>
          <td>${tempoRel(b.bloqueado_em)}<div class="mini">${tempo(b.bloqueado_em)}</div></td>
          <td>${tempo(b.expira_em)}</td>
          <td><button class="btn btn-danger" onclick="desbloquear('${b.ip}')">Desbloquear</button></td>
        </tr>`;
      });
      html += "</table>";
      document.getElementById("bloqueados").innerHTML = html;
    }
    
    // Suspeitos
    if((d.ips_suspeitos || []).length === 0){
      document.getElementById("suspeitos").innerHTML = "<p class='empty'>✅ Nenhum IP suspeito nas últimas 24h</p>";
    } else {
      let html = "<table class='table'><tr><th>IP</th><th>Falhas</th></tr>";
      d.ips_suspeitos.forEach(s => {
        html += `<tr>
          <td><span class="ip">${s.ip}</span></td>
          <td><span class="badge badge-warning">${s.falhas} falhas</span></td>
        </tr>`;
      });
      html += "</table>";
      document.getElementById("suspeitos").innerHTML = html;
    }
    
    // Eventos
    if((d.eventos_recentes || []).length === 0){
      document.getElementById("eventos").innerHTML = "<p class='empty'>Sem eventos ainda</p>";
    } else {
      let html = "<table class='table'><tr><th>Quando</th><th>Tipo</th><th>IP</th><th>Email</th><th>Resultado</th></tr>";
      d.eventos_recentes.slice(0, 30).forEach(e => {
        html += `<tr>
          <td>${tempoRel(e.quando)}</td>
          <td>${e.tipo}</td>
          <td><span class="ip">${e.ip}</span></td>
          <td>${e.email || "-"}</td>
          <td>${e.sucesso ? '<span class="badge badge-success">✓ OK</span>' : '<span class="badge badge-danger">✗ Falha</span>'}</td>
        </tr>`;
      });
      html += "</table>";
      document.getElementById("eventos").innerHTML = html;
    }
    
    timer = 30;
  } catch(e) {
    console.error(e);
  }
}

setInterval(() => {
  timer--;
  document.getElementById("timer").textContent = timer;
  if(timer <= 0){
    carregar();
  }
}, 1000);

carregar();
</script>
</body>
</html>"""
    return HTMLResponse(html)

class SecurityDashboardPlugin(PluginBase):
    name = "security_dashboard_visual"
    def setup(self, app):
        app.include_router(router)

plugin = SecurityDashboardPlugin()
