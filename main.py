def main():
    path_to_file = "books/frankenstein.txt"
    with open(path_to_file) as f:
        file_contents = f.read()
        print(file_contents)
        print(generate_report(file_contents))

def count_words(string):
    return len(string.split())

def count_characters(string):
    count_characters = {}
    for c in string:
        c = c.lower()
        if c not in count_characters.keys():
            count_characters[c] = 1
        else:
            count_characters[c] +=1
    return {k: v for k, v in sorted(count_characters.items(), key=lambda item: item[1], reverse=True)}

def generate_report(file_contents):
    word_count = count_words(file_contents)
    char_count = count_characters(file_contents)
    out_report = ""

    out_report += "--- Begin report of books/frankenstein.txt ---\n\n"
    out_report += f"{word_count} found in the document\n"
    for c in char_count.keys():
        if c.isalpha():
            out_report += f"The '{c}' character was found {char_count[c]} times\n"

    return out_report

main()