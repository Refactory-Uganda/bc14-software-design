from abc import ABC, abstractmethod
from computer import Computer, Laptop
from input_devices import Keyboard, Mouse
from memory import PrimaryMemory, SecondaryMemory
from output_devices import Monitor, Projector
from processors import AMD, Intel, NVIDIA
from facade import *
from brands import Lenovo

# Step 3: Create an abstract decorator class for implementing the Computer interface.
class ComputerDecorator(Computer, ABC):
    def __init__(self, decorated_computer: Computer):
        self.decorated_computer = decorated_computer

    @abstractmethod
    def cost(self) -> int:
        pass


# Step 4: Create concrete decorator classes extending the ComputerDecorator class.
class WirelessDecorator(ComputerDecorator):
    def cost(self) -> int:
        return self.decorated_computer.cost()


class WirelessMouseDecorator(WirelessDecorator):
    def cost(self) -> int:
        return self.decorated_computer.cost() + 10  # Example: Add 10 to the cost


class WirelessSpeakerDecorator(WirelessDecorator):
    def cost(self) -> int:
        return self.decorated_computer.cost() + 20  # Example: Add 20 to the cost


# Step 5: Use the decorators to decorate Computer objects.
computer1 = Computer(Mouse(), AMD(), PrimaryMemory(), Monitor(),Lenovo(),ComputerFacade(Display(),DVD(),Speaker()))

print(computer1.cost())

wireless_mouse = WirelessMouseDecorator(computer1)
print(wireless_mouse.cost())

wireless_speaker = WirelessSpeakerDecorator(computer1)
print(wireless_speaker.cost())
