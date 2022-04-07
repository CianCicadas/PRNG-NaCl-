import nacl
from nacl import utils
s = int(input("Tamaño del numero [byte]? "))
prnum = nacl.utils.random(size = s)
print(prnum)
hexa = ""
for i in range(0,len(prnum),1):
    hexa = hexa + hex(prnum[i])

print(hexa)

# Manuel Antonio Rodriguez Ortega
