import ssl
import socket
import json

host = 'xapi.xtb.com'
port = 5124
USERID = 16556495
PASSWORD = 'Robert0s!'

host = socket.getaddrinfo(host, port)[0][4][0]
s = socket.socket()
s.connect((host, port))
s = ssl.SSLContext().wrap_socket(s)

parameters = {
    "command": "login",
    "arguments": {
        "userId": USERID,
        "password": PASSWORD

    },
    "prettyPrint": True
}
packet = json.dumps(parameters, indent=4)
s.send(packet.encode("UTF-8"))

END = b'\n\n'
response = s.recv(8192)


###################################################
# sending command parameters
parameters = {
    "command": "getAllSymbols",
    "arguments": {
        "symbol": "CDR.PL"
    }
}

# {
#     "command": "getChartLastRequest",
#     "arguments": {
#         "info": {
#             "period": 5,
#             "start": 1722113765860,
#             "symbol": "EURUSD"
#         }
#     }
# }

packet = json.dumps(parameters)
s.send(packet.encode("UTF-8"))

# -------------------------------------------------

response = s.recv(8192)
if END in response:
    print('getAllSymbols:', response[:response.find(END)])
else:
    print('getAllSymbols:', response)

###################################################


if END in response:
    print('Print login: {}'.format(response[:response.find(END)]))

parameters = {
    "command": "logout"
}
packet = json.dumps(parameters, indent=4)
s.send(packet.encode("UTF-8"))

response = s.recv(8192)
if END in response:
    print('Print logout: {}'.format(response[:response.find(END)]))
