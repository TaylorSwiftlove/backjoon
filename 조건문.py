# 1330 번

i, j = input().split(" ")
i, j = int(i), int(j)
if i > j :
    print(">")
if i < j :
    print("<")
if i == j :
    print("==")

# 9498 번

i = int(input())
if i <= 100 and i >= 90:
    print("A")
if i <= 89 and i >= 80:
    print("B")
if i <= 79 and i >= 70:
    print("C")
if i <= 69 and i >= 60:
    print("D")
if i < 60:
    print("F")

# 2753 번

i = int(input())
if i % 4==0 and i % 100!=0 or i % 400==0 :
    print(1)
else :
    print(0)

# 14681 번
x = int(input())
y = int(input())

if x > 0 and y > 0 :
    print(1)
    
if x < 0 and y > 0 :
    print(2)

if x < 0 and y < 0 :
    print(3)

if x > 0 and y < 0 :
    print(4)

# 2884 번

h, m = input().split(" ")
h, m = int(h), int(m)

if m < 45 :
    m = m - 45 + 60
    if h == 0 :
        h = 23
    elif h > 0 :
        h -= 1
elif m >= 45 :
    m -= 45

print(h, m)