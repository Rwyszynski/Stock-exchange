import json
import socket
import logging
import time
import ssl
from threading import Thread

# set to true on debug environment only
DEBUG = True

# default connection properites
DEFAULT_XAPI_ADDRESS = 'xapi.xtb.com'
DEFAULT_XAPI_PORT = 5124
DEFUALT_XAPI_STREAMING_PORT = 5125

# wrapper name and version
WRAPPER_NAME = 'python'
WRAPPER_VERSION = '2.5.0'

# API inter-command timeout (in ms)
API_SEND_TIMEOUT = 100

# max connection tries
API_MAX_CONN_TRIES = 3

# logger properties
logger = logging.getLogger("jsonSocket")
FORMAT = '[%(asctime)-15s][%(funcName)s:%(lineno)d] %(message)s'
logging.basicConfig(format=FORMAT)

if DEBUG:
    logger.setLevel(logging.DEBUG)
else:
    logger.setLevel(logging.CRITICAL)


class JsonSocket(object):
    def __init__(self, address, port, encrypt=False):
        self._ssl = encrypt
        if self._ssl != True:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket = ssl.wrap_socket(sock)
        self.conn = self.socket
        self._timeout = None
        self._address = address
        self._port = port
        self._decoder = json.JSONDecoder()
        self._receivedData = ''

    def connect(self):
        for i in range(API_MAX_CONN_TRIES):
            try:
                self.socket.connect((self.address, self.port))
            except socket.error as msg:
                logger.error("SockThread Error: %s" % msg)
                time.sleep(0.25)
                continue
            logger.info("Socket connected")
            return True
        return False

    def _read(self, bytesSize=4096):
        if not self.socket:
            raise RuntimeError("socket connection broken")
        while True:
            char = self.conn.recv(bytesSize).decode()
            self._receivedData += char
            try:
                (resp, size) = self._decoder.raw_decode(self._receivedData)
                if size == len(self._receivedData):
                    self._receivedData = ''
                    break
                elif size < len(self._receivedData):
                    self._receivedData = self._receivedData[size:].strip()
                    break
            except ValueError as e:
                continue
        logger.info('Received: ' + str(resp))
        return resp

    def _readObj(self):
        msg = self._read()
        return msg

    def _closeConnection(self):
        self.conn.close()


class APIClient(JsonSocket):
    def __init__(self, address=DEFAULT_XAPI_ADDRESS, port=DEFAULT_XAPI_PORT, encrypt=True):
        super(APIClient, self).__init__(address, port, encrypt)
        if (not self.connect()):
            raise Exception("Cannot connect to " + address + ":" +
                            str(port) + " after " + str(API_MAX_CONN_TRIES) + " retries")

    def execute(self, dictionary):
        self._sendObj(dictionary)
        return self._readObj()

    def disconnect(self):
        self.close()

    def commandExecute(self, commandName, arguments=None):
        return self.execute(baseCommand(commandName, arguments))

    def disconnect(self):
        self._running = False
        self._t.join()
        self.close()

    def subscribePrice(self, symbol):
        self.execute(dict(command='getTickPrices',
                     symbol=symbol, streamSessionId=self._ssId))

# Command templates


def baseCommand(commandName, arguments=None):
    if arguments == None:
        arguments = dict()
    return dict([('command', commandName), ('arguments', arguments)])


def loginCommand(userId, password, appName=''):
    return baseCommand('login', dict(userId=userId, password=password, appName=appName))


def main():

    # enter your login credentials here
    userId = 16556495
    password = "Robert0s!"

    # create & connect to RR socket
    client = APIClient()

    # connect to RR socket, login
    loginResponse = client.execute(
        loginCommand(userId=userId, password=password))
    logger.info(str(loginResponse))

    # check if user logged in correctly
    if (loginResponse['status'] == False):
        print('Login failed. Error code: {0}'.format(
            loginResponse['errorCode']))
        return

    # get ssId from login response
    ssid = loginResponse['streamSessionId']

    # second method of invoking commands
    resp = client.commandExecute('getAllSymbols')

    # create & connect to Streaming socket with given ssID
    # and functions for processing ticks, trades, profit and tradeStatus
    sclient = APIStreamClient(ssId=ssid, tickFun=procTickExample, tradeFun=procTradeExample,
                              profitFun=procProfitExample, tradeStatusFun=procTradeStatusExample)

    # subscribe for prices
    sclient.subscribePrices(['EURUSD', 'EURGBP', 'EURJPY'])

    # gracefully close RR socket
    client.disconnect()


if __name__ == "__main__":
    main()
