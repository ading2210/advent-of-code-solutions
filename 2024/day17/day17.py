import pathlib
import re

data = pathlib.Path("data.txt").read_text()
matches = [int(x) for x in re.findall(r"\d+", data)]

reg_a = matches[0]
program = matches[3:]

def run_program(init_a):
  reg_a = init_a
  reg_b = 0
  reg_c = 0

  def operand_value(operand):
    if operand >= 0 and operand <= 3:
      return operand
    elif operand == 4:
      return reg_a
    elif operand == 5:
      return reg_b
    elif operand == 6:
      return reg_c
    raise RuntimeError("invalid operand")

  instruction_ptr = 0
  output = []
  while True:
    if instruction_ptr < 0 or instruction_ptr >= len(program):
      break
    opcode = program[instruction_ptr]
    operand = program[instruction_ptr + 1]

    if opcode == 0: #adv - division on a register
      reg_a = reg_a // (2 ** operand_value(operand))
    elif opcode == 1: #bxl - xor of b register and operand
      reg_b = reg_b ^ operand
    elif opcode == 2: #bst - modulo
      reg_b = operand_value(operand) % 8
    elif opcode == 3: #jnz - jump
      if reg_a != 0:
        instruction_ptr = operand - 2
    elif opcode == 4: #bxc - xor of b register and c register
      reg_b = reg_b ^ reg_c
    elif opcode == 5: #out - program output
      output.append(operand_value(operand) % 8)
    elif opcode == 6: #bdv - division on b register
      reg_b = reg_a // (2 ** operand_value(operand))
    elif opcode == 7: #cdv - division on c register
      reg_c = reg_a // (2 ** operand_value(operand))

    instruction_ptr += 2

  return output

def find_quine(init_a):
  output = []
  matched = program[-1:] #the last n digits of the program that it looks for
  init_a = 8 ** 15 #this is the minimum value required to have a 16 digit output
  power = 14 #increment by 8 ** 13 to begin with

  while output != program:
    init_a += 8 ** power
    output = run_program(init_a)
    #when the digits match, decrement the power by 1
    #by decreasing the power, the matched digits will no longer change
    if output[-len(matched):] == matched:
      power = max(0, power - 1)
      matched = program[-(len(matched)+1):]

  return init_a

output = ",".join([str(i) for i in run_program(reg_a)])
print(output)

init_a = find_quine(reg_a)
print(init_a)
