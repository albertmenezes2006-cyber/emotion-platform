"""
Plugin: Otimizacao de Imagens
Categoria: performance
"""
VERSAO = "1.0"
NOME = "image_optimization"
DESCRICAO = "WebP, AVIF, lazy loading, responsive images e compressao"
CATEGORIA = "performance"


FORMATOS_MODERNOS = ["webp", "avif"]
QUALIDADE_PADRAO = {"webp": 85, "avif": 80, "jpeg": 90, "png": 95}
LARGURAS_RESPONSIVAS = [320, 480, 640, 768, 1024, 1280, 1920]

def converter_para_webp(imagem_bytes: bytes, qualidade: int = 85) -> bytes:
    try:
        from PIL import Image
        import io
        img = Image.open(io.BytesIO(imagem_bytes))
        if img.mode in ("RGBA", "LA"):
            background = Image.new("RGB", img.size, (255,255,255))
            background.paste(img, mask=img.split()[-1])
            img = background
        elif img.mode != "RGB":
            img = img.convert("RGB")
        saida = io.BytesIO()
        img.save(saida, format="WEBP", quality=qualidade, optimize=True)
        return saida.getvalue()
    except ImportError:
        return imagem_bytes
    except Exception:
        return imagem_bytes

def redimensionar_imagem(imagem_bytes: bytes, largura: int, altura: int = None) -> bytes:
    try:
        from PIL import Image
        import io
        img = Image.open(io.BytesIO(imagem_bytes))
        if altura:
            img = img.resize((largura, altura), Image.LANCZOS)
        else:
            ratio = largura / img.width
            nova_altura = int(img.height * ratio)
            img = img.resize((largura, nova_altura), Image.LANCZOS)
        saida = io.BytesIO()
        fmt = img.format or "JPEG"
        img.save(saida, format=fmt, quality=90, optimize=True)
        return saida.getvalue()
    except Exception:
        return imagem_bytes

def gerar_srcset_responsivo(url_base: str, larguras: list = None) -> str:
    larguras = larguras or [480, 768, 1024, 1280]
    partes = []
    for l in larguras:
        if "cloudinary.com" in url_base:
            partes_url = url_base.split("/upload/")
            if len(partes_url) == 2:
                url = f"{partes_url[0]}/upload/w_{l},f_webp,q_85/{partes_url[1]}"
            else:
                url = url_base
        else:
            url = url_base
        partes.append(f"{url} {l}w")
    return ", ".join(partes)

def gerar_img_tag_otimizada(url: str, alt: str, largura: int = 800, lazy: bool = True) -> str:
    srcset = gerar_srcset_responsivo(url)
    loading = 'loading="lazy"' if lazy else 'loading="eager"'
    return (f'<img src="{url}" srcset="{srcset}" sizes="(max-width: 768px) 100vw, {largura}px" '
            f'alt="{alt}" width="{largura}" {loading} decoding="async">')

def gerar_placeholder_blur(largura: int = 40, altura: int = 30) -> str:
    return "data:image/svg+xml;base64,PHN2ZyB3aWR0aD0ie2xhcmd1cmF9IiBoZWlnaHQ9IntffSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cmVjdCB3aWR0aD0iMTAwJSIgaGVpZ2h0PSIxMDAlIiBmaWxsPSIjMWExYTJlIi8+PC9zdmc+"

def analisar_imagem(imagem_bytes: bytes) -> dict:
    try:
        from PIL import Image
        import io
        img = Image.open(io.BytesIO(imagem_bytes))
        tamanho_kb = len(imagem_bytes) / 1024
        return {
            "largura": img.width,
            "altura": img.height,
            "formato": img.format,
            "modo": img.mode,
            "tamanho_kb": round(tamanho_kb, 1),
            "otimizacao_sugerida": "webp" if img.format not in ("WEBP","AVIF") else "ja_otimizado",
            "reducao_estimada_pct": 30 if img.format == "PNG" else 20 if img.format in ("JPEG","JPG") else 0
        }
    except Exception as e:
        return {"erro": str(e)}

def stats_image_opt() -> dict:
    return {
        "formatos_suportados": FORMATOS_MODERNOS + ["jpeg","png","gif"],
        "larguras_responsivas": LARGURAS_RESPONSIVAS,
        "pil_disponivel": bool(__import__("importlib").util.find_spec("PIL")),
        "plugin": "image_optimization v1.0"
    }
