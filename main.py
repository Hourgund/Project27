from counter import Counter

c1 = Counter()
c2 = Counter()
c3 = Counter()

c1.increment()
c1.increment()

c2.increment()

c3.increment()
c3.increment()
c3.decrement()

print(c1)
print(c2)
print(c3)
