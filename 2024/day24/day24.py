import pathlib
import itertools
import random

wires_str, gates_str = pathlib.Path("data.txt").read_text().split("\n\n")

class Gate:
  def __init__(self, gate_type, a_wire, b_wire, output):
    self.type = gate_type
    self.a_wire = a_wire
    self.b_wire = b_wire
    self.output = output
    self.inputs = (a_wire, b_wire)
  
  def __str__(self):
    return f"{self.a_wire} {self.type} {self.b_wire} -> {self.output}"

class Circuit:
  def __init__(self, wires, gates, x=None, y=None):
    self.wires = dict(wires)
    self.gates = list(gates)
    if x is not None:
      self.set_number("x", x)
    if y is not None:
      self.set_number("y", y)

    self.simulate_circuit()
    self.output = self.get_number("z")

  def next_gate(self):
    for gate in self.gates:
      if gate.a_wire in self.wires and gate.b_wire in self.wires:
        self.gates.remove(gate)
        return gate

  def process_gate(self, gate):
    a = self.wires[gate.a_wire]
    b = self.wires[gate.b_wire]
    if gate.type == "AND":
      return a & b
    elif gate.type == "XOR":
      return a ^ b
    elif gate.type == "OR":
      return a | b

  def simulate_circuit(self):
    gate = self.next_gate()
    while gate:
      self.wires[gate.output] = self.process_gate(gate)
      gate = self.next_gate()

  def get_number(self, prefix):
    nums = {}
    for wire, value in self.wires.items():
      if not wire.startswith(prefix):
        continue
      power = int(wire.lstrip(prefix))
      nums[power] = value

    num = 0
    for bit, value in nums.items():
      num |= value << bit
    return num
  
  def set_number(self, prefix, num):
    for bit in range(0, 46):
      wire = f"{prefix}{bit}"
      self.wires[wire] = num & 1
      num >>= 1

wires = {}
for line in wires_str.splitlines():
  wire, value = line.split(": ")
  wires[wire] = int(value)
gates = []
for line in gates_str.splitlines():
  a_wire, gate_type, b_wire, _, output = line.split()
  gates.append(Gate(gate_type, a_wire, b_wire, output))

circuit = Circuit(wires, gates)
print(circuit.output)

#thanks to this guy on reddit for the algorithm i used
#https://www.reddit.com/r/adventofcode/comments/1hl698z/comment/m3llouk/

input_of_or = set(itertools.chain(*(g.inputs for g in gates if g.type == "OR")))
output_of_and = set((g.output for g in gates if g.type == "AND" and g.a_wire != "x00"))

c1 = set(g.output for g in gates 
  if g.output[0] == "z" and g.type != "XOR" and g.output != "z45")
c2 = set(g.output for g in gates 
  if g.type == "XOR" and g.a_wire[0] not in "xy" and g.output[0] != "z")
c3 = input_of_or ^ output_of_and

wrong_outputs = c1 | c2 | c3
print(",".join(sorted(wrong_outputs)))