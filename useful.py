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
    count = 0
    sorted_args = sorted(args)
    for elem in args:
        count += 1
    q1 = int(count * 0.25)
    return (sorted_args[q1])


def get_q2(*args):
    """get Q2"""
    count = 0
    sorted_args = sorted(args)
    for elem in args:
        count += 1
    q2 = int(count * 0.50)
    return (sorted_args[q2])

def get_q3(*args):
    """get Q3"""
    count = 0
    sorted_args = sorted(args)
    for elem in args:
        count += 1
    Q3 = int(count * 0.75)
    return (sorted_args[Q3])

def get_min(*args):
    """get min"""
    res = args[0]
    for elem in args:
        if elem < res:
            res = elem
    return (res)

def get_max(*args):
    """get max"""
    res = args[0]
    for elem in args:
        if elem > res:
            res = elem
    return (res)

def get_cov(x, y):
    """get covariance"""
    total = 0
    count = 0
    meanx = get_mean(*x)
    meany = get_mean(*y)
    for xi, yi in zip(x, y):
        total += (xi - meanx) * (yi - meany)
        count +=1
    return (total / count)

def get_corr(x, y):
    """get correlation"""
    corr = get_cov(x, y) / (get_std(*x) * get_std(*y))
    return (corr)

def main():
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]
    res = get_corr(x, y)
    print(f"{res}")


if __name__ == "__main__":
    main()