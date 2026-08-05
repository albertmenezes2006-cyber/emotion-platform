from PIL import Image, ImageDraw, ImageFont, ImageEnhance
import subprocess, os

print("🎬 Criando Reels V8 — LIMPO E PRECISO...")
os.makedirs("reels8_temp", exist_ok=True)

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

def draw_texto_fixo(draw, txt, y_fixo, size, cor, bold=True, max_chars=25):
    """Desenha texto em posição Y FIXA. Quebra linha apenas se texto muito longo."""
    fonte = fnt(size, bold)
    
    # Quebrar em linhas de max_chars caracteres
    palavras = txt.split()
    linhas = []
    linha = ""
    for p in palavras:
        if len(linha) + len(p) + 1 <= max_chars:
            linha = linha + " " + p if linha else p
        else:
            if linha:
                linhas.append(linha)
            linha = p
    if linha:
        linhas.append(linha)
    
    # Calcular altura total
    bb = draw.textbbox((0,0), "Ag", font=fonte)
    h_linha = bb[3] - bb[1] + 15
    
    # Verificar se cabe na tela
    y_atual = y_fixo
    for l in linhas:
        bb = draw.textbbox((0,0), l, font=fonte)
        tw = bb[2]-bb[0]
        th = bb[3]-bb[1]
        x = (W-tw)//2
        
        # Fundo do texto
        padding = 15
        draw.rounded_rectangle(
            [(x-padding, y_atual-padding),
             (x+tw+padding, y_atual+th+padding)],
            radius=10,
            fill=(0,0,0,160)
        )
        
        # Sombra
        draw.text((x+2, y_atual+2), l, font=fonte, fill=(0,0,0))
        # Texto
        draw.text((x, y_atual), l, font=fonte, fill=cor)
        y_atual += h_linha
    
    return y_atual

def criar_cena(bg_path, estilo, t1_txt, t1_size, t1_cor,
               t2_txt, t2_size, t2_cor, output):
    """Cria frame com exatamente 2 textos em posições fixas."""
    
    # Fundo
    bg = Image.open(bg_path).resize((W,H), Image.LANCZOS)
    bg = ImageEnhance.Brightness(bg).enhance(0.35)
    bg = ImageEnhance.Contrast(bg).enhance(1.3)
    bg = bg.convert("RGBA")
    
    # Overlay simples e limpo
    ov = Image.new("RGBA",(W,H),(0,0,0,0))
    d = ImageDraw.Draw(ov)
    
    cores_overlay = {
        "gancho": (20,0,40,140),
        "dor":    (0,0,0,150),
        "virada": (40,10,80,150),
        "reveal": (0,0,15,150),
        "cta":    (30,0,60,160),
    }
    d.rectangle([(0,0),(W,H)], fill=cores_overlay.get(estilo,(0,0,0,150)))
    bg = Image.alpha_composite(bg, ov)
    draw = ImageDraw.Draw(bg)
    
    # Barras decorativas topo
    draw.rectangle([(0,0),(W,12)], fill=(167,139,250))
    draw.rectangle([(0,12),(W,20)], fill=(250,204,21))
    
    # TEXTO 1 — Posição Y = 650 (terço superior)
    if t1_txt:
        draw_texto_fixo(draw, t1_txt, 650, t1_size, t1_cor, bold=True, max_chars=20)
    
    # Divisor horizontal no meio
    draw.rectangle([(100, 960),(W-100, 968)], fill=(167,139,250,200))
    
    # TEXTO 2 — Posição Y = 1000 (terço inferior)
    if t2_txt:
        draw_texto_fixo(draw, t2_txt, 1000, t2_size, t2_cor, bold=False, max_chars=30)
    
    # Badge inferior fixo
    draw.rectangle([(0,H-130),(W,H)], fill=(8,0,20,250))
    draw.rectangle([(0,H-132),(W,H-124)], fill=(167,139,250))
    
    f_badge = fnt(42, True)
    f_url = fnt(28, False)
    
    bb = draw.textbbox((0,0),"@emotionai_br",font=f_badge)
    x = (W-(bb[2]-bb[0]))//2
    draw.text((x, H-110), "@emotionai_br", font=f_badge, fill=(250,204,21))
    
    bb = draw.textbbox((0,0),"Link na bio — Gratis para comecar",font=f_url)
    x = (W-(bb[2]-bb[0]))//2
    draw.text((x, H-58), "Link na bio — Gratis para comecar", font=f_url, fill=(134,239,172))
    
    bg.convert("RGB").save(output, quality=98)

def make_clip(frame, audio, clip):
    dur = get_dur(audio)
    subprocess.run([
        'ffmpeg','-y','-loop','1','-i',frame,'-i',audio,
        '-filter_complex','[0:v]scale=1080:1920,fps=25[v]',
        '-map','[v]','-map','1:a',
        '-c:v','libx264','-preset','fast','-crf','16',
        '-c:a','aac','-b:a','192k',
        '-pix_fmt','yuv420p','-t',str(dur), clip
    ], capture_output=True)
    return dur

# CENAS — 2 textos por cena, posições fixas
cenas = [
    # (bg, audio, estilo, t1_txt, t1_size, t1_cor, t2_txt, t2_size, t2_cor)
    ("reels2_frames/home_top.png",
     "reels2_audio/gancho.mp3", "gancho",
     "VOCE CUIDA DA SUA SAUDE MENTAL?", 85, (250,204,21),
     "Continue assistindo e descubra algo que vai mudar tudo.", 55, (200,200,255)),

    ("reels2_frames/home_meio.png",
     "reels2_audio/dor1.mp3", "dor",
     "ANSIEDADE. INSONIA.", 95, (252,165,165),
     "Pensamentos que nao param. Ninguem entende.", 58, (220,220,255)),

    ("reels2_frames/home_baixo.png",
     "reels2_audio/dor2.mp3", "dor",
     "BUSCA AJUDA MAS NAO SABE POR ONDE COMECAR?", 78, (255,255,255),
     "Isso vai mudar agora.", 65, (252,165,165)),

    ("reels2_frames/home_top.png",
     "reels2_audio/virada.mp3", "virada",
     "PLATAFORMA BRASILEIRA GRATUITA COM IA", 80, (250,204,21),
     "Feita especialmente para saude mental.", 58, (200,200,255)),

    ("reels2_frames/chat.png",
     "reels2_audio/reveal1.mp3", "reveal",
     "CHAT COM IA 24H", 100, (167,139,250),
     "Empatia real. Sem julgamento. Sem fila.", 62, (255,255,255)),

    ("reels2_frames/avaliacao.png",
     "reels2_audio/reveal2.mp3", "reveal",
     "PHQ-9 E GAD-7 GRATIS", 95, (250,204,21),
     "As mesmas avaliacoes que psicologos usam.", 58, (255,255,255)),

    ("reels2_frames/dashboard.png",
     "reels2_audio/reveal3.mp3", "reveal",
     "ACOMPANHE SUA EVOLUCAO", 88, (167,139,250),
     "Dashboard emocional completo. Dia a dia.", 60, (255,255,255)),

    ("reels2_frames/mindfulness.png",
     "reels2_audio/reveal4.mp3", "reveal",
     "MINDFULNESS E MEDITACAO", 88, (167,139,250),
     "Tecnicas cientificas no seu celular.", 62, (255,255,255)),

    ("reels2_frames/home_top.png",
     "reels2_audio/cta.mp3", "cta",
     "E COMPLETAMENTE GRATUITO", 90, (250,204,21),
     "Acesse agora. Link na bio.", 72, (134,239,172)),
]

clips = []
for i, (bg,audio,estilo,t1,s1,c1,t2,s2,c2) in enumerate(cenas):
    print(f"  🎨 Cena {i+1}/9...")
    fr = f"reels8_temp/frame_{i:02d}.jpg"
    cl = f"reels8_temp/clip_{i:02d}.mp4"
    criar_cena(bg, estilo, t1, s1, c1, t2, s2, c2, fr)
    dur = make_clip(fr, audio, cl)
    clips.append(cl)
    print(f"    ✅ {dur:.1f}s")

# Concatenar
lista = "reels8_temp/lista.txt"
with open(lista,'w') as f:
    for c in clips:
        f.write(f"file '{os.path.abspath(c)}'\n")

print("\n🎬 Concatenando...")
subprocess.run(['ffmpeg','-y','-f','concat','-safe','0',
    '-i',lista,'-c','copy','reels8_temp/base.mp4'], capture_output=True)

print("🎵 Adicionando musica...")
subprocess.run([
    'ffmpeg','-y','-i','reels8_temp/base.mp4','-i','reels_musica_bg.mp3',
    '-filter_complex',
    '[1:a]volume=0.12[m];[0:a]volume=1.0[v];[v][m]amix=inputs=2:duration=first[a]',
    '-map','0:v','-map','[a]','-c:v','copy','-c:a','aac','-b:a','256k',
    '-shortest','reels_V8_CLEAN.mp4'
], capture_output=True)

size = os.path.getsize('reels_V8_CLEAN.mp4')/(1024*1024)
print(f"\n🎉 REELS V8 PRONTO!")
print(f"📁 reels_V8_CLEAN.mp4 — {size:.1f} MB")
print(f"✅ 2 textos por cena — posicoes fixas")
print(f"✅ Fundo solido atras de cada texto")
print(f"✅ Sem sobreposicao possivel")
