s = input ()

if s.count("f") >= 2:
    first = s.find("f") + 1
    second = s[first:].find("f") + first
    print (second)
elif s.count("f") == 1:
    print (-1)
else:
    print (-2)
    