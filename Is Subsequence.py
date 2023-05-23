s = "abc"
t = "ahbgdc"

isSubsequence = True

tempCount = 0


for i in range(len(t)):
    tempLetter = s[tempCount]
    if t[i] == tempLetter:
        tempCount += 1
if tempCount != len(s):
    isSubsequence = False
print(isSubsequence)





