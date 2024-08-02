# utils/extract_items.py

import re

def extract_items(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    pattern = re.compile(r'add_item\\(\d+)\\.*?\\.*?\\.*?\\.*?\\(.*?)\\')
    items = pattern.findall(content)
    return {name.lower(): item_id for item_id, name in items}

def load_items(file_path):
    return extract_items(file_path)
