
def double_it(num):
    print "Input: %d  Doubled: %d" % (num, 2 * num)


def triple_it(num):
    print "Input: %d  Tripled: %d" % (num, 3 * num)


def bigger_it(num):
    factor = 9876543210123456789
    print "Input: %d  Bigger: %d" % (num, factor * num)


def number_to_weekday(num):
    if num < 0:
        num = 0
        print 'Negative changed to zero'
    elif num == 0:
        print 'Zero'
    elif num == 1:
        print 'Single'
    else:
        print 'More'


if __name__ == "__main__":
    print "testing double"
    double_it(10)
    double_it(500)

