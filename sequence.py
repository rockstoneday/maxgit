n = int(input("Enter the length of the sequence: ")) # Do not change this line
tala1 = 3
tala2 = 2
tala3 = 1


print(tala3)
print(tala2)
print(tala1)

for i in range(n-3):
    nextnum = tala1 + tala2 + tala3
    tala3 = tala2
    tala2 = tala1
    tala1 = nextnum
    
    print (nextnum)
