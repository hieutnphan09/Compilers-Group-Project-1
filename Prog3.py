reserved_words = ["cin>>", "for", "int", "cout<<"]
operators = ["+", "-", "*", "/", "++", "--"]
special = [">", "=", ";", "(", ")", ">=", ","]

def is_word_char(ch: str) -> bool:
    return ch.isalnum() or ch == '_' 

def is_number(toke: str) -> bool:
    if toke.startswith('-'):
        toke = toke[1:]
    return len(toke) > 0 and toke.isdigit()

def is_identifier(toke: str) -> bool:
    if len(toke) == 0:
        return False
    if not (toke[0].isalpha() or toke[0] == '_'):
        return False
    return all(is_word_char(c) for c in toke[1:])

def scan_lexemes(line:str) -> list:
    tokens = []
    i = 0 
    n = len(line)

    while i < n:
        ch = line[i]

        if ch.isspace(): #skip whitespace between tokes
            i+=1
            continue

        if is_word_char(ch):
            start = i
            while i < n and is_word_char(line[i]):
                i+=1
            word = line[start:i]
            if line[i:i +2] in ["<<", ">>"]:
                word += line[i:i +2]
                i+=2
            tokens.append(word)
            continue
        if ch == '-' and i+1 < n and line[i+1].isdigit():
            start = i
            i+=1
            while i < n and line[i].isdigit():
                i+=1
            tokens.append(line[start:i])
            continue
        two = line[i:i +2]
        if two in ("++", "--", ">=", "<="):
            tokens.append(two)
            i+=2
            continue
        tokens.append(ch)
        i+=1
    return tokens

def classify(toke: str) -> str:
    lower = toke.lower()

    #1 case-insensitive reserved word
    if lower in [w.lower() for w in reserved_words]:
        return "reserved word"

    #2 Special symbol
    special_effective = [s for s in special if s != ">"]
    if toke in special_effective:
        return "special symbol"
    if toke in operators or toke == ">":
        return "operator"

    #3 Number
    if is_number(toke):
        return "number"

    #4 Identifier
    if is_identifier(toke):
        return "identifier"

    #5 If none of the above
    return "invalid"

def main():
    while True: 
        line = input("Enter a statement: ")
        line = line[:255] #255 char cap

        for toke in scan_lexemes(line):
            print(f"{toke}\t\t{classify(toke)}")

        go_again = input("CONTINUE (y/n)?: ").strip().lower()
        if go_again != 'y':
            break
if __name__ == "__main__":
    main()