try:
    import non_existent_module
except ModuleNotFoundError:
    print("ModuleNotFoundError: Module does not exist.")