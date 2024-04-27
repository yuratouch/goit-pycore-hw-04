def print_filetree(list:list):
    with open("output.txt", "w", encoding="utf-8") as file:
        for line in list:
            file.write(line + "\n")

    with open("output.txt", "r", encoding="utf-8") as file:
        print(file.read())