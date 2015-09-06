import time, threading
import OSC
import subprocess

#server_address = ("127.0.0.1", 9000)
server_address = ("172.20.10.11", 9000)
server = OSC.OSCServer(server_address)
server.addDefaultHandlers()
process = subprocess.Popen( "tail -f /home/root/git/github-muraji/ChaosMouth/script/hoge.py", shell=True, stderr=subprocess.STDOUT  )

def myMediaChange_handler(addr, tags, data, client_address):
    print data[0]
    global process
    if data[0] == 1:
        resetMedia()
        cmd = "aplay /home/root/git/github-muraji/ChaosMouth/media/high/1.wav"
        process = subprocess.Popen( cmd, shell=True, stderr=subprocess.STDOUT  )
        print process
    elif data[0] == 2:
        resetMedia()
        cmd = "aplay /home/root/git/github-muraji/ChaosMouth/media/high/2.wav"
        process = subprocess.Popen( cmd, shell=True, stderr=subprocess.STDOUT  )
        print process
    elif data[0] == 3:
        resetMedia()
        cmd = "aplay /home/root/git/github-muraji/ChaosMouth/media/high/3.wav"
        process = subprocess.Popen( cmd, shell=True, stderr=subprocess.STDOUT  )
        print process

def resetMedia():
    global process
    print "kill to:"
    print process
    process.kill()
    time.sleep(0.1)


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
