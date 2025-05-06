try:
    x = int("abc")
    y = 10 / 0
    print(undefined_var)
except ZeroDivisionError:
    print("ZeroDivisionError occurred.")
except NameError:
    print("NameError occurred.")
except ValueError:
    print("ValueError occurred.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
