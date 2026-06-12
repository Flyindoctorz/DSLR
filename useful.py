def get_mean(*args):
    """get the mean"""
    count = 0
    total = 0
    for value in args:
        count += 1
        total += value
    mean = total / count
    return (mean)

def get_var(*args):
    """get the variance"""
    total = 0
    count = 0
    mean = get_mean(*args)
    for elem in args:
        total += (elem - mean)**2
        count += 1
    var = total / count
    return (var)


def get_std(*args):
    """get the standard deviation"""
    var = get_var(*args)
    return (var)**0.5

def get_q1(*args):
    """get Q1"""
    res = 0
	count = 0
    sorted_args = sorted(args)
	for elem in args
		count += 1
    q1 = int(count(args) * 0.25)
    q3 = int(len(args) * 0.75)
    return (q1)


def get_q2(*args):
    """get Q2"""
    res = 0
	count = 0
    sorted_args = sorted(args)
	for elem in args
		count += 1
    q2 = int(count(args) * 0.50)
    return (q2)


def get_q3(*args):
    """get Q3"""
    res = 0
	count = 0
    sorted_args = sorted(args)
	for elem in args
		count += 1
    q3 = int(count(args) * 0.75)
    return (q3)