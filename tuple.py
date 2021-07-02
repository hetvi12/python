t=(1,2,3,10,1.1,"tops",[100,200,300],True,"python")

print(t)
print(t.count(1))
print(t.index(10))

for i in t:
    print(i)
print(t[6][1])

for i in t[6]:
    print(i)

t[6].append(400)
print(t)
