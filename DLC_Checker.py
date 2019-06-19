#Version 2, Using set
import time
from colorama import init
from termcolor import colored, cprint
init()

print(colored("================================================================================================", 'cyan',attrs=['bold']))
print(colored('DLC_Checker by Tankerch v.190619', 'cyan',attrs=['bold']))
print(colored("================================================================================================", 'cyan',attrs=['bold']))
start = time.time()

#Open file
line_Real = set(line.strip().split(",")[0] for line in open('Update.lst'))
line_inform = [line.rstrip('\n').split(",") for line in open('ListDLC.lst')]
line_DLC = set(list(zip(*line_inform))[0])
line_informset = set(list(zip(*line_inform))[1])

#Searching with intersection and linear remove searching
count_p = set()
for x in line_DLC.intersection(line_Real):
    for y in line_inform:
        if x == y[0]:
            count_p.add(y[1])
            line_inform.remove(y)
            break

#Separating installed with not installed
count_n = line_informset.difference(count_p)

#Show time
print(colored('Already Installed:', 'cyan',attrs=['bold']))
for x in sorted(count_p):
    print(x)

#print("\nNot Installed:")
print(colored("\nNot Installed:", 'cyan',attrs=['bold']))
for x in sorted(count_n):
    print(x)

#Ending & Note
end = time.time()
print("\n\nElapsed time:", end-start)
text = input("Press Enter to end program")
