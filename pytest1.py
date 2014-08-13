
def double_it(num):
    print "Input: %d  Doubled: %d" % (num, 2 * num)


def triple_it(num):
    print "Input: %d  Tripled: %d" % (num, 3 * num)


def bigger_it(num):
    factor = 9876543210123456789
    print "Input: %d  Bigger: %d" % (num, factor * num)


def number_to_weekday(num):
    weekday = ''
    if num == 1:
        weekday = 'Sunday'
    elif num == 2:
        weekday = 'Monday'
    elif num == 3:
        weekday = 'Tuesday'
    elif num == 4:
        weekday = 'Wednesday'
    elif num == 5:
        weekday = 'Thursday'
    elif num == 6:
        weekday = 'Friday'
    elif num == 7:
        weekday = 'Saturday'
    else:
        weekday = 'Baxterday'
        raise Exception('Hey! That is not a weekday!')

    return weekday


if __name__ == "__main__":
    print "testing double"
    double_it(10)
    double_it(500)


