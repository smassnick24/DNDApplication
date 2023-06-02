# currently empty
mod = "-3"

prog = "+2"

total = int(mod) + int(prog)

formatted = "+" + str(total) if total >= 0 else str(total)

print(formatted)