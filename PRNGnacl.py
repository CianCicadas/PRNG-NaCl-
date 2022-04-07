import nacl
from nacl import utils
prnum = nacl.utils.random(size = 32)
print(prnum)
hexa = ""
for i in range(0,len(prnum),1):
    hexa = hexa + hex(prnum[i])

print(hexa)

# Manuel Antonio Rodriguez Ortega
