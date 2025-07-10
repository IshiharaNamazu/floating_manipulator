l = [3.5, 0.25, 2.5, 2.5, 0.5, 0.25, 0.25]

def length(l, size):
    print("i:", size)
    print(sum(l[0:size+1]) - (l[0]+l[size])/2)
    
def joint(l, index):
    if(index >= len(l)-1):
        return
    print("j:" + str(index) + ":" + str(-l[index+1]/2))
    
print("len:")
for i in range(0, len(l)):
    length(l, i)

print("joint:")
for i in range(0, len(l)):
    joint(l, i)