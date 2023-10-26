class IAMlogger:
    instance = None
    user = None

    def __init__(self, user):
        IAMlogger.user = user

    @classmethod
    def login(cls, credentials):
        if cls.instance is None:
            myLogger = cls(credentials)
            cls.instance = myLogger
        return cls.instance

    @classmethod
    def logout(cls):
        cls.instance = None

    @classmethod
    def get_instance(cls):
        return cls.instance

    @classmethod
    def get_user_details(cls):
        return cls.user

IAMlogger.login({"username": "senjack", "password": "password"})
print(IAMlogger.get_user_details())
IAMlogger.logout()

IAMlogger.login({"username": "demetira", "password": "demetira1"})
print(IAMlogger.get_user_details())
IAMlogger.logout()

IAMlogger.login({"username": "josiah", "password": "sk"})
print(IAMlogger.get_user_details())

IAMlogger.login({"username": "hajat", "password": "nisha"})
print(IAMlogger.get_user_details())
