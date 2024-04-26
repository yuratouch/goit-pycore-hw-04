from pathlib import Path

file_path = Path("salary_file.txt")

def total_salary(path):
    try:
        sum = 0
        with open(path) as file:
            lines = [el.strip() for el in file.readlines()]
        
        for line in lines:
            splited_line = line.split(",")
            sum += int(splited_line[1])

        return (sum, int(sum/len(lines)))

    except FileNotFoundError:
        print(f"The file '{path}' does not exist.")
        return (None, None)

    except Exception as error:
        print(f"An error occurred: {error}")
        return (None, None)

total, average = total_salary(file_path)
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")