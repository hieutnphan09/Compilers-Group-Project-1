"""
Prog2.py Question 13 Lexeme Pre-Processor

This reads infile.txt and writes outfile.txt
    -Removes comments, blank lines
    -Normalizes spacing to one space between lexemes
    -Starts new output line after each ';'
"""

MULTI_CHAR_LEXEMES = ["cin>>", "cout<<", ">=", "<=", "++", "--"]

def strip_comment(line: str) -> str:
    #Remove everything from the first '//' on
    idx = line.find("//") #search line for '//'
    if idx != -1: 
        return line[:idx]
    return line

def is_word_char(ch: str) -> bool:
    return ch.isalnum() or ch == '_'

def tokenize(text: str) -> list:
    tokens = [] #empty list
    i = 0 #symbolic cursor position 
    n = len(text) # number characters in string

    while i < n:
        ch = text[i] #look at character cursor is on

        #1. skip whitespace/separate lexemes
        if ch.isspace():
            i += 1 
            continue
        #2 try to match multi-character lexemes/tokens
        matched = None 
        for lex in MULTI_CHAR_LEXEMES:
            if text[i:i + len(lex)] == lex:
                if matched is None or len(lex) > len(matched):
                    matched = lex
        if matched:
            tokens.append(matched)
            i += len(matched)
            continue
        #3 run of leters, digits, underscore
        if is_word_char(ch):
            start = i
            while i<n and is_word_char(text[i]):
                i+=1
            tokens.append(text[start:i])
            continue

        #4 Otherwise treat this single punctuation/operator character as its own lexeme
        tokens.append(ch)
        i+= 1
    return tokens 

def preprocess(input_path: str, output_path: str) -> None:
    with open(input_path, "r") as infile:
        raw_lines = infile.readlines()

    #strip comments line by line, tokenize what remains
    all_tokens = []
    for line in raw_lines:
        cleaned = strip_comment(line)
        all_tokens.extend(tokenize(cleaned))

    out_lines = []
    current_line = []
    for toke in all_tokens:
        current_line.append(toke)
        if toke == ';':
            out_lines.append(' '.join(current_line))
            current_line = []
    if current_line:
        out_lines.append(' '.join(current_line))

    with open(output_path, "w") as outfile:
        for line in out_lines:
            outfile.write(line + "\n")

def main():
    preprocess("infile.txt", "outfile.txt")
    print("Complete; outfile.txt written")

if __name__ == "__main__":
    main()