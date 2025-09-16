import http.server
import socketserver
import json
import subprocess
import logging

# Configure logging for better feedback in the terminal.
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

PORT = 8000

class SimulatorRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        """Handle GET requests to the server."""
        if self.path == '/simulators':
            logging.info("Received request for simulator list.")
            try:
                # 1. Run the `xcrun simctl` command to get a JSON list of simulators.
                # The `available` flag ensures we only get a list of simulators that are ready to use.
                process = subprocess.run(
                    ['xcrun', 'simctl', 'list', 'devices', 'available', '--json'],
                    capture_output=True,
                    text=True,
                    check=True
                )
                
                # 2. Parse the JSON output from the command.
                sim_data = json.loads(process.stdout)
                
                # 3. Extract the name and UDID for each available simulator.
                # We filter out unnecessary information to keep the response clean.
                available_simulators = []
                for runtime, devices in sim_data['devices'].items():
                    for device in devices:
                        available_simulators.append({
                            'name': device['name'],
                            'udid': device['udid'],
                            'runtime': runtime
                        })
                
                # 4. Prepare and send the JSON response.
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                # This header is crucial for allowing a front-end web app to connect to this server.
                self.send_header('Access-Control-Allow-Origin', '*') 
                self.end_headers()
                
                response_json = json.dumps({'simulators': available_simulators}, indent=4)
                self.wfile.write(response_json.encode('utf-8'))
                
                logging.info(f"Successfully returned {len(available_simulators)} simulators.")

            except subprocess.CalledProcessError as e:
                # Handle errors if the command fails to run.
                logging.error(f"Error executing simctl: {e.stderr}")
                self.send_response(500)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                error_message = json.dumps({'error': 'Failed to get simulator list.', 'details': e.stderr.strip()})
                self.wfile.write(error_message.encode('utf-8'))

            except json.JSONDecodeError as e:
                # Handle errors if the output from simctl isn't valid JSON.
                logging.error(f"Error parsing simctl output: {e}")
                self.send_response(500)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                error_message = json.dumps({'error': 'Invalid JSON response from simctl.'})
                self.wfile.write(error_message.encode('utf-8'))
        else:
            # Handle requests for other paths
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write("404 Not Found. Please request the /simulators endpoint.".encode('utf-8'))

    def do_OPTIONS(self):
        """Handle pre-flight OPTIONS requests for CORS."""
        self.send_response(200, "ok")
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), SimulatorRequestHandler) as httpd:
        logging.info("Starting server...")
        logging.info(f"Serving at http://localhost:{PORT}")
        logging.info("Access http://localhost:8000/simulators to get the list.")
        httpd.serve_forever()

