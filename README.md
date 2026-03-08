# Word Counter

A simple Python script that counts the number of words in a text file — built with error handling to make it reliable in real-world use.

## Features

- Counts words in any `.txt` file
- Handles common errors gracefully with clear messages
- Supports `utf-8` encoding (special characters, emojis, multilingual text)
- Accepts filename as a command-line argument

## Requirements

- Python 3.x
- No external libraries needed

## Usage

**Basic (default file):**
```bash
python word_counter.py
```

**With a specific file:**
```bash
python word_counter.py myfile.txt
```

## Example Output

```
Success! The file contains 142 words.
```

## Error Handling

| Error | Message |
|---|---|
| File not found | `Error: The file at 'myfile.txt' was not found.` |
| No read permission | `Error: Permission denied when trying to read 'myfile.txt'.` |
| Any other error | `An unexpected error occurred: <details>` |

## How It Works

1. Opens the file using a `with` statement for safe, automatic file handling
2. Reads the full content with `utf-8` encoding
3. Splits the text on whitespace using `.split()` to count words accurately
4. Returns the word count, or `None` if an error occurred
 
## Project Context

Built as part of my internship at **CodVeda Technologies** focused on defensive programming and writing code that doesn't just work, but holds up.

  NB:Target file can be modified from my file "example.txt" to file of your choice for coade to be able to read your file when executed.
