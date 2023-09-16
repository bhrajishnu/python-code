#! /home/codespace/.python/current/bin/python

while True:
    try:
        x = int(input("whats the value of x?-"))
    except ValueError:
        print("Type a number not a word")

    else:
        break
while True:
    try:
        y = int(input("whats the value of x?-"))
    except ValueError:
        print("Type a number not a word")

    else:
        break
u = (input("whats your name?-"))

h = (u)
print("plz use the follwing + * / -")
t = (input("whats the symble?-"))
if t == "+":
    z = x + y
    print(f"{x} {t} {y}=", z)

    print(f"{h}")

if t == "*":
    z = x * y
    print(f"{x}{t}{y}=", z)

    print(f"{h}")
elif t == "/":
    z = x + y
    print(f"{x}{t}{y}=", z)

    print(f"{h}")
elif t == "-":
    z = x + y
    print(f"{x}{t}{y}=", z)

    print(f"{h}")