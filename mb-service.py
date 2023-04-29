import argparse
from flask import Flask
from waitress import serve
from paste.translogger import TransLogger
import app

# Parse command line arguments
def parse_arguments():
    parser = argparse.ArgumentParser(description='Mandelbrot Service')
    parser.add_argument('--host', default='0.0.0.0', help='Host to bind the service (default: 0.0.0.0)')
    parser.add_argument('--port', type=int, default=8000, help='Port to bind the service (default: 8000)')
    parser.add_argument('--worker-threads', type=int, default=4, help='Number of worker threads (default: 4)')
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_arguments()
    print(f'Starting server at {args.host}:{args.port} using {args.worker_threads} worker thread(s)')
    serve(TransLogger(app.create_app(), setup_console_handler=False), 
          host=args.host, port=args.port, threads=args.worker_threads )
    
    