# 2557 번
print("Hello World!")

# 10718 번
print("강한친구 대한육군")
print("강한친구 대한육군")

# 10171 번
print("\\    /\\")
print(" )  ( ')")
print("(  /  )")
print(" \\(__)|")

# 10172 번
print("|\\_/|")
print("|q p|   /}")
print('( 0 )"""\\')
print('|"^"`    |')
print("||_/=\\\\__|")

# 1000 번
A, B = input().split()
print(int(A) + int(B))

# 1001 번
A, B = input().split()
print(int(A)-int(B))

# 10998 번
A, B = input().split()
print(int(A)*int(B))

# 1008 번
A, B = input().split()
print(int(A)/int(B))

# 10869 번
A, B = input().split()
A = int(A)
B = int(B)
print(A+B)
print(A-B)
print(A*B)
print(A//B)
print(A%B)

# 10430 번
A, B, C = input().split(" ")
A, B, C = int(A), int(B), int(C)
print((A+B)%C)
print(((A%C)+(B%C))%C)
print((A*B)%C)
print(((A%C)*B%C)%C)

# 2588 번
a = int(input())
i = int(input())

b = i // 100
c = i % 100 // 10
d = i % 10
print(a*d)
print(a*c)
print(a*b)
print(a*d+a*c*10+a*b*100)