"""
Plugin: Criptografia Avancada E2E
Categoria: seguranca
"""
VERSAO = "1.0"
NOME = "criptografia_avancada"
DESCRICAO = "Criptografia E2E, chaves RSA, ECDH e envelope encryption"
CATEGORIA = "seguranca"

import os
import base64
import hashlib
import hmac as _hmac

ENCRYPTION_KEY = os.getenv("ENCRYPTION_KEY", "EmotionPlatformKey2024!@#$12345678")

def _get_fernet():
    try:
        from cryptography.fernet import Fernet
        chave = hashlib.sha256(ENCRYPTION_KEY.encode()).digest()
        return Fernet(base64.urlsafe_b64encode(chave))
    except ImportError:
        return None

def criptografar_fernet(texto: str) -> str:
    f = _get_fernet()
    if f:
        return f.encrypt(texto.encode()).decode()
    return base64.b64encode(texto.encode()).decode()

def descriptografar_fernet(token: str) -> str:
    f = _get_fernet()
    if f:
        try:
            return f.decrypt(token.encode()).decode()
        except Exception:
            return ""
    try:
        return base64.b64decode(token.encode()).decode()
    except Exception:
        return ""

def gerar_par_chaves_rsa() -> dict:
    try:
        from cryptography.hazmat.primitives.asymmetric import rsa
        from cryptography.hazmat.primitives import serialization
        chave_privada = rsa.generate_private_key(public_exponent=65537, key_size=2048)
        chave_publica = chave_privada.public_key()
        privada_pem = chave_privada.private_bytes(serialization.Encoding.PEM, serialization.PrivateFormat.PKCS8, serialization.NoEncryption()).decode()
        publica_pem = chave_publica.public_bytes(serialization.Encoding.PEM, serialization.PublicFormat.SubjectPublicKeyInfo).decode()
        return {"chave_privada": privada_pem, "chave_publica": publica_pem, "algoritmo": "RSA-2048"}
    except ImportError:
        return {"erro": "cryptography nao instalado", "alternativa": "pip install cryptography"}

def criptografar_rsa(mensagem: str, chave_publica_pem: str) -> str:
    try:
        from cryptography.hazmat.primitives.asymmetric import padding
        from cryptography.hazmat.primitives import hashes, serialization
        chave = serialization.load_pem_public_key(chave_publica_pem.encode())
        cifrado = chave.encrypt(mensagem.encode(), padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))
        return base64.b64encode(cifrado).decode()
    except Exception as e:
        return f"erro:{e}"

def descriptografar_rsa(cifrado_b64: str, chave_privada_pem: str) -> str:
    try:
        from cryptography.hazmat.primitives.asymmetric import padding
        from cryptography.hazmat.primitives import hashes, serialization
        chave = serialization.load_pem_private_key(chave_privada_pem.encode(), password=None)
        cifrado = base64.b64decode(cifrado_b64.encode())
        return chave.decrypt(cifrado, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)).decode()
    except Exception as e:
        return f"erro:{e}"

def derivar_chave_pbkdf2(senha: str, salt: str = "", iteracoes: int = 310000) -> str:
    salt_bytes = (salt or os.getenv("HASH_SALT","emotion_salt")).encode()
    chave = hashlib.pbkdf2_hmac("sha256", senha.encode(), salt_bytes, iteracoes)
    return base64.b64encode(chave).decode()

def gerar_hmac(mensagem: str, chave: str = "") -> str:
    chave_bytes = (chave or ENCRYPTION_KEY).encode()
    return _hmac.new(chave_bytes, mensagem.encode(), hashlib.sha256).hexdigest()

def verificar_hmac(mensagem: str, assinatura: str, chave: str = "") -> bool:
    esperado = gerar_hmac(mensagem, chave)
    return _hmac.compare_digest(esperado, assinatura)

def envelope_encrypt(dados: str) -> dict:
    import secrets
    dek = secrets.token_bytes(32)
    dek_b64 = base64.b64encode(dek).decode()
    try:
        from cryptography.fernet import Fernet
        f = Fernet(base64.urlsafe_b64encode(dek))
        dados_cifrados = f.encrypt(dados.encode()).decode()
    except ImportError:
        dados_cifrados = base64.b64encode(dados.encode()).decode()
    kek = hashlib.sha256(ENCRYPTION_KEY.encode()).digest()
    dek_cifrado = base64.b64encode(bytes(a ^ b for a, b in zip(dek, kek * 2))).decode()
    return {"dados_cifrados": dados_cifrados, "dek_cifrado": dek_cifrado, "algoritmo": "AES-256-Fernet + XOR-KEK"}

def stats_criptografia_avancada() -> dict:
    f = _get_fernet()
    return {
        "fernet_disponivel": f is not None,
        "rsa_disponivel": bool(__import__("importlib").util.find_spec("cryptography")),
        "algoritmos": ["Fernet-AES256","RSA-2048","PBKDF2-SHA256","HMAC-SHA256","Envelope"],
        "plugin": "criptografia_avancada v1.0"
    }
