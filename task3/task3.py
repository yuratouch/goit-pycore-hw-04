import sys
from pathlib import Path
from colorama import Fore
from data_handler import get_list_of_files
from output_handler import print_filetree

def main():
    try:
        path_str_len = len(sys.argv[1])
        path_to_dir = Path(sys.argv[1])
        target_dir_name = f"{Fore.GREEN}{path_to_dir.name}/{Fore.RESET}"

        prepared_list = get_list_of_files(path_to_dir, path_str_len)
        prepared_list.insert(0, target_dir_name)

        return print_filetree(prepared_list)
    
    except FileNotFoundError:
        print(f"{Fore.RED}No such directory.\nPlease try again with the correct path to the directory.{Fore.RESET}")
        return None
    
    except NotADirectoryError:
        print(f"{Fore.RED}{path_to_dir} is a file.\nPlease try input path to directory.{Fore.RESET}")
        return None

if __name__ == '__main__':
    main()