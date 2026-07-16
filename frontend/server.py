import http.server
import socketserver
import json
import os
import urllib.parse
import sys
# Add parent directory and engine folder to Python path to import tesm_simulation and historical_validation
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'engine'))
from tesm_simulation import run_simulation, generate_scenario_matrix, run_monte_carlo
from historical_validation import verify_historical_case

PORT = 8080

class TESMRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Enable CORS for browser requests
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

    def do_POST(self):
        parsed_url = urllib.parse.urlparse(self.path)
        path = parsed_url.path
        
        if path in ['/api/simulate', '/api/matrix', '/api/montecarlo', '/api/historical']:
            content_length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(content_length).decode('utf-8')
            params = json.loads(body) if body else {}
            
            try:
                if path == '/api/simulate':
                    res = run_simulation(params)
                elif path == '/api/matrix':
                    res = generate_scenario_matrix(params)
                elif path == '/api/montecarlo':
                    trials = int(params.pop('trials', 200))
                    res = run_monte_carlo(params, trials=trials)
                elif path == '/api/historical':
                    crisis = params.get('crisis', 'dotcom')
                    res = verify_historical_case(crisis)
                
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                # JSON serializable formatting
                res_json = json.dumps(res, default=str)
                self.end_headers()
                self.wfile.write(res_json.encode('utf-8'))
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"error": str(e)}).encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()

def run_server():
    # Force socket reuse
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), TESMRequestHandler) as httpd:
        print(f"TESM Unified Python Server running at http://localhost:{PORT}/")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down server.")

if __name__ == "__main__":
    # Ensure working directory is the frontend directory so local files are served correctly
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    run_server()
