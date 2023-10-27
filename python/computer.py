from bluetooth import BluetoothDevice
from input_devices import InputDevice
from memory import Memory
from output_devices import OutputDevice
from processors import Processor
from wifi import WiFiDevice
from abc import ABC, abstractmethod

from brands import Brand
from facade import ComputerFacade

class Computer:
    """
    The responsibility of this Computer class is to control other Peripherals.
    And control is the only reason why Computer would change.
    """

    def __init__(self, input_device: InputDevice, processor: Processor, memory: Memory, output_device: OutputDevice,brand:Brand,movie:ComputerFacade):
        self._input_device = input_device
        self._processor = processor
        self._memory = memory
        self._output_device = output_device
        self._brand = brand
        self._movie = movie


    @abstractmethod
    def cost(self) -> int:
        return 500

    def set_movie_system(self,movie:ComputerFacade):
        self._brand.set_movie_system()

    def get_movie_system(self):
        return self._brand.get_movie_system()
    
    def input(self):
        self._input_device.input()

    def set_input_device(self, input_device: InputDevice):
        self._input_device = input_device

    def get_input_device(self):
        return self._input_device

    def process(self, data: any, instruction_id: int) -> bool:
        return self._processor.process(data, instruction_id)

    def set_memory(self, memory: Memory):
        self._memory = memory

    def get_memory(self):
        return self._memory

    def store(self, data: any, key: str):
        return self._memory.store(data, key)

    def retrieve(self, key: str):
        return self._memory.retrieve(key)

    def set_processor(self, processor: Processor):
        self._processor = processor

    def get_processor(self):
        return self._processor

    def output(self, data: any):
        self._output_device.output(data)

    def set_output_device(self, output_device: OutputDevice):
        self._output_device = output_device

    def get_output_device(self):
        return self._output_device
    
    def boot(self):
        self._brand.boot()
    


class Desktop(Computer):
    pass
class Laptop(Computer):
    pass
 
class Walltop(Computer):
    pass

# Usage





