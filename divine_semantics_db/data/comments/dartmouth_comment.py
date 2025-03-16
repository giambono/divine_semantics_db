"""

"""
import pandas as pd


def process_text_to_csv(author, cantica, canto, input_text, output_file='output.csv'):
    """
    Processes input text to generate a CSV file with structured commentary data.

    Parameters:
    - author: The author of the commentary (e.g., "Sapegno").
    - cantica: The name of the cantica (e.g., "Inferno").
    - canto: The canto number.
    - input_text: The raw text containing the commentary with verses.
    - output_file: The name of the CSV file to save the processed data.
    """
    # Split the input text by lines and remove empty lines
    lines = [line.strip() for line in input_text.split('\n') if line.strip()]

    # Prepare the data list to collect the parsed information
    data = []

    # Process the lines: Each pair of lines represents start/end verses and the comment
    for i in range(0, len(lines), 2):
        # Line i is the start and end verse line
        start_end_line = lines[i].strip().strip()
        # Line i + 1 is the comment line
        comment_line = lines[i + 1].strip()

        start_verse, end_verse = tuple(map(int, start_end_line.split("-")))

        try:
            # Add the parsed row to the data list
            data.append([cantica, canto, start_verse, end_verse, author, comment_line])
        except Exception as e:
            print(f"Error parsing verses in line: {start_end_line}")
            continue

    # Create a DataFrame from the collected data
    df = pd.DataFrame(data, columns=["cantica", "canto", "start_verse", "end_verse", "author", "comment"])

    # Save the DataFrame to the specified CSV file
    df.to_csv(output_file, index=False)

    return output_file  # Return the file path for confirmation


if __name__ == "__main__":
    author = "Sapegno"
    cantica = "Inferno"
    canto = "34"
    # Open the file in read mode
    with open('raw_text.txt', 'r') as file:
        # Read the content of the file
        text = file.read()


    # Call the function
    process_text_to_csv(author, cantica, canto, text, output_file=f'{author}_{cantica}_{canto}.csv')
