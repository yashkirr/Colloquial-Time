# Yashkir Ramsamy
# 1 July 2019
# Module for converting digital time format to a colloquial english time phrase


import datetime


numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve"]
timePhrases = ["five", "ten", "quarter", "twenty", "twenty-five", "half"]
context = ["o' clock", "past", "to"]



def getcurrentTime():
    """
    Summary
       Gets current time and returns a string
    ----------------------------------

    :return:
    -----------
        list
        returns H and M values in list of length 2


    """
    h = int('{:%H}'.format(datetime.datetime.now()))
    m = int('{:%M}'.format(datetime.datetime.now()))

    return [h, m]


def appropriateHours(h):
    """
    Summary
        Rounds hours to its 12hr form
    ----------------------------------
    :param m: int
        Value of hours
    ----------------------------------
    :return:
    -----------
        int
        12hr format hour value

    """
    if h > 12:
        h = h-12
    return h

def appropriateMinutes(m):
    """
    Summary
        Rounds minutes used for use of determining colloquial phrase
    ----------------------------------
    :param m: int
        Value of minutes
    ----------------------------------
    :return:
    -----------
        int
        rounded minute value

    """
    if m > 30:
        m = 60 - m
    return 5 * round((m/5))



def pastOrTo(m):
    """
    Summary
        Determine "past" or "to" or "o' clock"
    ----------------------------------
    :param m: int
        Value of minutes
    ----------------------------------
    :return:
    -----------
        str
        returns the context of time

    """
    if m == 0:
        return context[0]
    elif m < 31:
        return context[1]
    else:
        return context[2]



def returnTime(h, m):
    """
    Summary
        Returns H and M in a colloquial english phrase
    ----------------------------------
    :param h: int
        Value of hour
    :param m: int
        Value of hour
    ----------------------------------
    :return:
    -----------
        str
        returns colloquial english phrase

    """
    h = appropriateHours(h)
    m = appropriateMinutes(m)
    if (pastOrTo(m) == context[0]) or (m == 0): # check if time is currently o'clock or to be o' clock
        if m == 0:
            if h == 12: # if current time is 12:58+ , change to 1:00
                return numbers[0]+" "+pastOrTo(m)
            return numbers[h]+" "+pastOrTo(m) # if time is not 12:58+
        else:
            return numbers[h-1]+" "+pastOrTo(m)
    else:
        ptval = pastOrTo(m)
        if m == 5:
            index = 0
        elif m == 10:
            index = 1
        elif m == 15:
            index = 2
        elif m == 20:
            index = 3
        elif m == 25:
            index = 4
        else:
            index = 5
        phase = timePhrases[index]

        if ptval == "past":
            return phase+" "+ptval+" "+numbers[h-1]  # [h-1] to select current hour
        elif h == 12:
            return phase+" "+ptval+" "+numbers[0]    # [0] to select "twelve"
        else:
            return phase+" "+ptval+" "+numbers[h]    # [h] to select the coming hour


# example usage
def main():
    print(returnTime(5,23))


if __name__ == "__main__":
    main()
