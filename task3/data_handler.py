from colorama import Fore

nesting_symbol = "    "
list_of_files = []

def get_folder(path: str):
    splited_string = path.split("/")
    string_with_nesting = (nesting_symbol * len(splited_string)) + splited_string[-1] + "/"
    string_with_color = f"{Fore.GREEN}{string_with_nesting}{Fore.RESET}"

    return string_with_color

def get_file(path: str):
    splited_string = path.split("/")
    string_with_nesting = (nesting_symbol * len(splited_string)) + splited_string[-1]
    string_with_color = f"{Fore.BLUE}{string_with_nesting}{Fore.RESET}"

    return string_with_color

def get_list_of_files(path, str_len):
    for el in path.iterdir():
        if el.is_dir():
            rel_path_string = str(el)[str_len + 1:]
            list_of_files.append(get_folder(rel_path_string))

            get_list_of_files(el, str_len)
        else:
            rel_path_string = str(el)[str_len + 1:]
            list_of_files.append(get_file(rel_path_string))

    return list_of_files