import re
import socket
import srv
import testApplication

srv.net.connect()
srv.net.send = srv.net.socS_main.send
patt1 = re.compile('(\w*)\s*(.*?);')

while 1:
    try:
        data = srv.net.connR.recv(1024)
    except socket.error:
        print "socket error!"
        continue
    m = patt1.match(data)
    if not m: continue
    m1,m2 = m.group(1), m.group(2)

    if m1 == 'Exit':
        print 'Session closed: Exit'
        srv.net.close()
        break
    elif m1 == 'test':
        testApplication.ttt(m2)
    else: 
        print "unrecognized message: " + data


