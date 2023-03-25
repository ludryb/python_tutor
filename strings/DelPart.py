s = input()

first = s.find("h")
last = s.rfind("h")

final = s[:first] + s[last+1:]
print(final)