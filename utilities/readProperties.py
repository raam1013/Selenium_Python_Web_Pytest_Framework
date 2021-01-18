import  configparser

config = configparser.RawConfigParser()
config.read('.\\Configurations\\config.ini')


class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('common info' , 'baseURL')
        return url

    @staticmethod
    def getApplicationUserEmail():
        email = config.get('common info', 'username')
        return email

    @staticmethod
    def getApplicationPassword():
        passwd = config.get('common info', 'password')
        return passwd
