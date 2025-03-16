import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

url = "https://en.wikipedia.org/wiki/List_of_cultural_references_in_the_Divine_Comedy"
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')


# Extract plain text
text = soup.text

# Identify starting point (after alphabetical index)
start_indicator = "A B C D E F G H I J K L M N O P Q R S T U V W Z – References"
end_indicator = "References[edit]"

# Extract the relevant text section
start_pos = text.find(start_indicator) + len(start_indicator)
end_pos = text.find(end_indicator)

relevant_text = text[start_pos:end_pos].strip()

# Split the text into lines
lines = relevant_text.split('\n')

characters = []
current_char = {}

for line in lines:
    if line.endswith('[edit]') or ": See" in line:
        continue

    line = line.strip()
    if not line:
        continue  # Skip empty lines

    # Detect a new character (lines with "Name: Description" format)
    if ':' in line and not line.startswith(' '):
        if current_char:
            characters.append(current_char)
        name, description = line.split(':', 1)
        current_char = {
            'Name': name.strip(),
            'Description': description.strip(),
            'References': []
        }
    else:
        # Otherwise, it's a reference for the current character
        if current_char:
            current_char['References'].append(line.strip())

# Append the last character
if current_char:
    characters.append(current_char)


expanded_data = [
    {'Description': char['Description'], 'Name': char['Name'], 'Reference': ref}
    for char in characters
    for ref in char['References']
]

# Create DataFrame
_df = pd.DataFrame(expanded_data)

# Identify rows that do NOT contain 'Inf.', 'Purg.', or 'Par.' in the Reference column
df_non_matching = _df[~_df['Reference'].str.contains(r'Inf|Purg|Par', regex=True)]

df_matching = _df[_df['Reference'].str.contains(r'Inf|Purg|Par', regex=True)]

df_matching.columns = ['description', 'name', 'reference']
df = df_matching[['name', 'description', 'reference']]

# Split 'reference' column into 'ref_descr' and 'ref' based on the pattern given
# df[['ref_descr', 'ref']] = df['reference'].str.extract(r'^(.*?)(\b(?:Inf|Purg|Par).*)$')

# Correct regex to split only at exact matches ("Inf", "Inf.", "Purg", "Purg.", "Par", "Par.") not substrings like "Paradise"
df[['ref_descr', 'ref']] = df['reference'].str.extract(r'^(.*?)(\b(?:Inf\.?|Purg\.?|Par\.?)\b.*)$')


# Drop the original 'reference' column as it's no longer needed
df_final = df.drop(columns=['reference'])


# Display or save DataFrame
print(df_final.head())
df_final.to_csv('divine_comedy_characters2.csv', index=False)
