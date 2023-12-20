import os
from readchar import readkey, key
i=0
while True:
    k = readkey()
    if k == "n":
         os.system('cls' if os.name=='nt' else 'clear')
         print(i)
         i += 1
         if i == 51:
             break
         else:
             continue
    else:
        continue