#!/usr/bin/env python3
import ssl
import socket
from datetime import datetime

HOST = "emotion-platform-albert.onrender.com"

print("=== SSL/TLS ===")
print(f"Host: {HOST}")
print()

try:
    ctx = ssl.create_default_context()
    with socket.create_connection((HOST, 443), timeout=10) as sock:
        with ctx.wrap_socket(sock, server_hostname=HOST) as ssock:
            cert = ssock.getpeercert()
            versao = ssock.version()
            cipher = ssock.cipher()

            print("  OK  Certificado SSL valido")
            print(f"  OK  Versao TLS: {versao}")

            if cipher:
                print(f"  OK  Cipher: {cipher[0]}")

            # Validade
            expiry = cert.get("notAfter", "")
            if expiry:
                exp_date = datetime.strptime(expiry, "%b %d %H:%M:%S %Y %Z")
                dias = (exp_date - datetime.utcnow()).days
                if dias > 30:
                    print(f"  OK  Certificado valido por {dias} dias")
                elif dias > 0:
                    print(f"  WARN Certificado expira em {dias} dias!")
                else:
                    print("  ERR  Certificado EXPIRADO!")

            # Emissor
            issuer_raw = cert.get("issuer", ())
            issuer = {}
            for item in issuer_raw:
                if item:
                    k, v = item[0]
                    issuer[k] = v
            org = issuer.get("organizationName", "?")
            print(f"  OK  Emissor: {org}")

            # Versao TLS
            if "TLSv1.3" in versao:
                print("  OK  TLS 1.3 (maxima seguranca)")
            elif "TLSv1.2" in versao:
                print("  OK  TLS 1.2 (seguro)")
            else:
                print(f"  WARN {versao} (considere atualizar)")

except ssl.SSLCertVerificationError as exc:
    print(f"  ERR Certificado invalido: {exc}")
except Exception as exc:
    print(f"  ERR Erro SSL: {exc}")

print()
print(f"Analise completa: https://www.ssllabs.com/ssltest/analyze.html?d={HOST}")
