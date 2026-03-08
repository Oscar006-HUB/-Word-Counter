import sys
# open the file in read mode
def count_words(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
# Split by whitespace an filter out  empty strings              
            words = content.split()    
            word_count = len(words)
            
            print(f"Success! The file contains {word_count} words.")
            return word_count
        
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
# Message displayed when file is not found.
    except PermissionError:
        print(f"Error: Permission denied when trying to read'{file_path}'.")
    except Exception as e:
        print(f"An unexpected error occured:{e}")
 # example.txt used as the target file with content in it.       
if __name__ == "__main__":
    target_file = "example.txt"
    count_words(target_file)    