from writer import write_numbers_to_file
def read_file_safely(filename):
    try:
        file = open(filename, "r")
        lines = file.readlines()

        for line in lines:
            print(line.strip())

        file.close()
    except FileNotFoundError:
        print("File not found")
    except PermissionError:
        print("Permission denied")

if __name__ == "__main__":
    filename = "file.txt"

    write_numbers_to_file(filename)
    read_file_safely(filename)
