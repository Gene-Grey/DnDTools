import warnings

def addTime(time_adds, dateArray):
    i = 1

    while time_adds != []:
        if type(time_adds[0]) == tuple:
            print("Turn", i, "start :", dateArray)

            if type(time_adds[0][0]) == int:
                if type(time_adds[0][1]) == int:
                    dateArray[time_adds[0][0]] = \
                    dateArray[time_adds[0][0]] + time_adds[0][1]

                    if dateArray[6] >= 60:
                        dateArray[5] += dateArray[6] // 60
                        dateArray[6] = dateArray[6] % 60

                    if dateArray[5] >= 60:
                        dateArray[4] += dateArray[5] // 60
                        dateArray[5] = dateArray[5] % 60

                    if dateArray[4] >= 24:
                        dateArray[3] += dateArray[4] // 24
                        dateArray[4] = dateArray[4] % 24

                    if dateArray[3] > 28:
                        dateArray[2] += dateArray[4] // 28
                        dateArray[3] = dateArray[3] % 28

                    if dateArray[2] > 12:
                        dateArray[1] += dateArray[2] // 12
                        dateArray[2] = dateArray[2] % 12

                else:
                    pass
                    warnings.warn("Second value in tuple not int, skipped")
            else:
                pass
                warnings.warn("First value in tuple not int, skipped")
        else:
            pass
            warnings.warn("Non tuple element given, skipped")

        del time_adds[0]
        print("Turn", i, "end :", dateArray, "\n")
        i += 1

def main():
    dateArray = [3, 1970, 7, 25, 12, 6, 9]
    
    addTimeQueue = []
    addTime(addTimeQueue, dateArray)

    print(dateArray[0], "-", dateArray[1], "/", dateArray[2], "/", \
        dateArray[3], " ", dateArray[4], ":", f'{dateArray[5]:02}',\
        ":", f'{dateArray[6]:02}', sep="")

if __name__ == "__main__":
    main()
