from PIL import Image, ImageDraw, ImageFont, ImageEnhance
import subprocess, os

print("🎬 Criando Reels PERFEITO v3.1...")
os.makedirs("reels3_temp", exist_ok=True)

W, H = 1080, 1920

def get_font(size, bold=False):
    try:
        path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
        return ImageFont.truetype(path, size)
    except:
        return ImageFont.load_default()

def get_dur(audio):
    r = subprocess.run(
        ['ffprobe','-v','quiet','-show_entries','format=duration',
         '-of','default=noprint_wrappers=1:nokey=1', audio],
        capture_output=True, text=True
    )
    return float(r.stdout.strip())

def wrap_center(draw, texto, y, font, cor, max_width=950, sombra=True, spacing=12):
    palavras = texto.split()
    linhas, linha = [], ""
    for p in palavras:
        teste = linha + " " + p if linha else p
        bb = draw.textbbox((0,0), teste, font=font)
        if bb[2]-bb[0] > max_width and linha:
            linhas.append(linha)
            linha = p
        else:
            linha = teste
    if linha:
        linhas.append(linha)

    h = draw.textbbox((0,0), "Ag", font=font)[3]
    yy = y
    for l in linhas:
        bb = draw.textbbox((0,0), l, font=font)
        tw = bb[2]-bb[0]
        x = (W - tw)//2
        if sombra:
            draw.text((x+3, yy+3), l, font=font, fill=(0,0,0))
        draw.text((x, yy), l, font=font, fill=cor)
        yy += h + spacing

def criar_frame(bg_path, estilo, textos, output):
    bg = Image.open(bg_path).resize((W, H), Image.LANCZOS)
    bg = ImageEnhance.Contrast(bg).enhance(1.25)
    bg = ImageEnhance.Brightness(bg).enhance(0.60)
    bg = ImageEnhance.Color(bg).enhance(1.20)
    bg = bg.convert("RGBA")

    overlay = Image.new("RGBA", (W,H), (0,0,0,0))
    d = ImageDraw.Draw(overlay)

    if estilo == "gancho":
        d.rectangle([(0,0),(W,H)], fill=(20,0,40,120))
    elif estilo == "dor":
        d.rectangle([(0,0),(W,H)], fill=(0,0,0,170))
    elif estilo == "virada":
        d.rectangle([(0,0),(W,H)], fill=(70,20,120,150))
    elif estilo == "reveal":
        d.rectangle([(0,0),(W,H)], fill=(10,0,30,145))
    elif estilo == "cta":
        d.rectangle([(0,0),(W,H)], fill=(50,0,90,170))

    bg = Image.alpha_composite(bg, overlay)
    draw = ImageDraw.Draw(bg)

    draw.rectangle([(0,0),(W,10)], fill=(167,139,250))
    draw.rectangle([(0,10),(W,14)], fill=(250,204,21))

    for t in textos:
        font = get_font(t.get("size",70), t.get("bold",True))
        wrap_center(draw, t["texto"], t["y"], font, t.get("cor",(255,255,255)), t.get("max_w",950))

    draw.rectangle([(0,H-160),(W,H)], fill=(15,0,35,235))
    font1 = get_font(38, True)
    font2 = get_font(30, False)
    wrap_center(draw, "@emotionai_br", H-135, font1, (250,204,21))
    wrap_center(draw, "emotion-platform-albert.onrender.com", H-90, font2, (196,181,253))
    wrap_center(draw, "Link na bio | Gratis para comecar", H-50, font2, (134,239,172), sombra=False)

    bg.convert("RGB").save(output, quality=97)

cenas = [
    ("reels2_frames/home_top.png", "reels2_audio/gancho.mp3", "gancho", [
        {"texto":"⚡ PARA TUDO!", "y":130, "size":140, "cor":(250,204,21)},
        {"texto":"Voce ainda cuida da sua saude mental do jeito antigo?", "y":320, "size":70},
        {"texto":"Continue vendo...", "y":560, "size":54, "cor":(167,139,250), "bold":False},
    ]),
    ("reels2_frames/home_meio.png", "reels2_audio/dor1.mp3", "dor", [
        {"texto":"Ansiedade. Insonia. Pensamentos que nao param.", "y":220, "size":82, "cor":(252,165,165)},
        {"texto":"Sensacao de que ninguem entende voce.", "y":430, "size":60, "cor":(255,255,255), "bold":False},
    ]),
    ("reels2_frames/home_baixo.png", "reels2_audio/dor2.mp3", "dor", [
        {"texto":"E quando voce resolve buscar ajuda...", "y":250, "size":72},
        {"texto":"nao sabe por onde comecar.", "y":430, "size":88, "cor":(252,165,165)},
    ]),
    ("reels2_frames/home_top.png", "reels2_audio/virada.mp3", "virada", [
        {"texto":"🤯 E se eu te dissesse...", "y":130, "size":84, "cor":(250,204,21)},
        {"texto":"que existe uma plataforma brasileira e gratis", "y":300, "size":66},
        {"texto":"com Inteligencia Artificial?", "y":470, "size":78, "cor":(167,139,250)},
    ]),
    ("reels2_frames/chat.png", "reels2_audio/reveal1.mp3", "reveal", [
        {"texto":"💬 CHAT COM IA", "y":110, "size":96, "cor":(167,139,250)},
        {"texto":"Empatia 24h por dia", "y":260, "size":76, "cor":(250,204,21)},
        {"texto":"Sem julgamento. Sem fila de espera.", "y":400, "size":62},
    ]),
    ("reels2_frames/avaliacao.png", "reels2_audio/reveal2.mp3", "reveal", [
        {"texto":"📊 PHQ-9 E GAD-7", "y":130, "size":92, "cor":(250,204,21)},
        {"texto":"Avaliacoes clinicas reais", "y":280, "size":68, "cor":(167,139,250)},
        {"texto":"Gratis. Em 2 minutos.", "y":430, "size":74, "cor":(134,239,172)},
    ]),
    ("reels2_frames/dashboard.png", "reels2_audio/reveal3.mp3", "reveal", [
        {"texto":"📈 DASHBOARD EMOCIONAL", "y":120, "size":82, "cor":(167,139,250)},
        {"texto":"Acompanhe sua evolucao dia apos dia", "y":290, "size":66},
        {"texto":"Isso muda tudo.", "y":450, "size":82, "cor":(250,204,21)},
    ]),
    ("reels2_frames/mindfulness.png", "reels2_audio/reveal4.mp3", "reveal", [
        {"texto":"🧘 MINDFULNESS E MEDITACAO", "y":120, "size":72, "cor":(167,139,250)},
        {"texto":"Tecnicas com evidencias cientificas", "y":290, "size":62},
        {"texto":"No seu celular. A qualquer hora.", "y":430, "size":70, "cor":(250,204,21)},
    ]),
    ("reels2_frames/home_top.png", "reels2_audio/cta.mp3", "cta", [
        {"texto":"🚀 ACESSE AGORA", "y":170, "size":118, "cor":(250,204,21)},
        {"texto":"E gratis para comecar", "y":370, "size":86},
        {"texto":"Saude mental nao e privilegio.", "y":560, "size":64, "cor":(252,165,165)},
        {"texto":"Link na bio", "y":720, "size":88, "cor":(134,239,172)},
    ]),
]

clips = []
for i, (bg, audio, estilo, textos) in enumerate(cenas):
    print(f"  🎨 Cena {i+1}/9")
    frame = f"reels3_temp/frame_{i:02d}.jpg"
    clip = f"reels3_temp/clip_{i:02d}.mp4"
    criar_frame(bg, estilo, textos, frame)
    dur = get_dur(audio)
    subprocess.run([
        'ffmpeg','-y','-loop','1','-i',frame,'-i',audio,
        '-filter_complex',
        f'[0:v]scale=8000:-1,zoompan=z=\'min(zoom+0.0007,1.08)\':d={int(dur*25)}:x=\'iw/2-(iw/zoom/2)\':y=\'ih/2-(ih/zoom/2)\':s=1080x1920,fps=25[v]',
        '-map','[v]','-map','1:a',
        '-c:v','libx264','-preset','slow','-crf','18',
        '-c:a','aac','-b:a','192k','-pix_fmt','yuv420p','-t',str(dur),clip
    ], capture_output=True)
    clips.append(clip)

with open("reels3_temp/lista.txt","w") as f:
    for c in clips:
        f.write(f"file '{os.path.abspath(c)}'\\n")

subprocess.run([
    'ffmpeg','-y','-f','concat','-safe','0','-i','reels3_temp/lista.txt',
    '-c','copy','reels3_temp/video_base.mp4'
], capture_output=True)

subprocess.run([
    'ffmpeg','-y',
    '-i','reels3_temp/video_base.mp4',
    '-i','reels_musica_bg.mp3',
    '-filter_complex',
    '[1:a]volume=0.12[m];[0:a]volume=1.0[v];[v][m]amix=inputs=2:duration=first[a]',
    '-map','0:v','-map','[a]',
    '-c:v','copy','-c:a','aac','-b:a','256k',
    '-shortest','reels_PERFEITO_emotionai.mp4'
], capture_output=True)

size = os.path.getsize('reels_PERFEITO_emotionai.mp4')/(1024*1024)
print(f"\\n🎉 PRONTO: reels_PERFEITO_emotionai.mp4")
print(f"📦 {size:.1f} MB")
