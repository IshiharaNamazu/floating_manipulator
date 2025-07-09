l = [3.5, 0.25, 2.5, 2.5, 0.5, 0.25, 0.25]

def length(l, size):
    print("size:", size)
    print(sum(l[0:size+1]) - (l[0]+l[size])/2)
    
for i in range(0, len(l)):
    length(l, i)