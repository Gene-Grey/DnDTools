import warnings

def date(self, parameter_list):
    """
    docstring
    """
    def __init__(self, era=1, year=0, month=1, day=1, hour=1,
                    minute=0, second=0, add_time_queue=[]):
        self.era = era
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.second = second
        self.add_time_queue = add_time_queue

    def get_era(self):
        return self.era

    def set_era(self, era):
        self.era = era
        
    def del_era(self):
        del self.era

    def get_year(self):
        return self.year

    def set_year(self, year):
        self.year = year

    def del_year(self):
        del self.year

    def get_month(self):
        return self.month

    def set_month(self, month):
        self.month = month

    def del_month(self):
        del self.month

    def get_day(self):
        return self.day

    def set_day(self, day):
        self.day = day

    def del_day(self):
        del self.day

    def get_hour(self):
        return self.hour

    def set_hour(self, hour):
        self.hour = hour

    def del_hour(self):
        del self.hour

    def get_minute(self):
        return self.minute

    def set_minute(self, minute):
        self.minute = minute

    def del_minute(self):
        del self.minute

    def get_second(self):
        return self.second

    def set_second(self, second):
        self.second = second

    def del_second(self):
        del self.second

    def release_queue(self, dateArray):
        while self.add_time_queue != []:
            if type(self.add_time_queue[0]) == tuple:
                if type(self.add_time_queue[0][0]) == int:
                    if type(self.add_time_queue[0][1]) == int:
                        dateArray[self.add_time_queue[0][0]] = \
                        dateArray[self.add_time_queue[0][0]] \
                        + self.add_time_queue[0][1]

                        if self.second >= 60:
                            self.minute += self.second // 60
                            self.second = self.second % 60

                        if self.minute >= 60:
                            self.hour += self.minute // 60
                            self.minute = self.minute % 60

                        if self.hour >= 24:
                            self.day += self.hour // 24
                            self.hour = self.hour % 24

                        if self.day > 28:
                            self.month += self.hour // 28
                            self.day = self.day % 28

                        if self.month > 12:
                            self.year += self.month // 12
                            self.month = self.month % 12

                    else:
                        pass
                        warnings.warn("Second value in tuple not int, skipped")
                else:
                    pass
                    warnings.warn("First value in tuple not int, skipped")
            else:
                pass
                warnings.warn("Non tuple element given, skipped")

            del self.add_time_queue[0]

    def displayDate(self):
        print(self.era, "-", self.year, "/", self.month, "/", \
                self.day, " ", self.hour, ":", f'{self.minute:02}',\
                ":", f'{self.second:02}', sep="")

def main():
    return None

if __name__ == "__main__":
    main()
