from http.server import HTTPServer, SimpleHTTPRequestHandler
import os

class CustomHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        
        # Personalizar con el nombre del estudiante / grupo
        estudiante = os.getenv("ESTUDIANTE_NOMBRE", "Cristian Salcedo")
        
        html_content = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Servidor Web DMZ - {estudiante}</title>
    <style>
        body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin: 40px; background-color: #0f172a; color: #f8fafc; display: flex; justify-content: center; align-items: center; min-height: 80vh; }}
        .container {{ background: #1e293b; padding: 35px; border-radius: 12px; box-shadow: 0 10px 25px rgba(0,0,0,0.5); max-width: 650px; width: 100%; border: 1px solid #334155; }}
        h1 {{ color: #38bdf8; margin-top: 0; font-size: 1.8rem; }}
        h2 {{ color: #f1f5f9; font-size: 1.3rem; margin-top: 10px; border-bottom: 2px solid #334155; padding-bottom: 12px; }}
        .status {{ color: #4ade80; font-weight: bold; background: rgba(74, 222, 128, 0.15); padding: 4px 10px; border-radius: 6px; font-size: 0.9rem; }}
        .info-box {{ background: #0f172a; border-left: 4px solid #38bdf8; padding: 15px; margin: 20px 0; border-radius: 4px; }}
        p {{ line-height: 1.6; color: #cbd5e1; }}
        .footer {{ font-size: 0.85rem; color: #64748b; margin-top: 20px; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>🛡️ Servidor DMZ Activo</h1>
        <h2>Laboratorio de {estudiante}</h2>
        <p>Estado del servicio: <span class="status">ONLINE / ACTIVO</span></p>
        <div class="info-box">
            <p><strong>Laboratorio de Ciberseguridad:</strong> {estudiante}</p>
            <p>Este nodo actúa como objetivo central para las pruebas de tráfico y análisis de logs en el entorno de Render.</p>
        </div>
        <p class="footer">Nodo de Red Perimetral (DMZ) &bull; Puerto 8080</p>
    </div>
</body>
</html>
"""
        self.wfile.write(html_content.encode("utf-8"))

    def log_message(self, format, *args):
        # Asegurar que todas las peticiones entrantes se muestren inmediatamente en los logs de Render
        print(f"[DMZ LOG] {self.address_string()} - {format % args}", flush=True)

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))
    server_address = ("", port)
    httpd = HTTPServer(server_address, CustomHandler)
    print(f"Servidor DMZ iniciado y escuchando en el puerto {port}...", flush=True)
    httpd.serve_forever()
