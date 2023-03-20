class CPU:
    def freeze(self):
        print("Freezing CPU")
    
    def jump(self, position):
        print(f"Jumping to position {position}")
    
    def execute(self):
        print("Executing CPU instructions")

class Memory:
    def load(self, position, data):
        print(f"Loading data {data} into memory position {position}")

class HardDrive:
    def read(self, sector, size):
        return f"{size} bytes of data from sector {sector}"

class ComputerFacade:
    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.hard_drive = HardDrive()
    
    def start(self):
        self.cpu.freeze()
        self.memory.load(0, self.hard_drive.read(0, 1024))
        self.cpu.jump(0)
        self.cpu.execute()

computer = ComputerFacade()
computer.start()
