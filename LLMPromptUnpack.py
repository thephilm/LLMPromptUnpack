import os
import re

def extract_files(input_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract file sections
    file_pattern = r'--- File: (.*?) ---\n(.*?)\n--- End of File ---'
    files = re.finditer(file_pattern, content, re.DOTALL)

    for match in files:
        filepath = match.group(1)
        content = match.group(2)
        
        # Create directories if needed
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        # Write file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
            print(f"Extracted: {filepath}")

if __name__ == "__main__":
    extract_files("project.txt")