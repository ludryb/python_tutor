s = input()

first = s.find("h")
last = s.rfind("h")

final = s[:first+1] + s[last-1:first:-1] + s[last:]
print(final)
