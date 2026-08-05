from PIL import Image, ImageDraw, ImageFont, ImageEnhance
import subprocess, os

print("🎬 Criando Reels v4.0 — Layout Limpo e Profissional...")
os.makedirs("reels4_temp", exist_ok=True)

W, H = 1080, 1920

def font(size, bold=False):
    try:
        p = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
        return ImageFont.truetype(p, size)
    except:
        return ImageFont.load_default()

def get_dur(audio):
    r = subprocess.run(
        ['ffprobe','-v','quiet','-show_entries','format=duration',
         '-of','default=noprint_wrappers=1:nokey=1', audio],
        capture_output=True, text=True)
    return float(r.stdout.strip())

def draw_text_center(draw, texto, y, fnt, cor, sombra=True, max_w=900):
    palavras = texto.split()
    linhas, linha = [], ""
    for p in palavras:
        teste = linha + " " + p if linha else p
        bb = draw.textbbox((0,0), teste, font=fnt)
        if bb[2]-bb[0] > max_w and linha:
            linhas.append(linha)
            linha = p
        else:
            linha = teste
    if linha:
        linhas.append(linha)

    y_atual = y
    for l in linhas:
        bb = draw.textbbox((0,0), l, font=fnt)
        h_linha = bb[3] - bb[1]
        tw = bb[2] - bb[0]
        x = (W - tw) // 2
        if sombra:
            for dx,dy in [(3,3),(-3,3),(3,-3),(-3,-3),(0,4)]:
                draw.text((x+dx, y_atual+dy), l, font=fnt, fill=(0,0,0,200))
        draw.text((x, y_atual), l, font=fnt, fill=cor)
        y_atual += h_linha + 20
    return y_atual

def criar_frame(bg_path, estilo, elemento_principal, elemento_secundario, elemento_terciario, output):
    # Abrir e tratar imagem
    bg = Image.open(bg_path).resize((W, H), Image.LANCZOS)
    bg = ImageEnhance.Contrast(bg).enhance(1.2)
    bg = ImageEnhance.Brightness(bg).enhance(0.45)
    bg = ImageEnhance.Color(bg).enhance(1.1)
    bg = bg.convert("RGBA")

    # Overlay
    ov = Image.new("RGBA", (W,H), (0,0,0,0))
    d = ImageDraw.Draw(ov)

    if estilo == "gancho":
        for i in range(H):
            a = int(140 * (1 - i/H)) + 60
            d.rectangle([(0,i),(W,i+1)], fill=(40,0,60,min(a,180)))
    elif estilo == "dor":
        d.rectangle([(0,0),(W,H)], fill=(0,0,0,160))
    elif estilo == "virada":
        for i in range(H):
            a = int(170 * (i/H))
            d.rectangle([(0,i),(W,i+1)], fill=(60,15,100,min(a,170)))
    elif estilo == "reveal":
        d.rectangle([(0,0),(W,H)], fill=(5,0,20,150))
        for i in range(300):
            a = int(120*(1-i/300))
            d.rectangle([(0,i),(W,i+1)], fill=(80,20,180,a))
    elif estilo == "cta":
        for i in range(H):
            a = int(190*(i/H))
            d.rectangle([(0,i),(W,i+1)], fill=(50,0,80,min(a,190)))

    bg = Image.alpha_composite(bg, ov)
    draw = ImageDraw.Draw(bg)

    # Linha decorativa topo
    draw.rectangle([(0,0),(W,8)], fill=(167,139,250))
    draw.rectangle([(0,8),(W,14)], fill=(250,204,21))

    # HIERARQUIA VISUAL CLARA:
    # 1. Elemento principal — grande, centralizado verticalmente
    # 2. Elemento secundario — medio, abaixo
    # 3. Elemento terciario — pequeno, discreto

    centro_v = H // 2

    # Principal (bem grande, impacto)
    if elemento_principal:
        f1 = font(elemento_principal.get("size", 110), True)
        y1 = draw_text_center(draw,
            elemento_principal["texto"],
            centro_v - 200,
            f1,
            elemento_principal.get("cor", (255,255,255)),
            max_w=elemento_principal.get("max_w", 940))

    # Linha divisoria decorativa
    if elemento_secundario:
        draw.rectangle([(W//4, centro_v-20),(W*3//4, centro_v-14)], fill=(167,139,250,180))

    # Secundario (medio, complemento)
    if elemento_secundario:
        f2 = font(elemento_secundario.get("size", 65), elemento_secundario.get("bold", False))
        y2 = draw_text_center(draw,
            elemento_secundario["texto"],
            centro_v + 10,
            f2,
            elemento_secundario.get("cor", (196,181,253)),
            max_w=elemento_secundario.get("max_w", 860))

    # Terciario (pequeno, discreto)
    if elemento_terciario:
        f3 = font(elemento_terciario.get("size", 48), False)
        draw_text_center(draw,
            elemento_terciario["texto"],
            centro_v + 180,
            f3,
            elemento_terciario.get("cor", (167,139,250)),
            sombra=False,
            max_w=800)

    # Badge inferior
    draw.rectangle([(0,H-150),(W,H)], fill=(10,0,25,240))
    draw.rectangle([(0,H-152),(W,H-144)], fill=(167,139,250))
    draw_text_center(draw, "@emotionai_br", H-125, font(42,True), (250,204,21), sombra=False)
    draw_text_center(draw, "Link na bio — Gratis para comecar", H-72, font(32,False), (134,239,172), sombra=False)

    bg.convert("RGB").save(output, quality=98)

# CENAS — máximo 3 elementos por cena, hierarquia clara
cenas = [
    {
        "bg": "reels2_frames/home_top.png",
        "audio": "reels2_audio/gancho.mp3",
        "estilo": "gancho",
        "principal":   {"texto": "⚡ PARA.", "size": 160, "cor": (250,204,21)},
        "secundario":  {"texto": "Voce ainda cuida da sua saude mental do jeito antigo?", "size": 62, "cor": (255,255,255), "bold": False},
        "terciario":   {"texto": "Continue assistindo 👇", "size": 46, "cor": (167,139,250)},
    },
    {
        "bg": "reels2_frames/home_meio.png",
        "audio": "reels2_audio/dor1.mp3",
        "estilo": "dor",
        "principal":   {"texto": "Ansiedade. Insonia. Pensamentos que nao param.", "size": 82, "cor": (252,165,165), "max_w": 900},
        "secundario":  {"texto": "Sensacao de que ninguem entende.", "size": 58, "cor": (255,255,255), "bold": False},
        "terciario":   None,
    },
    {
        "bg": "reels2_frames/home_baixo.png",
        "audio": "reels2_audio/dor2.mp3",
        "estilo": "dor",
        "principal":   {"texto": "E quando voce resolve buscar ajuda...", "size": 78, "cor": (255,255,255)},
        "secundario":  {"texto": "nao sabe por onde comecar.", "size": 72, "cor": (252,165,165), "bold": True},
        "terciario":   None,
    },
    {
        "bg": "reels2_frames/home_top.png",
        "audio": "reels2_audio/virada.mp3",
        "estilo": "virada",
        "principal":   {"texto": "🤯 E SE EU TE DISSESSE...", "size": 95, "cor": (250,204,21)},
        "secundario":  {"texto": "Plataforma brasileira e GRATUITA com Inteligencia Artificial.", "size": 60, "cor": (255,255,255), "bold": False, "max_w": 880},
        "terciario":   {"texto": "Feita para isso. 👇", "size": 50, "cor": (167,139,250)},
    },
    {
        "bg": "reels2_frames/chat.png",
        "audio": "reels2_audio/reveal1.mp3",
        "estilo": "reveal",
        "principal":   {"texto": "💬 CHAT COM IA", "size": 110, "cor": (167,139,250)},
        "secundario":  {"texto": "Empatia real. 24h por dia. Sem julgamento.", "size": 60, "cor": (255,255,255), "bold": False},
        "terciario":   {"texto": "Sempre disponivel. Sem fila de espera.", "size": 46, "cor": (134,239,172)},
    },
    {
        "bg": "reels2_frames/avaliacao.png",
        "audio": "reels2_audio/reveal2.mp3",
        "estilo": "reveal",
        "principal":   {"texto": "PHQ-9 e GAD-7", "size": 120, "cor": (250,204,21)},
        "secundario":  {"texto": "Avaliacoes clinicas reais. As mesmas que psicologos usam.", "size": 58, "cor": (255,255,255), "bold": False, "max_w": 880},
        "terciario":   {"texto": "✅ Gratis. Em 2 minutos.", "size": 52, "cor": (134,239,172)},
    },
    {
        "bg": "reels2_frames/dashboard.png",
        "audio": "reels2_audio/reveal3.mp3",
        "estilo": "reveal",
        "principal":   {"texto": "📈 Sua Evolucao Emocional", "size": 90, "cor": (167,139,250)},
        "secundario":  {"texto": "Acompanhe seu progresso dia apos dia.", "size": 62, "cor": (255,255,255), "bold": False},
        "terciario":   {"texto": "Isso muda tudo. 🔥", "size": 55, "cor": (250,204,21)},
    },
    {
        "bg": "reels2_frames/mindfulness.png",
        "audio": "reels2_audio/reveal4.mp3",
        "estilo": "reveal",
        "principal":   {"texto": "🧘 Mindfulness e Meditacao", "size": 92, "cor": (167,139,250)},
        "secundario":  {"texto": "Tecnicas com evidencias cientificas no seu celular.", "size": 58, "cor": (255,255,255), "bold": False, "max_w": 880},
        "terciario":   {"texto": "A qualquer hora. 🌙", "size": 52, "cor": (250,204,21)},
    },
    {
        "bg": "reels2_frames/home_top.png",
        "audio": "reels2_audio/cta.mp3",
        "estilo": "cta",
        "principal":   {"texto": "🚀 E GRATUITO", "size": 130, "cor": (250,204,21)},
        "secundario":  {"texto": "Porque saude mental nao e privilegio.", "size": 62, "cor": (255,255,255), "bold": False},
        "terciario":   {"texto": "🔗 Link na bio. Acesse agora.", "size": 54, "cor": (134,239,172)},
    },
]

clips = []
for i, c in enumerate(cenas):
    print(f"  🎨 Cena {i+1}/9 — {c['estilo']}...")
    frame = f"reels4_temp/frame_{i:02d}.jpg"
    clip  = f"reels4_temp/clip_{i:02d}.mp4"

    criar_frame(c["bg"], c["estilo"],
                c.get("principal"), c.get("secundario"), c.get("terciario"),
                frame)

    dur = get_dur(c["audio"])

    subprocess.run([
        'ffmpeg','-y','-loop','1','-i',frame,'-i',c["audio"],
        '-filter_complex',
        f'[0:v]scale=8000:-1,zoompan=z=\'min(zoom+0.0005,1.06)\':d={int(dur*25)}:x=\'iw/2-(iw/zoom/2)\':y=\'ih/2-(ih/zoom/2)\':s=1080x1920,fps=25[v]',
        '-map','[v]','-map','1:a',
        '-c:v','libx264','-preset','slow','-crf','16',
        '-c:a','aac','-b:a','192k','-pix_fmt','yuv420p',
        '-t',str(dur), clip
    ], capture_output=True)

    clips.append(clip)
    print(f"    ✅ {dur:.1f}s")

# Lista para concatenar
lista = "reels4_temp/lista.txt"
with open(lista, 'w') as f:
    for c in clips:
        f.write(f"file '{os.path.abspath(c)}'\n")

# Concatenar
print("\n🎬 Concatenando...")
subprocess.run([
    'ffmpeg','-y','-f','concat','-safe','0',
    '-i', lista,'-c','copy','reels4_temp/base.mp4'
], capture_output=True)

# Adicionar musica
print("🎵 Adicionando musica...")
subprocess.run([
    'ffmpeg','-y',
    '-i','reels4_temp/base.mp4',
    '-i','reels_musica_bg.mp3',
    '-filter_complex',
    '[1:a]volume=0.12[m];[0:a]volume=1.0[v];[v][m]amix=inputs=2:duration=first[a]',
    '-map','0:v','-map','[a]',
    '-c:v','copy','-c:a','aac','-b:a','256k',
    '-shortest','reels_V4_FINAL.mp4'
], capture_output=True)

size = os.path.getsize('reels_V4_FINAL.mp4')/(1024*1024)
print(f"\n🎉 REELS V4 PRONTO!")
print(f"📁 reels_V4_FINAL.mp4")
print(f"📦 {size:.1f} MB")
print(f"✅ Layout limpo — max 3 elementos por cena")
print(f"✅ Hierarquia visual clara")
print(f"✅ Musica emocional")
print(f"✅ Ken Burns suave")
