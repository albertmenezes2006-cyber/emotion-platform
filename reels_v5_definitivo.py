from PIL import Image, ImageDraw, ImageFont, ImageEnhance
import subprocess, os

print("🎬 Criando Reels V5 — DEFINITIVO...")
os.makedirs("reels5_temp", exist_ok=True)

W, H = 1080, 1920

def fnt(size, bold=False):
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

def texto(draw, txt, y, fonte, cor, max_w=940):
    palavras = txt.split()
    linhas, linha = [], ""
    for p in palavras:
        teste = linha + " " + p if linha else p
        bb = draw.textbbox((0,0), teste, font=fonte)
        if bb[2]-bb[0] > max_w and linha:
            linhas.append(linha)
            linha = p
        else:
            linha = teste
    if linha:
        linhas.append(linha)

    y_pos = y
    for l in linhas:
        bb = draw.textbbox((0,0), l, font=fonte)
        h = bb[3]-bb[1]
        tw = bb[2]-bb[0]
        x = (W-tw)//2
        # Sombra forte
        for dx,dy in [(4,4),(-4,4),(4,-4),(-4,-4),(0,5),(5,0),(-5,0)]:
            draw.text((x+dx, y_pos+dy), l, font=fonte, fill=(0,0,0))
        draw.text((x, y_pos), l, font=fonte, fill=cor)
        y_pos += h + 25
    return y_pos

def frame(bg_path, estilo, t1, t2, t3, output):
    bg = Image.open(bg_path).resize((W,H), Image.LANCZOS)
    bg = ImageEnhance.Brightness(bg).enhance(0.40)
    bg = ImageEnhance.Contrast(bg).enhance(1.3)
    bg = bg.convert("RGBA")

    ov = Image.new("RGBA",(W,H),(0,0,0,0))
    d = ImageDraw.Draw(ov)

    if estilo == "gancho":
        d.rectangle([(0,0),(W,H//2)], fill=(30,0,50,160))
        d.rectangle([(0,H//2),(W,H)], fill=(0,0,0,180))
    elif estilo == "dor":
        d.rectangle([(0,0),(W,H)], fill=(0,0,0,170))
    elif estilo == "virada":
        d.rectangle([(0,0),(W,H)], fill=(50,10,90,170))
    elif estilo == "reveal":
        d.rectangle([(0,0),(W,H)], fill=(5,0,20,160))
    elif estilo == "cta":
        d.rectangle([(0,0),(W,H)], fill=(40,0,70,175))

    bg = Image.alpha_composite(bg, ov)
    draw = ImageDraw.Draw(bg)

    # Linha topo
    draw.rectangle([(0,0),(W,10)], fill=(167,139,250))
    draw.rectangle([(0,10),(W,16)], fill=(250,204,21))

    # Caixa central transparente para textos
    draw.rounded_rectangle(
        [(60, H//2-320),(W-60, H//2+320)],
        radius=30,
        fill=(0,0,0,80)
    )

    # TEXTO 1 — Principal (grande, impacto)
    if t1:
        f1 = fnt(t1.get("size",100), True)
        y_fim = texto(draw, t1["texto"], H//2-280, f1, t1.get("cor",(255,255,255)))

    # Divisor
    draw.rectangle([(W//4, H//2-10),(W*3//4, H//2-3)], fill=(167,139,250))

    # TEXTO 2 — Secundario (médio, claro)
    if t2:
        f2 = fnt(t2.get("size",58), t2.get("bold",False))
        y_fim2 = texto(draw, t2["texto"], H//2+20, f2, t2.get("cor",(220,220,255)), max_w=880)

    # TEXTO 3 — Terciário (pequeno, discreto)
    if t3:
        f3 = fnt(t3.get("size",46), False)
        texto(draw, t3["texto"], H//2+200, f3, t3.get("cor",(134,239,172)), max_w=800)

    # Badge
    draw.rectangle([(0,H-140),(W,H)], fill=(10,0,25,245))
    draw.rectangle([(0,H-142),(W,H-134)], fill=(167,139,250))
    texto(draw, "@emotionai_br", H-118, fnt(40,True), (250,204,21))
    texto(draw, "Link na bio — Gratis para comecar!", H-68, fnt(30,False), (134,239,172))

    bg.convert("RGB").save(output, quality=98)

cenas = [
    ("reels2_frames/home_top.png","reels2_audio/gancho.mp3","gancho",
     {"texto":"⚡ PARA TUDO!","size":140,"cor":(250,204,21)},
     {"texto":"Voce ainda cuida da sua saude mental do jeito antigo?","size":58,"cor":(255,255,255)},
     {"texto":"Continue vendo 👇","size":46,"cor":(167,139,250)}),

    ("reels2_frames/home_meio.png","reels2_audio/dor1.mp3","dor",
     {"texto":"Ansiedade. Insonia.","size":110,"cor":(252,165,165)},
     {"texto":"Pensamentos que nao param. Sensacao de que ninguem entende.","size":56,"cor":(220,220,255)},
     None),

    ("reels2_frames/home_baixo.png","reels2_audio/dor2.mp3","dor",
     {"texto":"Quando voce resolve buscar ajuda...","size":78,"cor":(255,255,255)},
     {"texto":"nao sabe por onde comecar.","size":80,"cor":(252,165,165),"bold":True},
     None),

    ("reels2_frames/home_top.png","reels2_audio/virada.mp3","virada",
     {"texto":"🤯 E SE EU TE DISSESSE...","size":92,"cor":(250,204,21)},
     {"texto":"Existe uma plataforma brasileira GRATUITA com Inteligencia Artificial feita para isso.","size":56,"cor":(255,255,255)},
     {"texto":"👇 Continua assistindo","size":46,"cor":(167,139,250)}),

    ("reels2_frames/chat.png","reels2_audio/reveal1.mp3","reveal",
     {"texto":"💬 CHAT COM IA","size":115,"cor":(167,139,250)},
     {"texto":"Empatia real. 24 horas por dia. Sem julgamento. Sem fila.","size":56,"cor":(255,255,255)},
     {"texto":"✅ Sempre disponivel","size":46,"cor":(134,239,172)}),

    ("reels2_frames/avaliacao.png","reels2_audio/reveal2.mp3","reveal",
     {"texto":"PHQ-9 e GAD-7","size":118,"cor":(250,204,21)},
     {"texto":"As mesmas avaliacoes que psicologos usam no consultorio.","size":56,"cor":(255,255,255)},
     {"texto":"✅ Gratis. Em 2 minutos.","size":48,"cor":(134,239,172)}),

    ("reels2_frames/dashboard.png","reels2_audio/reveal3.mp3","reveal",
     {"texto":"📈 Sua Evolucao","size":112,"cor":(167,139,250)},
     {"texto":"Acompanhe seu progresso emocional dia apos dia.","size":58,"cor":(255,255,255)},
     {"texto":"Isso muda tudo. 🔥","size":50,"cor":(250,204,21)}),

    ("reels2_frames/mindfulness.png","reels2_audio/reveal4.mp3","reveal",
     {"texto":"🧘 Mindfulness","size":118,"cor":(167,139,250)},
     {"texto":"Tecnicas com evidencias cientificas no seu celular a qualquer hora.","size":56,"cor":(255,255,255)},
     {"texto":"🌙 Disponivel agora","size":46,"cor":(250,204,21)}),

    ("reels2_frames/home_top.png","reels2_audio/cta.mp3","cta",
     {"texto":"🚀 E GRATUITO","size":130,"cor":(250,204,21)},
     {"texto":"Porque saude mental nao e privilegio de poucos.","size":60,"cor":(255,255,255)},
     {"texto":"🔗 Acesse agora. Link na bio!","size":52,"cor":(134,239,172)}),
]

clips = []
for i,(bg,audio,estilo,t1,t2,t3) in enumerate(cenas):
    print(f"  🎨 Cena {i+1}/9 — {estilo}")
    fr = f"reels5_temp/frame_{i:02d}.jpg"
    cl = f"reels5_temp/clip_{i:02d}.mp4"
    frame(bg, estilo, t1, t2, t3, fr)
    dur = get_dur(audio)

    # SEM zoompan — evita distorcao
    # Usar fade simples e escala correta
    subprocess.run([
        'ffmpeg','-y',
        '-loop','1','-i',fr,
        '-i',audio,
        '-filter_complex',
        f'[0:v]scale=1080:1920:force_original_aspect_ratio=disable,fps=25[v]',
        '-map','[v]','-map','1:a',
        '-c:v','libx264','-preset','fast','-crf','16',
        '-c:a','aac','-b:a','192k',
        '-pix_fmt','yuv420p','-t',str(dur), cl
    ], capture_output=True)

    clips.append(cl)
    print(f"    ✅ {dur:.1f}s — sem distorcao")

# Concatenar
lista = "reels5_temp/lista.txt"
with open(lista,'w') as f:
    for c in clips:
        f.write(f"file '{os.path.abspath(c)}'\n")

print("\n🎬 Concatenando...")
subprocess.run([
    'ffmpeg','-y','-f','concat','-safe','0',
    '-i',lista,'-c','copy','reels5_temp/base.mp4'
], capture_output=True)

print("🎵 Adicionando musica...")
subprocess.run([
    'ffmpeg','-y',
    '-i','reels5_temp/base.mp4',
    '-i','reels_musica_bg.mp3',
    '-filter_complex',
    '[1:a]volume=0.12[m];[0:a]volume=1.0[v];[v][m]amix=inputs=2:duration=first[a]',
    '-map','0:v','-map','[a]',
    '-c:v','copy','-c:a','aac','-b:a','256k',
    '-shortest','reels_V5_DEFINITIVO.mp4'
], capture_output=True)

size = os.path.getsize('reels_V5_DEFINITIVO.mp4')/(1024*1024)
print(f"\n🎉 REELS V5 DEFINITIVO PRONTO!")
print(f"📁 reels_V5_DEFINITIVO.mp4")
print(f"📦 {size:.1f} MB")
print(f"✅ Sem distorcao — escala direta 1080x1920")
print(f"✅ Caixa central para textos")
print(f"✅ Max 3 elementos por cena")
print(f"✅ Hierarquia visual clara")
print(f"✅ Sombra forte nos textos")
