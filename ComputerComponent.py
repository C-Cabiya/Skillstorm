class ComputerComponent:
    def __init__(self, serial_number, manufacterer, model):
        self.serial_number = serial_number
        self.manufacterer = manufacterer
        self.model = model
    
    def __str__(self):
        return f"Component Model: {self.model} Manufactered By: {self.manufacterer} Serial No.: {self.serial_number}"

class CPU(ComputerComponent):
    def __init__(self, serial_number:int, manufacterer:str, model:str, cores:int,
                 clock_speed:int, generation:int):
        super().__init__(serial_number, manufacterer, model)
        self.cores = cores
        self.clock_speed = clock_speed
        self.generation = generation
    
    def __str__(self):
        return f"""CPU Component: \n{super().__str__()} 
        Cores: {self.cores}
        Clock Time: {self.clock_speed}
        Generation: {self.generation}"""
    
class Storage(ComputerComponent):
    def __init__(self, serial_number:int, manufacterer:str, model:str,
                 storage_type:str, size:int):
        super().__init__(serial_number, manufacterer, model)
        self.storage_type = storage_type
        self.size = size
    def __str__(self):
        return f"""Storage Component: \n{super().__str__()} 
        Storage Type: {self.storage_type}
        Size: {self.size}"""

# Differentiating between SSDs and HDDs to demonstrate polymorphism
class SSD(Storage):
    def __init__ (self, serial_number:int, manufacterer:str, model:str,
                 storage_type:int, size:int):
        super().__init__(serial_number, manufacterer, model,
                 storage_type, size)
    def __str__ (self):
        return f"SSD Type {super().__str__()}"

class HDD(Storage):
    def __init__ (self, serial_number:int, manufacterer:str, model:str,
                 storage_type:int, size:int):
        super().__init__(serial_number, manufacterer, model,
                 storage_type, size)
    def __str__ (self):
        return f"HDD Type {super().__str__()}"

class Memory(ComputerComponent):
    def __init__(self, serial_number:int, manufacterer:str, model:str,
                 capacity:int):
        super().__init__(serial_number, manufacterer, model)
        self.capacity = capacity
    def __str__(self):
        return f"""Memory Component: \n{super().__str__()} 
        Capacity: {self.capacity}"""