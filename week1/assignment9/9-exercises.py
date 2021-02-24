def format_orders1(orders):
    order_numbers = list(map(lambda x: x[0], orders))
    totals = list(map(lambda x: x[2] * x[3] + ((int(x[2] * x[3]) < 100) * 10), orders))
    results = list(map(lambda x, y: (x, round(y,2)), order_numbers, totals))

    return results

# Assumption: cost update of +10 when under 100, is not requested
def format_orders2(orders):
    order_numbers = list(map(lambda x: x[0], orders))
    totals = list(map(lambda x: x[1][1] * x[1][2], orders))
    results = list(map(lambda x, y: (x, round(y,2)), order_numbers, totals))

    return results

orders1 = [
['Order Number', 'Book Title and Author', 'Quantity', 'Price per Item'],
[34587,'Learning Python, Mark Lutz',4,40.95],
[98762,'Programming Python, Mark Lutz',5,56.80],
[77226,'Head First Python, Paul Barry',3,32.95],
[88112,'Einführung in Python3, Bernd Klein',3,24.99]]

orders2 = [
['Order Number', ('Book Title and Author', 'Quantity', 'Price per Item')],
[34587,('Learning Python, Mark Lutz',4,40.95)],
[98762,('Programming Python, Mark Lutz',5,56.80)],
[77226,('Head First Python, Paul Barry',3,32.95)],
[88112,('Einführung in Python3, Bernd Klein',3,24.99)]]

print("Exercise 1:")
print(format_orders1(orders1[1:]))

print("Exercise 2:")
print(format_orders2(orders2[1:]))