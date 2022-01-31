# # Based on work from https://RandomNerdTutorials.com
import config
import gc
import ledapp
from time import sleep


# import sys
#
def web_page():
    html = """<html><head> <title>numbrs.config</title> <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="icon" href="data:,"> <style>html{font-family: 'Courier New', monospace; display:inline-block; margin: 0px auto; text-align: center;}
  h1{color: #0F3376; padding: 2vh;}p{font-size: 1.5rem;}.button{display: inline-block; background-color: #3aac59; border: none;
  border-radius: 4px; color: white; padding: 16px 40px; text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}
  .button2{background-color: #9eb6b8;}.button3{background-color: #FF9900;}</style></head><body> <h1>numbrs.config</h1>
  <p>welcome to numbrs. </p>
  <p>here you can change the displayed values.</p>
  <p>  Displayed: <strong>""" + config.display + """</strong></p>
  <a href="?req=eth"><button class="button button2">Etherum</button></a></p></body></html><p>
  <a href="?req=eth"><button class="button button2">Etherum</button></a></p></body></html><p>
  <a href="/?req=btc"><button class="button button3">Bitcoin</button></a></p></body></html><p>
  <a href="?req=mkr"><button class="button button">Maker Coin</button></a></p></body></html>
  <a href="?req=off"><button class="button button">Turn Off</button></a></p></body></html>
  <p>(c) janco loenneker, 2022 </p> """
    return html


#
#
# running = True
#
# while running:
#
#
#     try:
#         s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         s.bind(('', 80))
#         s.listen()
#         conn, addr = s.accept()
#         print('Got a connection from %s' % str(addr))
#         request = conn.recv(1024)
#         request = str(request)
#         print('Content = %s' % request)
#         btc = request.find('/?req=btc')
#         eth = request.find('/?req=eth')
#         xch = request.find('/?req=xch')
#         if btc == 6:
#             print('BTC')
#             config.basevalue = "BTCduPenner"
#         if eth == 6:
#             print('ETH')
#             config.basevalue = "ETHduPenner"
#         if xch == 6:
#             print('XCH')
#             config.basevalue = "XCHduPenner"
#         response = web_page()
#         conn.send('HTTP/1.1 200 OK\n')
#         conn.send('Content-Type: text/html\n')
#         conn.send('Connection: close\n\n')
#         conn.sendall(response)
#         conn.close()
#     except KeyboardInterrupt:
#         running = False
#
#     except:
#         print(sys.stderr)

# Complete project details at https://RandomNerdTutorials.com

# def web_page():
#     if led.value() == 1:
#         gpio_state = "ON"
#     else:
#         gpio_state = "OFF"
#
#     html = """<html><head> <title>ESP Web Server</title> <meta name="viewport" content="width=device-width, initial-scale=1">
#   <link rel="icon" href="data:,"> <style>html{font-family: Helvetica; display:inline-block; margin: 0px auto; text-align: center;}
#   h1{color: #0F3376; padding: 2vh;}p{font-size: 1.5rem;}.button{display: inline-block; background-color: #e7bd3b; border: none;
#   border-radius: 4px; color: white; padding: 16px 40px; text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}
#   .button2{background-color: #4286f4;}</style></head><body> <h1>ESP Web Server</h1>
#   <p>GPIO state: <strong>""" + gpio_state + """</strong></p><p><a href="/?led=on"><button class="button">ON</button></a></p>
#   <p><a href="/?led=off"><button class="button button2">OFF</button></a></p></body></html>"""
#     return html
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('', 80))
s.listen(5)


def main():
    while True:
        try:
            sleep(1)
            print("Hello, I'm still here :)")
            conn, addr = s.accept()
            print('Got a connection from %s' % str(addr))
            request = conn.recv(1024)
            request = str(request)
            print('Content = %s' % request)
            btc = request.find('/?req=btc')
            eth = request.find('/?req=eth')
            mkr = request.find('/?req=mkr')
            off = request.find('/?req=off')
            if btc == 6:
                print('BTC')
                config.basevalue = 'BTCUSD'
                config.display = 'Bitcoin!'
                config.run = 1
                print(config.run)
            if eth == 6:
                print('ETH')
                config.basevalue = 'ETHUSD'
                config.display = 'Etherum'
                config.run = 1
                print(config.run)
            if mkr == 6:
                print('XCH')
                config.basevalue = 'MKRUSD'
                config.display = 'Makercoin!'
                config.run = 1
                print(config.run)
            if off == 6:
                print('OFF')
                config.display = 'Turned off!'
                config.run = 0
            response = web_page()
            conn.send('HTTP/1.1 200 OK\n')
            conn.send('Content-Type: text/html\n')
            conn.send('Connection: close\n\n')
            conn.sendall(response)
            conn.close()
            if config.run == 1:
                ledapp.init()
            if config.run == 0:
                ledapp.clear()

        except OSError as e:
            print(e)
main()
