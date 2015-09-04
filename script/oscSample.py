import time, threading
import OSC
import subprocess

#server_address = ("127.0.0.1", 9000)
server_address = ("192.168.1.102", 9000)
server = OSC.OSCServer(server_address)
server.addDefaultHandlers()
cmd = "cmixer cset numid=3 1"
out = subprocess.Popen( cmd, shell=True, stderr=subprocess.STDOUT  )

def myMsgPrinter_handler(addr, tags, data, client_address):
    print "osc://%server%server ->" % (OSC.getUrlStr(client_address), addr),
    print "(tags, data): (%server, %server)" % (tags, data)

def myMediaChange_handler(addr, tags, data, client_address):
    print data[0]
    if data[0] == 1:
        resetMedia()
        cmd = "amixer cset numid=1 65% && mpg321 /home/pi/git/ChaosMouth/media/talkingSample.mp3 --loop 0"
        out = subprocess.Popen( cmd, shell=True, stderr=subprocess.STDOUT  )
    elif data[0] == 2:
        resetMedia()
        cmd = "amixer cset numid=1 90% && mpg321  /home/pi/git/ChaosMouth/media/talkingSample.mp3 --loop 0"
        out = subprocess.Popen( cmd, shell=True, stderr=subprocess.STDOUT  )
    elif data[0] == 3:
        resetMedia()
        cmd = "amixer cset numid=1 90% && mpg321  /home/pi/git/ChaosMouth/media/radioSample.mp3 --loop 0"
        out = subprocess.Popen( cmd, shell=True, stderr=subprocess.STDOUT  )

def resetMedia():
        cmd = "pkill mpg321"
        out = subprocess.Popen( cmd, shell=True, stderr=subprocess.STDOUT  )

server.addMsgHandler("/print", myMsgPrinter_handler)
server.addMsgHandler("/media", myMediaChange_handler)
server_thread = threading.Thread(target=server.serve_forever)
server_thread.start()


#try :
#    client = OSC.OSCClient()
#    while True :
#        msg = OSC.OSCMessage("/print")
#        msg.append(int(time.time()))
#        client.sendto(msg, server_address)
#        time.sleep(1)

#except KeyboardInterrupt :
#    server.close()
#    server_thread.join()
