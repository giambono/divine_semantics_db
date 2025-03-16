import csv

# Specify the input and output file paths

input_file = "/home/rfflpllcn/IdeaProjects/divine_semantics_db/divine_semantics_db/data/commedia.csv"
output_file = "/home/rfflpllcn/IdeaProjects/divine_semantics_db/divine_semantics_db/data/commedia_modified.csv"



with open(input_file, 'r', newline='', encoding='utf-8') as fin:
    reader = csv.reader(fin, delimiter=';')
    rows = list(reader)

header = rows[0]

# Determine the index for the "text" column. Default to 5th column (index 4) if not found.
try:
    text_col_index = header.index("text")
except ValueError:
    text_col_index = 4

with open(output_file, 'w', newline='', encoding='utf-8') as fout:
    writer = csv.writer(fout, delimiter=';')
    writer.writerow(header)

    for row in rows[1:]:
        # Remove leading and trailing double quotes if they exist
        new_row = row[:4] + [";".join(row[4:-2])] + row[-2:]

        writer.writerow(new_row)

print(f"Modified CSV saved to: {output_file}")
