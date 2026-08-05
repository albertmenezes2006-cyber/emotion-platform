import subprocess, os

print("🎬 Criando Reels V9 — FFmpeg puro, fundo escuro sólido...")
os.makedirs("reels9_temp", exist_ok=True)

FONT_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_R = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

def get_dur(audio):
    r = subprocess.run(
        ['ffprobe','-v','quiet','-show_entries','format=duration',
         '-of','default=noprint_wrappers=1:nokey=1', audio],
        capture_output=True, text=True)
    return float(r.stdout.strip())

def make_cena(idx, audio, cor_fundo, textos, output):
    dur = get_dur(audio)

    # Montar filtros drawtext
    dt = []
    for t in textos:
        txt = t['txt'].replace("'", "\\'").replace(":", "\\:")
        dt.append(
            f"drawtext=fontfile={t['font']}:"
            f"text='{txt}':"
            f"fontsize={t['size']}:"
            f"fontcolor={t['cor']}:"
            f"x=(w-text_w)/2:"
            f"y={t['y']}:"
            f"shadowcolor=black:shadowx=3:shadowy=3:"
            f"box=1:boxcolor=black@0.5:boxborderw=12"
        )

    filtro = f"[0:v]scale=1080:1920," + ",".join(dt) + "[v]"

    subprocess.run([
        'ffmpeg', '-y',
        '-f', 'lavfi',
        '-i', f'color=c={cor_fundo}:size=1080x1920:rate=25',
        '-i', audio,
        '-filter_complex', filtro,
        '-map', '[v]', '-map', '1:a',
        '-c:v', 'libx264', '-preset', 'fast', '-crf', '18',
        '-c:a', 'aac', '-b:a', '192k',
        '-pix_fmt', 'yuv420p', '-t', str(dur),
        output
    ], capture_output=True)
    return dur

# CENAS com fundo sólido escuro
cenas = [
    # idx, audio, cor_fundo, textos
    (0, "reels2_audio/gancho.mp3", "0x1a0030", [
        {"txt": "PARA.", "font": FONT_B, "size": 160, "cor": "yellow", "y": 500},
        {"txt": "Voce cuida da sua", "font": FONT_B, "size": 80, "cor": "white", "y": 700},
        {"txt": "saude mental do jeito certo?", "font": FONT_B, "size": 80, "cor": "white", "y": 810},
        {"txt": "Continue assistindo... 👇", "font": FONT_R, "size": 55, "cor": "0xc4b5fd", "y": 1100},
    ]),
    (1, "reels2_audio/dor1.mp3", "0x0a0010", [
        {"txt": "Ansiedade.", "font": FONT_B, "size": 110, "cor": "0xfca5a5", "y": 500},
        {"txt": "Insonia.", "font": FONT_B, "size": 110, "cor": "0xfca5a5", "y": 640},
        {"txt": "Pensamentos que nao param.", "font": FONT_R, "size": 65, "cor": "white", "y": 900},
        {"txt": "Ninguem te entende.", "font": FONT_R, "size": 65, "cor": "0xc4b5fd", "y": 990},
    ]),
    (2, "reels2_audio/dor2.mp3", "0x0a0010", [
        {"txt": "Quando voce resolve", "font": FONT_R, "size": 75, "cor": "white", "y": 600},
        {"txt": "buscar ajuda...", "font": FONT_R, "size": 75, "cor": "white", "y": 700},
        {"txt": "nao sabe por onde comecar.", "font": FONT_B, "size": 85, "cor": "0xfca5a5", "y": 950},
    ]),
    (3, "reels2_audio/virada.mp3", "0x200050", [
        {"txt": "E SE EU TE DISSESSE...", "font": FONT_B, "size": 88, "cor": "yellow", "y": 500},
        {"txt": "que existe uma plataforma", "font": FONT_R, "size": 68, "cor": "white", "y": 700},
        {"txt": "brasileira e GRATUITA", "font": FONT_B, "size": 80, "cor": "0xa78bfa", "y": 800},
        {"txt": "com Inteligencia Artificial?", "font": FONT_R, "size": 68, "cor": "white", "y": 950},
    ]),
    (4, "reels2_audio/reveal1.mp3", "0x050015", [
        {"txt": "CHAT COM IA", "font": FONT_B, "size": 110, "cor": "0xa78bfa", "y": 500},
        {"txt": "Empatia real. 24h por dia.", "font": FONT_B, "size": 72, "cor": "yellow", "y": 680},
        {"txt": "Sem julgamento.", "font": FONT_R, "size": 65, "cor": "white", "y": 900},
        {"txt": "Sem fila de espera.", "font": FONT_R, "size": 65, "cor": "white", "y": 990},
    ]),
    (5, "reels2_audio/reveal2.mp3", "0x050015", [
        {"txt": "PHQ-9 e GAD-7", "font": FONT_B, "size": 110, "cor": "yellow", "y": 500},
        {"txt": "Avaliacoes clinicas reais.", "font": FONT_R, "size": 68, "cor": "white", "y": 680},
        {"txt": "As mesmas que psicologos usam.", "font": FONT_R, "size": 60, "cor": "0xc4b5fd", "y": 780},
        {"txt": "GRATIS. Em 2 minutos.", "font": FONT_B, "size": 72, "cor": "0x86efac", "y": 1000},
    ]),
    (6, "reels2_audio/reveal3.mp3", "0x050015", [
        {"txt": "DASHBOARD EMOCIONAL", "font": FONT_B, "size": 90, "cor": "0xa78bfa", "y": 500},
        {"txt": "Acompanhe sua evolucao", "font": FONT_R, "size": 68, "cor": "white", "y": 680},
        {"txt": "dia apos dia.", "font": FONT_B, "size": 80, "cor": "yellow", "y": 800},
        {"txt": "Isso muda tudo.", "font": FONT_B, "size": 72, "cor": "0xfca5a5", "y": 1000},
    ]),
    (7, "reels2_audio/reveal4.mp3", "0x050015", [
        {"txt": "MINDFULNESS", "font": FONT_B, "size": 110, "cor": "0xa78bfa", "y": 500},
        {"txt": "Tecnicas com evidencias", "font": FONT_R, "size": 68, "cor": "white", "y": 700},
        {"txt": "cientificas.", "font": FONT_R, "size": 68, "cor": "white", "y": 800},
        {"txt": "No seu celular. Agora.", "font": FONT_B, "size": 72, "cor": "yellow", "y": 1000},
    ]),
    (8, "reels2_audio/cta.mp3", "0x1a0040", [
        {"txt": "E GRATUITO", "font": FONT_B, "size": 130, "cor": "yellow", "y": 450},
        {"txt": "para comecar.", "font": FONT_R, "size": 80, "cor": "white", "y": 620},
        {"txt": "Saude mental nao e privilegio.", "font": FONT_R, "size": 62, "cor": "0xfca5a5", "y": 850},
        {"txt": "Link na bio. Acesse agora!", "font": FONT_B, "size": 72, "cor": "0x86efac", "y": 1050},
    ]),
]

clips = []
for idx, audio, fundo, textos in cenas:
    print(f"  🎨 Cena {idx+1}/9...")
    cl = f"reels9_temp/clip_{idx:02d}.mp4"
    dur = make_cena(idx, audio, fundo, textos, cl)
    clips.append(cl)
    print(f"    ✅ {dur:.1f}s")

# Concatenar
lista = "reels9_temp/lista.txt"
with open(lista,'w') as f:
    for c in clips:
        f.write(f"file '{os.path.abspath(c)}'\n")

print("\n🎬 Concatenando...")
subprocess.run([
    'ffmpeg','-y','-f','concat','-safe','0',
    '-i', lista,'-c','copy','reels9_temp/base.mp4'
], capture_output=True)

print("🎵 Adicionando musica...")
subprocess.run([
    'ffmpeg','-y',
    '-i','reels9_temp/base.mp4',
    '-i','reels_musica_bg.mp3',
    '-filter_complex',
    '[1:a]volume=0.15[m];[0:a]volume=1.0[v];[v][m]amix=inputs=2:duration=first[a]',
    '-map','0:v','-map','[a]',
    '-c:v','copy','-c:a','aac','-b:a','256k',
    '-shortest','reels_V9_DEFINITIVO.mp4'
], capture_output=True)

size = os.path.getsize('reels_V9_DEFINITIVO.mp4')/(1024*1024)
print(f"\n🎉 REELS V9 PRONTO!")
print(f"📁 reels_V9_DEFINITIVO.mp4 — {size:.1f} MB")
print(f"✅ Fundo solido — sem conflito com textos do site")
print(f"✅ FFmpeg puro — sem PIL")
print(f"✅ box=1 — fundo atras de cada texto")
