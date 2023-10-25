from strategy import *
class IAMlogger:
    _instance = None
    _user = None

    def __init__(self, user):
        if IAMlogger._instance is not None:
            raise Exception("This class is a singleton!")
        else:
            IAMlogger._instance = self
            IAMlogger._user = user

    @classmethod
    def login(cls, credentials):
        if cls._instance is None:
            IAMlogger._login_strategy.login(credentials)
            cls._instance = cls(credentials)
        return cls._instance
    
    @classmethod
    def set_login_strategy(cls, login_strategy:LoginStrategy):
        cls._login_strategy = login_strategy

    @classmethod
    def logout(cls):
        cls._instance = None

    @classmethod
    def getInstance(cls):
        return cls._instance

    @classmethod
    def getUserDetails(cls):
        return cls._user
    @classmethod
    def set_login_strategy(cls,login_strategy:LoginStrategy):
       cls.login_strategy = login_strategy

from strategy import UsernamePasswordStrategy,EmailPasswordStrategy


IAMlogger.login({"username":"senjack", "password":"password"})
print(IAMlogger.getUserDetails())
IAMlogger.logout()

IAMlogger.login({"username":"demetira", "password":"demetira1"})
print(IAMlogger.getUserDetails())
IAMlogger.logout()

IAMlogger.set_login_strategy(EmailPasswordStrategy())
IAMlogger.login({"email":"josiah@gmail.com", "password":"sk"})
print(IAMlogger.getUserDetails())
IAMlogger.logout()

IAMlogger.set_login_strategy(PhonenumberPasswordStrategy())
IAMlogger.login({"phonenumber":"3256789080", "password":"nisha"})
print(IAMlogger.getUserDetails())



