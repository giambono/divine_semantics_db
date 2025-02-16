import os
import config
import pandas as pd


EXCEL_FILE = os.path.join(config.APP_DIR, "data/dante_original.xlsx")  # Adjust if needed
df = pd.read_excel(EXCEL_FILE)

def extract_verse_count(verse_range):
    start, end = map(int, verse_range.split('-'))
    return end - start + 1

# Compute cumulative verse index
df["verse_count"] = df["verse"].apply(extract_verse_count)
df["cumulative_index"] = df["verse_count"].cumsum() - 1  # Make index 0-based

def generate_cumulative_list(df):
    cumulative_list = []
    last_index = -1
    for count in df["verse_count"]:
        indices = list(range(last_index + 1, last_index + 1 + count))
        cumulative_list.append(indices)
        last_index = indices[-1]
    return cumulative_list

df["cumulative_indices"] = generate_cumulative_list(df)


# Select the last row of each canto
last_lines_df = df.groupby("canto").tail(1)


last_lines_df.to_clipboard()
