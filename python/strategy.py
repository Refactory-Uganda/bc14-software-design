'''
Login strategies.
context class i.e IAMlogger
and then the strategies.
we have concrete and abstraction classes under the strategies.

'''
from abc import ABC, abstractmethod

class LoginStrategy(ABC):
    @abstractmethod
    def login(self, credentials: dict) -> None:
        pass

# Concrete strategies
class UsernamePasswordStrategy(LoginStrategy):
    def login(self, credentials: dict) -> None:
        print(f"username: {credentials['username']}, password: {credentials['password']}")

class EmailPasswordStrategy(LoginStrategy):
    def login(self, credentials: dict) -> None:
        print(f"username: {credentials['username']}, password: {credentials['password']}")

class PhonenumberPasswordStrategy(LoginStrategy):
    def login(self, credentials: dict) -> None:
        print(f"username: {credentials['username']}, password: {credentials['password']}")

              




    
