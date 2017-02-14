d = 10
b = 0
c = 0
o = 10
y = 0
g = 10
u = 0
h = 0
l = 0 
for l in range(0, 3):
    while c == 0:
        while b == 0:
            for i in range(0,a):
                print(" "*a + "x"*i)
                a -= 1
                i += 1
            b += 1
        else:
            for j in range(0, d):
                print(" "*j + "@"*d)
                j += 1
                d -= 1
        c += 1
    else:
        while y == 0:
            for t in range(0, o):
                print(" "*j + "x"*t + " "*o)
                o -= 1
                t += 1
            y += 1
        else:
            for f in range(0, g):
                print(" "*j + "x"*g + " "*f)
                f += 1
                g -= 1
    l += 1
