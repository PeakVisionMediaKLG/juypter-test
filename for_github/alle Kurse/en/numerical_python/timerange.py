def trange(start, stop, step):
    """ 
    trange(stop) -> time as a 3-tuple (hours, minutes, seconds)
    trange(start, stop[, step]) -> time tuple

    start: time tuple (hours, minutes, seconds)
    stop: time tuple
    step: time tuple

    returns a sequence of time tuples from start to stop incremented by step
    """        

    current = list(start)
    while current < list(stop):
        yield tuple(current)
        seconds = step[2] + current[2]
        min_borrow = 0
        hours_borrow = 0
        if seconds < 60:
            current[2] = seconds
        else:
            current[2] = seconds - 60
            min_borrow = 1
        minutes = step[1] + current[1] + min_borrow
        if minutes < 60:
            current[1] = minutes 
        else:
            current[1] = minutes - 60
            hours_borrow = 1
        hours = step[0] + current[0] + hours_borrow
        if hours < 24:
            current[0] = hours 
        else:
            current[0] = hours -24
            
for time in trange((10, 10, 10), (16, 50, 15), (0, 12, 5) ):
    print(time)
            

    
