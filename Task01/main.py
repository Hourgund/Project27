from counter02 import Counter

c1 = Counter(6)
c2 = Counter(6)
c3 = Counter(6)

c1.increment()
c1.increment()

c2.increment()

c3.increment()
c3.increment()
c3.decrement()

# c1.reset()

c1.count = 10
n = c1.count
del c1.count

print(c1.count)
print(c2.count)
print(c3.count)
