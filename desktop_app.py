"""
NeuroLectura Arcade 11 - Lanzador y Servidor Local de Escritorio
Permite ejecutar los 30 juegos como aplicación de escritorio nativa
y guarda automáticamente cada sesión en archivos locales (JSON y CSV).
"""

import os
import sys
import json
import csv
import socket
import webbrowser
import subprocess
from pathlib import Path
from http.server import HTTPServer, SimpleHTTPRequestHandler

BASE_DIR = Path(__file__).parent.resolve()
REGISTROS_DIR = BASE_DIR / "registros"
REGISTROS_DIR.mkdir(exist_ok=True)

JSON_LOG_FILE = REGISTROS_DIR / "registro_rendimiento.json"
CSV_LOG_FILE = REGISTROS_DIR / "registro_rendimiento.csv"

def find_free_port(start_port=8765):
    """Encuentra un puerto libre para el servidor."""
    for port in range(start_port, start_port + 50):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            if s.connect_ex(('localhost', port)) != 0:
                return port
    return 8765

def save_log_entry(entry):
    """Guarda la entrada de telemetría en disco tanto en JSON como en CSV."""
    # 1. Guardar en JSON acumulativo
    logs = []
    if JSON_LOG_FILE.exists():
        try:
            with open(JSON_LOG_FILE, 'r', encoding='utf-8') as f:
                logs = json.load(f)
        except Exception:
            logs = []
    
    logs.insert(0, entry)
    with open(JSON_LOG_FILE, 'w', encoding='utf-8') as f:
        json.dump(logs, f, ensure_ascii=False, indent=2)

    # 2. Guardar en CSV para abrir directamente en Excel
    file_exists = CSV_LOG_FILE.exists()
    headers = [
        'ID_Sesion', 'Fecha_Hora', 'Juego_ID', 'Juego', 'Pilar_Cognitivo',
        'Aciertos', 'Intentos', 'Precision_Porcentaje', 'Duracion_Segundos',
        'Puntaje', 'Errores_Detectados'
    ]
    
    with open(CSV_LOG_FILE, 'a', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(headers)
        writer.writerow([
            entry.get('id', ''),
            entry.get('formattedDate') or entry.get('timestamp', ''),
            entry.get('gameId', ''),
            entry.get('gameName', ''),
            entry.get('pillarName', ''),
            entry.get('correctAnswers', 0),
            entry.get('totalAttempts', 0),
            entry.get('accuracy', 0),
            entry.get('durationSeconds', 0),
            entry.get('score', 0),
            "; ".join(entry.get('specificErrors', []))
        ])
    print(f"✅ [Registro Guardado] Juego #{entry.get('gameId')} - {entry.get('gameName')} | Precisión: {entry.get('accuracy')}%")

class ArcadeRequestHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(BASE_DIR), **kwargs)

    def do_POST(self):
        if self.path == '/api/save_log':
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length)
            try:
                data = json.loads(post_data.decode('utf-8'))
                save_log_entry(data)
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'status': 'ok'}).encode('utf-8'))
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'status': 'error', 'message': str(e)}).encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()

    def log_message(self, format, *args):
        # Silenciar logs http ruidosos
        pass

def launch_desktop_window(url):
    """
    Intenta abrir Microsoft Edge en modo aplicación (sin barras de navegación,
    luciendo 100% como una aplicación nativa de escritorio de Windows).
    Si no está Edge, abre el navegador predeterminado.
    """
    edge_paths = [
        os.path.expandvars(r"%ProgramFiles(x86)%\Microsoft\Edge\Application\msedge.exe"),
        os.path.expandvars(r"%ProgramFiles%\Microsoft\Edge\Application\msedge.exe"),
        os.path.expandvars(r"%LocalAppData%\Microsoft\Edge\Application\msedge.exe")
    ]
    
    for path in edge_paths:
        if os.path.exists(path):
            try:
                subprocess.Popen([path, f"--app={url}", "--window-size=1280,820", "--start-maximized"])
                return
            except Exception:
                pass

    # Si no se encuentra Edge en esas rutas, abrir en navegador normal
    webbrowser.open(url)

def main():
    port = find_free_port()
    url = f"http://localhost:{port}/index.html"
    
    print("=" * 65)
    print("🚀  INICIANDO NEUROLECTURA ARCADE 11 (VERSIÓN ESCRITORIO)")
    print("=" * 65)
    print(f"📍 Servidor local activo en: {url}")
    print(f"📁 Los registros se guardan en: {REGISTROS_DIR}")
    print("💡 Presiona Ctrl+C en cualquier momento para cerrar.")
    print("=" * 65)

    server = HTTPServer(('127.0.0.1', port), ArcadeRequestHandler)
    launch_desktop_window(url)

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n👋 Cerrando NeuroLectura Arcade. ¡Buen entrenamiento lector!")
        server.server_close()

if __name__ == '__main__':
    main()
