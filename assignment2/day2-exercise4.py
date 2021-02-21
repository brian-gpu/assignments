import sys

def find_payments(p, r, duration):
    initial_p = p
    m = 0
    base_month_m = p/duration

    offset = 0
    count = 0
    total_interest_new = 0
    total_interest_old = sys.maxsize

    # Takes the total remaining interest, averages it, and adds
    # it to the base montly repayment -> assuming no interest.
    # Repeats until the variation in interest is less than .0001
    while abs(total_interest_old - total_interest_new) > 0.0001:
        month = 0
        interest = 0
        p = initial_p

        if count > 1:
            total_interest_old = total_interest_new

        total_interest_new = 0
        while month < duration:
            interest = p * ((r / 100)/12)
            p += interest - (base_month_m + offset)
            total_interest_new += interest
            month +=1

        offset = total_interest_new/duration
        m = base_month_m + offset
        count += 1

    return int(round(m))

args = input("input data:\n")
args = args.split(' ')
p = int(args[0])
r = int(args[1])
duration = int(args[2])

answer = find_payments(p,r,duration)
print("\nanswer:\n" + str(answer))