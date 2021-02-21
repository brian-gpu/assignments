def identify_type(data):
    for d in data:
        print(f"Type = {type(d)}, Item {d}")

data = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":"V", "section":"A"}]
identify_type(data)