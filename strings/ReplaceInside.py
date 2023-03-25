s = input()

first = s.find("h")
last = s.rfind("h")

final = s[:first + 1] + s[first + 1:last].replace("h", "H") + s[last:]
print(final)
