try:
    d = {"a": 1}
    print(d["b"])
except KeyError:
    print("KeyError: Key not found in dictionary.")
