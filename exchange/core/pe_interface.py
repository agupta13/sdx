__author__ = 'arpit'
import threading
import SocketServer
import policy_sdx
import params_sdx
import logging as log
log.basicConfig(filename='sdx.log',level=log.INFO)


exchangeIP = "127.0.0.1"

## Thread to handle incoming requests from various players
class ThreadedTCPRequestHandler_exchange(SocketServer.BaseRequestHandler):

    def handle(self):
        log.info('Handler called')
        data = self.request.recv(1024)
        #print self.client_address[0]
        log.info('Received: %s',data)

        ## create policy object
        policy_obj = policy_sdx.policy(self.client_address[0])
        policy_obj.policy_raw = data

        ## insert policy object to Policy Queue
        priority = 1 # Currently no logic to discern bw policies sent by various players
        params_sdx.PQ.put(policy_obj,priority)

        ## operations completed for this thread, send ok and let it go !
        response = 'ok'
        self.request.sendall(response)

class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass

def main():
    HOST, PORT = exchangeIP, 9006
    server_exchange = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler_exchange)
    ip, port = server_exchange.server_address
    server_thread_mc = threading.Thread(target=server_exchange.serve_forever)
    server_thread_mc.daemon = True
    server_thread_mc.start()
    log.info('Server running over IP:%s, port: %s',ip,port)

    # Keep server on until you get a keyboard interrupt "ctrl+c"
    try:
        server_exchange.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server_exchange.shutdown()
        log.info('Shutting down exchange server')
        log.info('bye')


if __name__=="__main__":
    main()