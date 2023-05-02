from counter import Counter

c1 = Counter(6)
c2 = Counter(6)
c3 = Counter(6)

c1.increment()
c1.increment()

c2.increment()

c3.increment()
c3.increment()
c3.decrement()

c1.reset()

print(c1)
print(c2)
print(c3)
