import re 

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)') # regex object - call compile and pattern looking for
mo = phoneNumRegex.search('My number is 508-843-2745') # search method to search string for pattern

groupie = input("what group do you want?")

if groupie == 1:
    bo = mo.group(1)
    print(bo)
elif groupie == 2:
    bo = mo.group(2)
    print(bo)
else:
    print("invalid entry")