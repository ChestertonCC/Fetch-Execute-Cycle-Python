# Activity (Python Code)
# Can you replicate the fetch execute cycle within python?
# At each stage you should show what is present in all the registers at that time
# You will need a variable to store what stage the cycle is at.
# The user can choose to go forward or backward in the cycle as they wish

# Task at https://new.edmodo.com/post/705828318

# Create the registers
memory = [0] * 100 # Initialize 100 memory locations
pc = 0 # The program counter starts at 0
cir = None # There is no current instruction
mar = None # There is nothing in the memory address register
mdr = None # Nothing here either

class ArithmeticLogicUnit:
  def __init__(self):
    self.accumulator = 0
    self.temporaryDataStore
  def prepare(self):
    self.temporaryDataStore = None
  def add(self, address):
    self.temporaryDataStore = self.accumulator
    getMemoryAddress(address)
    self.accumulator = self.accumulator + self.temporaryDataStore
    print("Accumulator value added to value of address "+str(address)+" and written to the accumulator")

alu = ArithmeticLogicUnit()

def writeToAccumulator(value):
  self.accumulator = value
  print(str(value) + " written to accumulator")

def getMemoryAddress(address):
  print("Getting the data at memory address "+str(address)+" and writing it to the accumulator")
  writeToAccumulator(memory[address])
  
def output(out):
  print("output: "+str(out))

def doCycle():
  
# Set some memory addresses
memory[0] = "LOAD 10"
memory[1] = "ADD 11"
memory[2] = "OUT"
memory[3] = "HLT"
memory[10] = 11
memory[11] = 22
