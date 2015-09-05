import OSC
import sys

server_address = ("192.168.1.102", 9000)

try :
    client = OSC.OSCClient()
    msg = OSC.OSCMessage("/media")
    msg.append(int(sys.argv[1]))
    client.sendto(msg, server_address)

except KeyboardInterrupt :
    print "finish!"
