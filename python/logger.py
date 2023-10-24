'''Singleton pattern ensures that there is only one instance of the class,
 and it provides a global point of access to that instance.'''

class IAMlogger: 
    __instance = None #private class variable that holds a single instance
    __user =  None

    def __init__(self, __user):
        IAMlogger.__user = __user

    @staticmethod
    def login(credentials):
        if IAMlogger.__instance is None:
            my_logger = IAMlogger(credentials["data"])
            IAMlogger.__instance = my_logger
        return IAMlogger.__instance

    @staticmethod
    def logout():
        IAMlogger.__instance = None

    @staticmethod
    def get_instance():
        return IAMlogger.__instance

    @staticmethod
    def get_user_details():
        return  IAMlogger.__user

# Usage
user1 = IAMlogger.login({'data': {'username':'senjack','password':'password'}})
# IAMlogger.logout()
user2 = IAMlogger.login({'data': {'username':'demetira','password': 'demetira1'}})

print(IAMlogger.get_user_details())  
print(IAMlogger.get_user_details())  
