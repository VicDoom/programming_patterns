# lab1 strategy
# lab2 шаблонный метод (спросить у кого-нибудь)
from Cryptodome.Cipher import DES
from Cryptodome.Cipher import AES
from Cryptodome.Cipher import ARC4

class StrategyInputInfo:
    def inputInfo(self):
        pass

class InputInfoConsole(StrategyInputInfo):
    def inputInfo(self):
        print('Please, enter key and text for encoding...')
        self.key = input()
        self.text = input()

class InputInfoFile(StrategyInputInfo):
    def inputInfo(self):
        f = open('input.txt')
        self.key = f.readline()
        self.text = f.readline()

class StrategyCipher:
    def execute(self):
        pass

class CipherDES(StrategyCipher):
    def execute(self):
        key = bytes(self.key, encoding="utf-8")
        key = self.pad(key, 8)

        des = DES.new(key, DES.MODE_ECB)

        text = bytes(self.text, encoding="utf-8")

        padded_text = self.pad(text, 8)

        encrypted_text = des.encrypt(padded_text)

        return encrypted_text

class CipherAES(StrategyCipher):
    def execute(self):
        key = bytes(self.key, encoding="utf-8")
        key = self.pad(key, 16)

        text = bytes(self.text, encoding="utf-8")

        aes = AES.new(key, AES.MODE_EAX)
        encrypted_text = aes.encrypt(text)
        return encrypted_text

class CipherARC4(StrategyCipher):
    def execute(self):
        key = self.pad(bytes(self.key, encoding="utf-8"), 16)
        cipher = ARC4.new(key)

        text = bytes(self.text, encoding="utf-8")
        encrypted_text = cipher.encrypt(text)
        return encrypted_text

class Context:
    def __init__(self, strategyCipher: StrategyCipher, strategyInputInfo: StrategyInputInfo):
        self._strategyCipher = strategyCipher
        self._strategyInputInfo = strategyInputInfo

    @property
    def strategyCipher(self):
        return self._strategyCipher

    @strategyCipher.setter
    def strategyCipher(self, strategyCipher: StrategyCipher):
        self._strategyCipher = strategyCipher

    @property
    def strategyInputInfo(self):
        return self._strategyInputInfo

    @strategyInputInfo.setter
    def strategyInputInfo(self, strategyInputInfo: StrategyInputInfo):
        self._strategyInputInfo = strategyInputInfo

    def do_some_cipher(self):
        return self._strategyCipher.execute(self)

    def get_info(self):
        self._strategyInputInfo.inputInfo(self)

    def pad(self, text, num):
        while len(text) % num != 0:
            text += b' '
        return text

if __name__ == "__main__":
    print("DES:")
    context = Context(CipherDES, InputInfoFile)
    context.get_info()
    print(context.do_some_cipher())

    print("AES:")
    context.strategyCipher = CipherAES
    context.get_info()
    print(context.do_some_cipher())

    print("ARC4")
    context.strategyCipher = CipherARC4
    context.strategyInputInfo = InputInfoConsole
    context.get_info()
    print(context.do_some_cipher())
