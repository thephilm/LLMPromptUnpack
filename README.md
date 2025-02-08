# **LLMPromptUnpack**  

LLMPromptUnpack extracts files from a structured text file created by **LLMPromptPack**.  
It reconstructs the original folder and file structure, restoring the project from a `.txt` backup.  

---

## **Installation Requirements**  
- Requires **Python**  

---

## **Usage**  

Run from the command line:  
python llm_prompt_unpack.py
This will process the default input file:  
project.txt
Simply rename your eported file to project.txt to use as input.

### **How It Works**  
1. The script reads the structured text file.  
2. It detects file sections formatted like this:  
--- File: path/to/file.ext --- (file content) --- End of File ---
3. It reconstructs the directory structure.  
4. It restores each file with its original content.  

### **Customizing the Input File**  
- You can modify the script to change the default filename.

---

## **Example Use Case**  
1. **LLMPromptPack** converts a project folder into a `.txt` file.  
2. The text file is used as **input for an LLM** or stored as a backup.  
3. Later, **LLMPromptUnpack** reconstructs the original files.  

---

## **Future Improvements**
- Allow users to specify a different output directory.  
- Add error handling for malformed `.txt` files.  
- Implement CLI arguments for better automation.  

---

### **License**
MIT License – Free to use and modify.

---

**Created by Philip Mastroianni**  
