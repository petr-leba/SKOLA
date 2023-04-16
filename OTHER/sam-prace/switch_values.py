import time

start = time.time_ns()
for _ in range(10000):
    a = 10
    b = 12
    temp = a
    a = b
    b = temp
end = time.time_ns()
print(end - start, " ns - pomocná proměnná 10000x")

start = time.time_ns()
for _ in range(10000):
    a = 10
    b = 12
    a, b = b, a
end = time.time_ns()
print(end - start, " ns - prohození proměnných 10000x")

start = time.time_ns()
for _ in range(10000):
    a = 10
    b = 12
    a = a + b
    b = a - b
    a = a - b
end = time.time_ns()
print(end - start, " ns - sčítáním a odčítáním 10000x")

start = time.time_ns()
for _ in range(10000):
    a = 10
    b = 12
    a = a ^ b
    b = a ^ b
    a = a ^ b
end = time.time_ns()
print(end - start, " ns - XORem 10000x")  

input()