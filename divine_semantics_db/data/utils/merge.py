import pandas as pd
from prompt_labeling import build_prompt


# Join outline onto verse dataframe
def find_outline_for_verse(verse_number, outline_df):
    match = outline_df[(outline_df['start_verse'] <= verse_number) & (outline_df['end_verse'] >= verse_number)]
    return match['text'].values[0] if not match.empty else ""


# Load data
commedia = pd.read_csv("/home/rfflpllcn/IdeaProjects/divine_semantics_db/divine_semantics_db/data/commedia.csv", sep=";")
commedia_inferno_en = commedia[(commedia["author"] == "kirkpatrick") & (commedia["cantica"] == 1)]

outline_inferno_en = pd.read_csv("/home/rfflpllcn/IdeaProjects/divine_semantics_db/divine_semantics_db/data/outlines/hollander/inferno/hollander_inferno_outline.csv", sep=";")

thematic_labels = pd.read_csv("/home/rfflpllcn/IdeaProjects/divine_semantics_db/divine_semantics_db/data/labels/thematic_labels_inferno.csv")

commedia_inferno_en['outline_text'] = commedia_inferno_en['verse_number'].apply(
    lambda v: find_outline_for_verse(v, outline_inferno_en)
)

# Create enhanced text
commedia_inferno_en['enhanced_text'] = (
        "Verse Text: " + commedia_inferno_en['text'] +
        "\nContext Summary: " + commedia_inferno_en['outline_text']
)

labels = "Label,Description: \n" +"\n".join([f"{label}: {description}" for label, description in thematic_labels.values])
grouped = commedia_inferno_en.groupby("outline_text")["text"].apply(list).reset_index()

print(commedia_inferno_en)