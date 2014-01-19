import srv

ns = srv.net

def ttt( m ):
    print 'got : %s' % m
    ns.send('this is coming from python! ;')
    ns.send('the message is: %s ;' % m)

