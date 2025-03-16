

def build_prompt(verses, canto_summary, examples, labels):
    """
    Build the GPT prompt for labeling a group of verses.

    Args:
        verses (list): List of verse texts.
        canto_summary (str): Summary of the canto these verses belong to.
        examples (str): Few-shot examples in "Verse: ...\nLabels: ..." format.
        labels (list): Full list of possible thematic labels.

    Returns:
        str: Fully formatted prompt ready for GPT.
    """

    verses_text = "\n".join(f"{i+1}. {verse}" for i, verse in enumerate(verses))

    prompt = f"""
You are an expert literary analyst specialized in Dante's Inferno. You will be shown a group of verses from Dante's Inferno (translated to English), along with a brief summary of the canto and its context. Your task is to assign thematic labels to this group of verses, choosing only from the provided list of thematic labels.

### Verses
{verses_text}

### Canto Context
{canto_summary}

### Thematic Labels (choose only from this list)
{", ".join(labels)}

### Examples
{examples}

### Output Format
You should respond in this exact format only:
Labels: ["label1", "label2", ...]

Now, analyze the verses and provide the thematic labels.
    """.strip()

    return prompt
