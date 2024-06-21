import ComputerComponent
import Computer

cpu = ComputerComponent.CPU(1234, "We_Make_Cores", "OkayCPU", 4, 2.5, 1)
ssd = ComputerComponent.SSD(1111, "Intel", "DC P1600X", "SSD", 58)
hdd = ComputerComponent.SSD(98765, "Western Digital", "WD20EZBX", "HDD", 2000)
memory = ComputerComponent.Memory(1,2,3,4)

# Making the computer with the ssd, to be switched later with a hdd
#   to demonstrate polymorphism
comp = Computer.Computer(1,cpu,ssd,memory)

# Outputting Computer information
print(comp)

# Testing the switch mechanic 
comp.switch_parts(hdd)

# Outputting again to demonstrate proper part switching mechanic
print(comp)