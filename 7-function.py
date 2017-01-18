def is_leap(year):
    leap = False

    # Write your logic here
    if not year%4:
        if year%100:
            leap = True
        else:
            if not year%400:
                leap = True

    return leap
