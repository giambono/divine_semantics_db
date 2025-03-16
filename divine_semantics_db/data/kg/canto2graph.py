import openai
import json
import pandas as pd

# Set your OpenAI API key
openai.api_key = "your-openai-api-key"  # Replace with your actual key

# Helper function to extract graph from tercet

def extract_graph_from_tercet(cantica, canto, tercet):
    prompt = f"""
You are an expert in narrative analysis and semantic parsing, tasked with converting tercets from Dante's Divine Comedy into a structured knowledge graph. For each tercet, extract the following:

1. **Nodes:** Any Person, Location, Animal, Sin, or Verse explicitly or implicitly mentioned.
2. **Relationships:** Meaningful interactions between these nodes using the allowed relationship types.

## Allowed Node Types (and their properties):
- Verse: cantica, canto, verse_number, text, author, theme
- Person: id, role, historical_identity, verses, quote, theme
- Location: id, description, verses, theme
- Animal: id, symbolism, verses, description, theme
- Sin: id, circle, description, punishment, verses, theme

## Allowed Relationship Types (and their properties):
- MENTIONS: source (Verse), target (any other), verse_number, canto
- APPEARS_IN: source (any), target (Verse), verse_number, canto
- GUIDES: source (Person), target (Person), verses
- ENCOUNTERS: source (Person), target (any), verses
- BLOCKS_PATH: source (Animal), target (Person), verses
- DESCRIBES: source (Verse), target (any), verses
- SUFFERS: source (Person), target (Sin), verses
- PUNISHES: source (Sin), target (Person), verses
- LOCATED_IN: source (Location), target (Location)
- REPRESENTS: source (any), target (abstract concept), description
- SEEK: source (Person), target (Person), verses
- JUDGES: source (Person), target (Person), verses
- NEXT_VERSE: source (Verse), target (Verse)
- ASSOCIATED_WITH: source (Sin), target (Location)
- CONTAINS: source (Canto), target (Verse)

---

## Input
Cantica: {cantica}
Canto: {canto}
Tercet:
{tercet}

---

## Output Format
{{
    "tercet": "{tercet}",
    "nodes": [{{<each node>}}],
    "relationships": [{{<each relationship>}}]
}}

Example Node:
{{
    "id": "Virgil",
    "type": "Person",
    "properties": {{
        "role": "Guide",
        "historical_identity": "Roman poet",
        "verses": ["Inferno 1:61-90"],
        "theme": "Guidance"
    }}
}}

Example Relationship:
{{
    "source": "Virgil",
    "target": "Narrator",
    "type": "GUIDES",
    "properties": {{
        "verses": ["Inferno 1:61-90"]
    }}
}}

---

Now process the following tercet:
Cantica: {cantica}
Canto: {canto}
Tercet:
{tercet}

Return only the JSON object, no explanations.
"""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a text analysis and graph extraction expert."},
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )

    extracted_graph = json.loads(response["choices"][0]["message"]["content"])
    return extracted_graph


# Example DataFrame representing a full canto split into tercets
data = {
    "cantica": ["Inferno"] * 3,
    "canto": [1] * 3,
    "tercet_number": [1, 2, 3],
    "tercet": [
        "Nel mezzo del cammin di nostra vita\nmi ritrovai per una selva oscura,\nché la diritta via era smarrita.",
        "Ahi quanto a dir qual era è cosa dura\nesta selva selvaggia e aspra e forte\nche nel pensier rinova la paura!",
        "Tant’è amara che poco è più morte;\nma per trattar del ben ch’i’ vi trovai,\ndirò de l’altre cose ch’i’ v’ho scorte."
    ]
}

canto_df = pd.DataFrame(data)

# Process each tercet
all_graphs = []

for _, row in canto_df.iterrows():
    graph = extract_graph_from_tercet(row['cantica'], row['canto'], row['tercet'])
    all_graphs.append(graph)

# Combine into a single structure (optional - you could also save as JSON per tercet)
with open("canto_1_graph.json", "w", encoding="utf-8") as f:
    json.dump(all_graphs, f, indent=2, ensure_ascii=False)

print("Processed graph saved as canto_1_graph.json")
