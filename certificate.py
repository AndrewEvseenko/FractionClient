import json
from rsa import PublicKey
from rsa import PrivateKey


class Certificate:

    def __init__(self, name, expire, issue, pubkey, privkey=PrivateKey(0, 0)):
        self.__name = name
        self.__pubkey = pubkey
        self.__privkey = privkey
        self.__expire = expire
        self.__issue = issue

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def getPublicKey(self):
        return self.__pubkey

    def setPublicKey(self, pubkey):
        self.__pubkey = pubkey

    def getPrivateKey(self):
        return self.__privkey

    def getExpire(self,):
        return self.__expire

    def setExpire(self, expire):
        self.__expire = expire

    def getIssue(self):
        return self.__issue

    def setIssue(self, issue):
        self.__issue = issue

    def getObjects(self, add=False):
        array = [self.__name, self.__expire, self.__issue, self.__pubkey.e, self.__pubkey.n]
        if add:
            array = array + self.__privkey.e + self.__privkey.n
        return array

    def getJSON(self, add=False):
        return json.dumps(self.getObjects(add))

    def toFile(self, file, add=False):
        json.dump(self.getObjects(add), file)

    @classmethod
    def fromFile(cls, file):
        arr = json.load(file)
        private_n = 0
        private_e = 0
        if len(arr) > 5:
            private_e = arr[5]
            private_n = arr[6]
        return cls(arr[0], arr[1], arr[2], PublicKey(arr[3], arr[4]), PrivateKey(private_e, private_n))

    @classmethod
    def fromJSON(cls, json_str):
        arr = json.loads(json_str)
        private_n = 0
        private_e = 0
        if len(arr) > 5:
            private_e = arr[5]
            private_n = arr[6]
        return cls(arr[0], arr[1], arr[2], PublicKey(arr[3], arr[4]), PrivateKey(private_e, private_n))
