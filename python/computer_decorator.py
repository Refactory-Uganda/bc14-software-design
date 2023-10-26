from abc import ABC, abstractmethod

# Step 1: Create an interface (Computer.py)
class Computer(ABC):
    @abstractmethod
    def peripheral(self) -> str:
        pass

    @abstractmethod
    def cost(self) -> int:
        pass

# Step 2: Create concrete classes implementing the interface, e.g., Mouse, Printer, Speaker, Keyboard, etc.
class Mouse(Computer):
    def peripheral(self) -> str:
        return "Mouse"

    def cost(self) -> int:
        return 50  # Example cost for a mouse

class Printer(Computer):
    def peripheral(self) -> str:
        return "Printer"

    def cost(self) -> int:
        return 100  # Example cost for a printer

class Speaker(Computer):
    def peripheral(self) -> str:
        return "Speaker"

    def cost(self) -> int:
        return 150  # Example cost for a speaker

class Keyboard(Computer):
    def peripheral(self) -> str:
        return "Keyboard"

    def cost(self) -> int:
        return 70  # Example cost for a keyboard

# Step 3: Create an abstract decorator class for implementing the Computer interface.
class ComputerDecorator(Computer, ABC):
    def __init__(self, decorated_computer: Computer):
        self.decorated_computer = decorated_computer

    @abstractmethod
    def peripheral(self) -> str:
        pass

    @abstractmethod
    def cost(self) -> int:
        pass

# Step 4: Create concrete decorator classes extending the ComputerDecorator class.
class WirelessDecorator(ComputerDecorator):
    def peripheral(self) -> str:
        return self.decorated_computer.peripheral()

    def cost(self) -> int:
        return self.decorated_computer.cost()

class WirelessMouseDecorator(WirelessDecorator):
    def peripheral(self) -> str:
        return f"Wireless {self.decorated_computer.peripheral()} Mouse"

    def cost(self) -> int:
        return self.decorated_computer.cost() + 10  # Example: Add 10 to the cost

class WirelessSpeakerDecorator(WirelessDecorator):
    def peripheral(self) -> str:
        return f"Wireless {self.decorated_computer.peripheral()} Speaker"

    def cost(self) -> int:
        return self.decorated_computer.cost() + 20  # Example: Add 20 to the cost

# Step 5: Use the decorators to decorate Computer objects.
mouse = Mouse()
speaker = Speaker()

wireless_mouse = WirelessMouseDecorator(mouse)
wireless_speaker = WirelessSpeakerDecorator(speaker)

# Step 6: Verify the output, including the peripheral and cost.
print("Mouse with a wire")
print(f"Peripheral: {mouse.peripheral()}")
print(f"Cost: ${mouse.cost()}")

print("\nMouse without a wire")
print(f"Peripheral: {wireless_mouse.peripheral()}")
print(f"Cost: ${wireless_mouse.cost()}")

print("\nSpeaker with a wire")
print(f"Peripheral: {speaker.peripheral()}")
print(f"Cost: ${speaker.cost()}")

print("\nSpeaker without a wire")
print(f"Peripheral: {wireless_speaker.peripheral()}")
print(f"Cost: ${wireless_speaker.cost()}")
