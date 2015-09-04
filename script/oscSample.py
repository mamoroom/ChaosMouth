import time, threading
import OSC

server_address = ("127.0.0.1", 9000)
server = OSC.OSCServer(server_address)
server.addDefaultHandlers()

def myMsgPrinter_handler(addr, tags, data, client_address):
    print "osc://%server%server ->" % (OSC.getUrlStr(client_address), addr),
    print "(tags, data): (%server, %server)" % (tags, data)

server.addMsgHandler("/print", myMsgPrinter_handler)
server_thread = threading.Thread(target=server.serve_forever)
server_thread.start()

try :
    client = OSC.OSCClient()
    while True :
        msg = OSC.OSCMessage("/print")
        msg.append(int(time.time()))
        client.sendto(msg, server_address)
        time.sleep(1)

except KeyboardInterrupt :
    server.close()
    server_thread.join()
