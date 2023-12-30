import socketserver
import http.server

from termcolor import colored


def serve(lh, lp):
    print(colored('----{    HTTP  SERVER    }----\n', attrs=["bold"]))

    handler = http.server.SimpleHTTPRequestHandler

    with socketserver.TCPServer((lh, lp), handler) as httpd:
        print(colored(f"[+] Server started at {lh}:{lp}\n", "green"))
        httpd.serve_forever()


