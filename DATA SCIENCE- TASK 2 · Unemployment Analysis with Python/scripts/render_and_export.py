import http.server
import socketserver
import threading
import subprocess
import time
import base64
import os
import sys
from urllib.parse import urlparse, parse_qs
from PIL import Image

PORT = 8765
saved_files = []
server_done = threading.Event()

class ExportHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        parsed = urlparse(self.path)
        if parsed.path == "/save_png":
            params = parse_qs(parsed.query)
            filename = params.get("filename", ["output.png"])[0]
            content_length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(content_length)
            
            # The body is base64 dataURL or raw bytes
            if body.startswith(b"data:image/png;base64,"):
                b64_data = body[len(b"data:image/png;base64,"):]
                raw_bytes = base64.b64decode(b64_data)
            else:
                raw_bytes = body
                
            out_path = os.path.join("assets", "png_exports_2000px", filename)
            os.makedirs(os.path.dirname(out_path), exist_ok=True)
            with open(out_path, "wb") as f:
                f.write(raw_bytes)
                
            saved_files.append(out_path)
            print(f"[EXPORT] Successfully saved {filename} ({len(raw_bytes)} bytes)")
            
            self.send_response(200)
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(b"OK")
            return
            
        elif parsed.path == "/done":
            self.send_response(200)
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(b"DONE")
            print("[EXPORT] All exports completed signal received.")
            server_done.set()
            return
            
        self.send_response(404)
        self.end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, GET, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def log_message(self, format, *args):
        # Silence verbose request logging
        pass

def start_server():
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("127.0.0.1", PORT), ExportHandler) as httpd:
        httpd.timeout = 1
        while not server_done.is_set():
            httpd.handle_request()
        print("[EXPORT] Server shutting down gracefully.")

if __name__ == "__main__":
    t = threading.Thread(target=start_server, daemon=True)
    t.start()
    print(f"Export server running on http://127.0.0.1:{PORT}")
    
    # We will trigger Edge headless
    time.sleep(1)
    edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    url = f"http://127.0.0.1:{PORT}/showcase/exporter.html"
    
    cmd = [
        edge_path,
        "--headless=new",
        "--disable-gpu",
        "--allow-running-insecure-content",
        url
    ]
    
    print("Launching Edge to render 2000x2000 canvases...")
    proc = subprocess.Popen(cmd)
    
    # Wait up to 30 seconds for export to complete
    done = server_done.wait(timeout=30)
    proc.terminate()
    
    print("\n--- EXPORT VERIFICATION ---")
    for f in saved_files:
        try:
            im = Image.open(f)
            print(f"[OK] {os.path.basename(f)}: Format={im.format}, Mode={im.mode}, Size={im.size}")
        except Exception as e:
            print(f"[ERR] Error opening {f}: {e}")
