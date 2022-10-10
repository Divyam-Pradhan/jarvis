#Program to check if a string is a subset of another string 


def check_subset(s1, s2):
    flag = True
    for char in s1:
        if char in s2:
            continue
        else:
            flag = False
    return flag


s1 = "Abc"
s2 = "Abcaradaba"
flag = check_subset(s1, s2)
print("s1 is a subset of s2:", flag)

s1 = "abbz"
s2 = "Hacktoberfest"
flag = check_subset(s1, s2)
print("s1 is a subset of s2:", flag)
