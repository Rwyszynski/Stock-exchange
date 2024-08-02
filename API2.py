import ssl
import socket
import json
import time
import datetime
from datetime import datetime
import dateutil.relativedelta


def download(period, stock):
    # times, stock, period
    d1 = datetime.now() - dateutil.relativedelta.relativedelta(days=2)
    unixtime = datetime.timestamp(d1)*1000

    d2 = datetime.now()
    unixtime2 = datetime.timestamp(d2)*1000

    d1 = int(unixtime)
    d2 = int(unixtime2)
    print(d1)
    print(d2)

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
        "command": "getChartRangeRequest",
        "arguments": {
            "info": {
                "end": d2,
                "period": period,
                "start": d1,
                "symbol": stock,
                "ticks": 0
            }
        }
    }

    packet = json.dumps(parameters)
    s.send(packet.encode("UTF-8"))

    # -------------------------------------------------

    response = s.recv(8192)

    ###################################################
    return response[:response.find(END)]


download(1440, "06N.PL")


# 5min, 30min, 4hour, 1day
# 5, 30, 240, 1440
