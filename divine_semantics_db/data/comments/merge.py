import pandas as pd
import os

# List all the files you want to merge
files = [f"Sapegno_Inferno_{i}.csv" for i in range(1, 35)]

# Initialize an empty DataFrame
merged_df = pd.DataFrame()

# Loop through each file and append its content
for file in files:
    temp_df = pd.read_csv(file)
    merged_df = pd.concat([merged_df, temp_df], ignore_index=True)

# Save the final merged file
merged_df.to_csv("sapegno_inferno.csv", index=False)

print("All files have been merged into 'sapegno_inferno.csv'")
