#!/usr/bin/env python3
import json

def serialize_and_save_to_file(data, filename):
    """Serialize a dictionary and save it to a JSON file."""
    with open(filename, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file)

def load_and_deserialize(filename):
    """Load and deserialize a JSON file back to a dictionary."""
    with open(filename, 'r', encoding='utf-8') as json_file:
        return json.load(json_file)
