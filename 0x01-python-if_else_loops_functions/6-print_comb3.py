#!/usr/bin/python3
#!/usr/bin/python3
for a in range(10):
    for b in range(10):
        if a == 8 and b == 9:
            print("{}{}".format(a, b))
        elif b > a:
            print("{}{}, ".format(a, b), end="")
