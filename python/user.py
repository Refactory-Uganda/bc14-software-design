'''Singleton pattern ensures that there is only one instance of the class,
 and it provides a global point of access to that instance.'''

class IAMlogger: 
    __instance = None #private class variable that holds a single instance
    __username = None
    __password = None

    def __init__(self, username, password):
        if IAMlogger.__instance is None:
            IAMlogger.__username = username
            IAMlogger.__password = password
            IAMlogger.__instance = self

    @staticmethod
    def login(username, password):
        if IAMlogger.__instance is None:
            IAMlogger(username, password)
        return IAMlogger.__instance

    @staticmethod
    def logout():
        IAMlogger.__instance = None

    @staticmethod
    def get_instance():
        return IAMlogger.__instance

    @staticmethod
    def get_user_details():
        if IAMlogger.__instance:
            return {
                'username': IAMlogger.__username,
                'password': IAMlogger.__password
            }
        else:
            return {}

# Usage
user1 = IAMlogger.login('senjack', 'password')
IAMlogger.logout()
user2 = IAMlogger.login('demetira', 'demetira1')

print(IAMlogger.get_user_details())  
print(IAMlogger.get_user_details())  
