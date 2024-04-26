from pathlib import Path

file_path = Path("cats_file.txt")

def get_cats_info(path):
    try:
        cats_list = []
        with open(path, encoding='utf-8') as file:
            lines = [el.strip() for el in file.readlines()]
        
        for line in lines:
            splited_line = line.split(",")
            cat_info = {"id": splited_line[0], "name": splited_line[1], "age": splited_line[2],}
            cats_list.append(cat_info)

        return cats_list

    except FileNotFoundError:
        print(f"The file '{path}' does not exist.")
        return None

    except Exception as error:
        print(f"An error occurred: {error}")
        return None

cats_info = get_cats_info(file_path)
print(cats_info)