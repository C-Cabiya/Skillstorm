import ComputerComponent

class Computer:
    def __init__(self, owner:str,
                 cpu: ComputerComponent.CPU,
                 storage: ComputerComponent.Storage,
                 memory: ComputerComponent.Memory):
        self.owner = owner
        # Type checking requirement 
        if not isinstance(cpu, ComputerComponent.CPU):
            raise TypeError("Passed CPU parameter must be a CPU type")
        if not isinstance(storage, ComputerComponent.Storage):
            raise TypeError("Passed Storage parameter must be a Storage type")
        if not isinstance(memory, ComputerComponent.Memory):
            raise TypeError("Passed Memory parameter must be a Memory type")
        self.cpu = cpu
        self.storage = storage
        self.memory = memory
    
    def __str__(self):
        return f"""COMPUTER OBJECT INFORMATION:
        Owner: {self.owner}
        {self.cpu}
        {self.storage}
        {self.memory}"""
    
    def switch_parts(self, part):
        if not isinstance(part, ComputerComponent.ComputerComponent):
            raise TypeError("When switching components, the superclass of the "+
                            "components must be of the ComputerComponent type")
        if isinstance(part, ComputerComponent.CPU):
            self.cpu = part
        if isinstance(part, ComputerComponent.Storage):
            self.storage = part
        if isinstance(part, ComputerComponent.Memory):
            self.memory = part


    