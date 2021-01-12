import mh
import solitaire
import socket
import common

'''
I. valaki be akar regisztralni:

   { type: 1, port: 4000, public_key: (123,234....) } 
        -> { status: "ok" }

II. valaki le akar kerdezni:

   { type: 0, port: 4001 }
        -> { status: "not found" }
        -> { status: "ok", public_key: (123123,342,...) }
'''

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((common.HOST, common.SERVER_PORT))
    s.listen()
    print("KeyServer started")

    dictionary = {}

    while True:
        clientsocket, address = s.accept()
        request = common.receive(clientsocket)

        if request["type"] == 1:
            port = request["port"]
            public_key = request["public_key"]
            dictionary[port] = public_key
            print("Client registred: ", port, public_key)
            common.send(clientsocket, {"status": "ok"})
        else:
            port = request["port"]
            if port in dictionary:
                common.send(clientsocket, {"status": "ok", "public_key":dictionary[port]})
                print("Request for", port, "-> ok, public key:", dictionary[port])
            else:
                common.send(clientsocket, {"status": "not found"})
                print("Request for", port, "-> not found")

        clientsocket.close()







main()