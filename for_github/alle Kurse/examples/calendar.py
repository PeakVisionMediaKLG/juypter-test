""" 
The class Calender implements a calendar.
A calendar dat can be set to an arbitrary date or it can be advanced to the next day. 
"""

class Calendar(object):

    months = (31,28,31,30,31,30,31,31,30,31,30,31)

    @staticmethod
    def leapyear(year):
        """ 
        The method leapyear returns True, if year is a leap year,
        else False.
        """

        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    leap_year = True
                else:
                    leap_year = False
            else:
                leap_year = True
        else:
            leap_year = False

        return leap_year


    def __init__(self, d, m, y):
        """
        d, m, y have to be integer values and year has to be 
        a four digit year number
        """

        self.set_Calendar(d,m,y)


    def set_Calendar(self, d, m, y):
        """
        d, m, y have to be integer values and year has to be 
        a four digit year number
        """

        if type(d) == int and type(m) == int and type(y) == int:
            self.__days = d
            self.__months = m
            self.__years = y
        else:
            raise TypeError("d, m, y have to be integers!")


    def __str__(self):
        return "{0:02d}.{1:02d}.{2:4d}".format(self.__days,
                                               self.__months,
                                               self.__years)


    def advance(self):
        """
        sets the date to the next day, considering leap years.
        """

        max_days = Calendar.months[self.__months-1]
        if self.__months == 2 and Calendar.leapyear(self.__years):
            max_days += 1
        if self.__days == max_days:
            self.__days= 1
            if self.__months == 12:
                self.__months = 1
                self.__years += 1
            else:
                self.__months += 1
        else:
            self.__days += 1


if __name__ == "__main__":
    x = Calendar(31,12,2012)
    print(x, end=" ")
    x.advance()
    print("after advance: ", x)
    print("2012 was a leap year:")
    x = Calendar(28,2,2012)
    print(x, end=" ")
    x.advance()
    print("after advance: ", x)
    x = Calendar(28,2,2013)
    print(x, end=" ")
    x.advance()
    print("after advance: ", x)
    print("1900 was not a leap year, as it is divisible by 100, but not by 400")
    x = Calendar(28,2,1900)
    print(x, end=" ")
    x.advance()
    print("nach advance: ", x)
    print("2000 war ein leap_year, weil die Zahl durch 400 teilbar ist:")
    x = Calendar(28,2,2000)
    print(x, end=" ")
    x.advance()
    print("nach advance: ", x)
