class IAMLogger:
    __instance = None
    __user = None

    def __init__(self, username, password):
        if IAMLogger.__instance is None:
            IAMLogger.__user = {'username': username, 'password': password}
            IAMLogger.__instance = self

    @staticmethod
    def login(username, password):
        if IAMLogger.__instance is None:
            IAMLogger(username, password)
        return IAMLogger.__instance

    @staticmethod
    def logout():
        IAMLogger.__instance = None

    @staticmethod
    def get_instance():
        return IAMLogger.__instance

    @staticmethod
    def get_user_details():
        if IAMLogger.__instance:
            return IAMLogger.__user
        else:
            return {}

# Decorator class for logging
class IAMLoggerWithLogging:
    def __init__(self, decorated_logger):
        self.decorated_logger = decorated_logger

    def login(self, username, password):
        print(f"User {username} is logging in.")
        return self.decorated_logger.login(username, password)

    def logout(self):
        user_details = self.decorated_logger.get_user_details()
        if user_details:
            print(f"User {user_details['username']} is logging out.")
        else:
            print("No user to log out.")
        self.decorated_logger.logout()

# Usage with the decorator
base_logger = IAMLogger('senjack', 'password')  # Create the base logger with initial user
decorated_logger = IAMLoggerWithLogging(base_logger)  # Wrap the base logger with the decorator

# Now you can use decorated_logger
decorated_logger.login('demetira', 'demetira1')
decorated_logger.logout()