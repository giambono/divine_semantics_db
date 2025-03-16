NODE_TYPES = {
    "Verse": {
        "description": "A single verse or line from the Divine Comedy",
        "properties": ["cantica", "canto", "verse_number", "text", "author", "theme"]
    },
    "Person": {
        "description": "A person or character (real, historical, mythological)",
        "properties": ["role", "historical_identity", "verses", "quote", "theme"]
    },
    "Location": {
        "description": "A physical or symbolic location",
        "properties": ["verses", "description", "theme"]
    },
    "Animal": {
        "description": "A symbolic or real animal appearing in the text",
        "properties": ["symbolism", "verses", "description", "theme"]
    },
    "Sin": {
        "description": "A moral or spiritual transgression",
        "properties": ["circle", "description", "punishment", "verses", "theme"]
    }
}


RELATIONSHIP_TYPES = {
    "MENTIONS": {
        "description": "A verse mentions an entity (person, location, animal, sin)",
        "properties": ["verse_number", "canto"]
    },
    "APPEARS_IN": {
        "description": "An entity appears in a specific verse",
        "properties": ["verse_number", "canto"]
    },
    "GUIDES": {
        "description": "One character guides another",
        "properties": ["verses"]
    },
    "ENCOUNTERS": {
        "description": "A character encounters someone or something",
        "properties": ["verses"]
    },
    "BLOCKS_PATH": {
        "description": "An obstacle blocks the narrator's path",
        "properties": ["verses"]
    },
    "DESCRIBES": {
        "description": "A verse describes a place, person, or sin",
        "properties": ["verses"]
    },
    "SUFFERS": {
        "description": "A sinner suffers a particular punishment",
        "properties": ["verses", "description"]
    },
    "PUNISHES": {
        "description": "Divine justice punishes a sinner",
        "properties": ["verses", "description"]
    },
    "LOCATED_IN": {
        "description": "A location exists within a larger location (e.g., Circle in Inferno)",
        "properties": []
    },
    "REPRESENTS": {
        "description": "An entity symbolizes an abstract concept",
        "properties": ["description"]
    },
    "SEEK": {
        "description": "One character seeks help or guidance from another",
        "properties": ["verses"]
    },
    "JUDGES": {
        "description": "A figure of authority assigns punishment",
        "properties": ["verses"]
    },
    "NEXT_VERSE": {
        "description": "Sequential link between verses (narrative flow)",
        "properties": []
    },
    "ASSOCIATED_WITH": {
        "description": "A sin is associated with a particular location (circle)",
        "properties": []
    },
    "CONTAINS": {
        "description": "A canto contains one or more verses",
        "properties": []
    }
}
