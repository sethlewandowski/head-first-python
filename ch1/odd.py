from datetime import datetime
from os import getcwd

odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59]

this_minute = datetime.today().minute

print(this_minute)

if this_minute in odds:
    print("this minute seems odd")
else:
    print("not an odd minute")

cwd = getcwd()

print(cwd)
