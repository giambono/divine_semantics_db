import re
import csv


def remove_numbers_except_canto(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    with open(file_path, 'w', encoding='utf-8') as file:
        for line in lines:
            if line.startswith("CANTO"):
                file.write(line)
            else:
                # Remove all numbers from the line
                new_line = re.sub(r'\d+', '', line)
                file.write(new_line)


def remove_blank_rows(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    with open(file_path, 'w', encoding='utf-8') as file:
        for line in lines:
            if line.strip():  # Check if the line is not empty or just whitespace
                file.write(line)


def add_indices(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    cumulative_index = 0
    reset_index = 0

    with open(file_path, 'w', encoding='utf-8') as file:
        for line in lines:
            if line.startswith("CANTO"):
                file.write(f"{cumulative_index}\t{reset_index}\t{line}")
                reset_index = 0  # Reset the index when encountering "CANTO"
            else:
                file.write(f"{cumulative_index}\t{reset_index}\t{line}")
                cumulative_index += 1
                reset_index += 1

def add_canto_index(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    current_canto_number = None

    with open(file_path, 'w', encoding='utf-8') as file:
        for line in lines:
            if "CANTO" in line:
                # Extract the last number from the line
                numbers = re.findall(r'\d+', line)
                if numbers:
                    current_canto_number = numbers[-1]
                file.write(line)  # Write the CANTO line as is
            else:
                if current_canto_number is not None:
                    file.write(f"{current_canto_number}\t{line}")
                else:
                    file.write(f"0\t{line}")  # Default to 0 if no CANTO line has been encountered yet


def remove_canto_lines(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    with open(file_path, 'w', encoding='utf-8') as file:
        for line in lines:
            if "CANTO" not in line:
                file.write(line)


def text_to_csv(input_file_path, output_file_path):
    with open(input_file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    with open(output_file_path, 'w', encoding='utf-8', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=';')

        for line in lines:
            parts = line.split(maxsplit=3)  # Split the line into at most 4 parts
            if len(parts) == 4:
                # Remove leading and trailing whitespace from the text part
                parts[3] = parts[3].strip()
                csvwriter.writerow(parts)
            else:
                # Handle lines that do not have the expected format
                csvwriter.writerow([line.strip()])

file_path = 'kirkpatrick_3.txt'
output_file_path = 'kirkpatrick_3.csv'

remove_numbers_except_canto(file_path)

remove_blank_rows(file_path)

add_indices(file_path)

add_canto_index(file_path)

remove_canto_lines(file_path)


text_to_csv(file_path, output_file_path)