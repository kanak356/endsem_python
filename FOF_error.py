try:
    with open("nonexistent.txt") as f:
        content = f.read()
except FileNotFoundError:
    print("FileNotFoundError: The file does not exist.")