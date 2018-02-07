import random
even_a = []
a = [random.randrange(1,1000) for i in range(1,50)]
print(sorted(a))
even_a = [b for b in a if b%2 == 0]
print(sorted(even_a))


