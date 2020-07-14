sum = 0
for i in range(1, 101):
    sum = sum+i
print(sum)

"""1-100的和"""
a = 0
for s in range(1, 101):
    a += s
print("和为：%s" % a)

"""1-100偶数和奇数的和"""
b = 0
c = 0
for f in range(1, 101):
    if f % 2 == 0:
        b += f
    else:
        c += f
print("偶数和：{0}".format(b))
print("奇数和：{0}".format(c))

for d in range(10):
    for j in range(0, d):
        print(end=" ")

    for j in range(1, 10):
        print('@', end=" ")
    print("")


