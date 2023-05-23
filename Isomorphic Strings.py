s = "foo"
t = "bar"

ans = True

map = {}

if len(s) != len(t):
    print(False)

for index, letter in enumerate(s):
    if t[index] in map.values():
        if letter not in map:
            ans = False
    if letter in map:
        if map[letter] == t[index]:
            map[letter] = t[index]
        else:
            ans = False
    map[letter] = t[index]

print(ans)



