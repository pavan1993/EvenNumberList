import random
even_a = []
a = [random.randrange(1,1000) for i in range(1,50)]
print(a)
for x in a:
    if x % 2 == 0:
        even_a.append(x)
print(even_a)



