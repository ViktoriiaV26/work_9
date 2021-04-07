a = set()
print(a)
b = {10, 32, 54, 28, 10, 3, 18, 28}
#all
print("all:", all(b))
print("all:", all(a))

#any
print("any:", any(b))
print("any:", any(a))

# len
print("len:", len(b))

#sum
print("sum:", sum(b))

#min/max
print("min:", min(b))
print("max:", max(b))

#sorted
print("sorted:", sorted(b))

# enumerate
d = {2, 3, 4, 6, 1, 7}
for i in enumerate(d, 10):
    print(i)