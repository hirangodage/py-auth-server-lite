from cheroot.wsgi import Server as WSGIServer,PathInfoDispatcher
import signal
import TestResourceServer
import AuthanticationServer

#host multiple instances
d=PathInfoDispatcher({'/app':TestResourceServer.TestApp,'/auth':AuthanticationServer.AuthApp})
server=WSGIServer(('0.0.0.0',8088),d)
#docker run -d -p 8088:8088 -t nginx
#start web server
try:
      server.start()
except KeyboardInterrupt:
      server.stop()