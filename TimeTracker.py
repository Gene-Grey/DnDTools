import time

switchOn = True
dateArray = [3, 1970, 7, 25, 12, 6, 9]

while switchOn == True:
    print(dateArray[0], "-", dateArray[1], "/", dateArray[2], "/", \
        dateArray[3], " ", dateArray[4], ":", f'{dateArray[5]:02}', \
        ":", f'{dateArray[6]:02}', sep="")
    switchOn = False
