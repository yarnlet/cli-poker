import os
from http.server import BaseHTTPRequestHandler, HTTPServer
import json5
from collections import namedtuple

class PokerServer(BaseHTTPRequestHandler):

  # GET
  def do_GET(self):
    # Send response status code
    self.send_response(200)

    # Send headers
    self.send_header('Content-type','text/plain; charset=utf-8')
    self.send_header('Content-length', str(len("fuck off!")))
    self.end_headers()

    # Write content as utf-8 data
    self.wfile.write(bytes("fuck off!", "utf8"))

    # print path
    print(self.path)
    return


class Game:
    def __init__(self, game_config) -> None:
        # parse config (direct if dict, from file if str)
        try:
            self.game_config = game_config if type(game_config) == dict else json5.loads(open(game_config, "r").read())
        except:
            print("Error reading game config file, using default config")
            return
        
        self.players = []
        self.round = 0
        self.deck = 0


def run():
    print('starting server...')

    # Server settings
    # Choose port 8080, for port 80, which is normally used for a http server, you need root access
    server_address = ('127.0.0.1', 8081)
    httpd = HTTPServer(server_address, PokerServer)
    print('running server...')
    httpd.serve_forever()
  
run()
