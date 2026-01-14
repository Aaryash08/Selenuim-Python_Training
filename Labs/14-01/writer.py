def write_numbers_to_file(filename):
    try:
        file = open(filename, "w")
        for i in range(1, 101):
            file.write(str(i) + "\n")
        file.close()
    except FileNotFoundError:
        print("File not found")
    except PermissionError:
        print("Permission denied")
