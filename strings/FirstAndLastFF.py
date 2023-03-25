s = input()

if s.count ("f") >= 2:
    a = s.find("f")
    b = s.rfind("f")
    print (a, b)
elif s.count ("f") == 1:
    a = s.find ("f")
    print (a)