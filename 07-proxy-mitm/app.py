from flask import Flask, request, Response
import requests
import os

app = Flask(__name__)

TARGET_DMZ = os.getenv("DMZ_URL", "https://servidor-web-dmz-csalcedo.onrender.com")

@app.route('/', defaults={'path': ''}, methods=['GET', 'POST'])
@app.route('/<path:path>', methods=['GET', 'POST'])
def mitm_proxy(path):
    print(f"\n[MITM INTERCEPTADO] Petición entrante hacia la ruta: /{path}", flush=True)
    print(f"[CABECERAS INTERCEPTADAS] {dict(request.headers)}", flush=True)
    
    url = f"{TARGET_DMZ}/{path}" if path else TARGET_DMZ
    try:
        resp = requests.get(url, timeout=5)
        contenido_original = resp.text
    except Exception as e:
        contenido_original = f"Error al conectar con la DMZ ({url}): {str(e)}"
    
    # Inyección de código en la respuesta HTTP (banner visible para el video + comentario HTML requerido)
    banner_mitm = """
    <div style="background-color: #ef4444; color: white; padding: 16px; margin: 20px auto; max-width: 650px; border-radius: 8px; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; box-shadow: 0 4px 15px rgba(239, 68, 68, 0.4); text-align: center; border: 2px solid #b91c1c;">
        <h3 style="margin: 0 0 6px 0; font-size: 1.2rem;">⚠️ [ALERTA DE SEGURIDAD - ATAQUE MITM]</h3>
        <p style="margin: 0; font-size: 0.95rem;">¡Este tráfico web ha sido <strong>interceptado y modificado en tránsito</strong> por el Proxy Interceptor (Módulo 07)!</p>
    </div>
    """
    
    # Inyección oficial del laboratorio
    contenido_alterado = contenido_original + banner_mitm + "\n\n<!-- [ALERTA MITM] Este contenido fue alterado en tránsito por el Proxy Interceptor -->"
    
    print("[MITM ALERTA] Respuesta modificada e inyectada con éxito.", flush=True)
    return Response(contenido_alterado, status=200, mimetype='text/html')

if __name__ == '__main__':
    port = int(os.getenv("PORT", 8080))
    print(f"Proxy MITM iniciado en puerto {port}, apuntando a DMZ: {TARGET_DMZ}", flush=True)
    app.run(host='0.0.0.0', port=port)
