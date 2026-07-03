#This is a main module to test machine.py
#Author: Gal ELhiani
#Tester: Meytar

from datetime import datetime
from machine import Machine, MachineType1, MachineType2

t1 = datetime(2026, 1, 1, 12, 0)
t2 = datetime(2026, 1, 1, 12, 1)
t3 = datetime(2026, 1, 1, 12, 2)
t4 = datetime(2026, 1, 1, 12, 3)

#State 1
a = MachineType1("Type 1", "a")
b = MachineType1("Type 1", "b")
c = MachineType1("Type 1", "c")
d = MachineType2("Type 2", "d")

for m in (a, b, c, d):
    m.start_machine(t1)

#State 2
e = MachineType2("Type 2", "e")
e.start_machine(t2)

#State 3
b.stop_machine(t3)

#State 4
total_cost = Machine.get_total_price(t4)

print(Machine.tracking_table)
print(f"Success! Calculated Total is ${total_cost}.")
