import os
import string
script_dir = os.path.dirname(__file__)
path_to_file = os.path.join(script_dir, "books", "frankenstein.txt")
def main():
    with open(path_to_file, encoding="utf-8") as f:
        file_contents = f.read()
        word_count = file_contents.split()
        # print(len(word_count))
        return len(word_count)

def count_characters():
    with open(path_to_file, encoding="utf-8") as f:
        file_contents = f.read()
        word_count = file_contents.split()
        lowered_string = file_contents.lower()
        letters = set(lowered_string)
        result = {}
        for i in letters:
            if i in string.punctuation or i in string.whitespace or i == "'":
                continue
            result[i] = lowered_string.count(i)
        # print(result)
        return result

def print_report():
    report = count_characters()
    print(f"--- Begin report of {path_to_file} ---")
    print(f"{main()} words found in the document")
    print()
    for k, v in report.items():
        print(f"The '{k}' character was found {v} times")
    print("--- End report ---")
if __name__ == "__main__":
    print_report()