

# ----- The DFSM, exactly as specified: (Sigma, Q, q0, F, delta) -----
SIGMA = {'a', 'b'}
Q = {1, 2, 3, 4, 5}
q0 = 1
F = {2, 5}

delta = {
    1: {'a': 2,    'b': 3},
    2: {'a': 2,    'b': 4},
    3: {'a': 5,    'b': 4},
    4: {'a': 5,    'b': 4},
    5: {'a': None, 'b': None},   # {9} has no outgoing a or b move
}


def accepts_state(s: str) -> bool:
    
    state = q0
    for ch in s:
        # reject symbols outside SIGMA {a,b}
        if ch not in SIGMA:
            return False       
        # dead state
        if state is None:
            break                 
        state = delta[state][ch]
    return state in F # return only the accepting state


def main():
    print("DFSM acceptor for L = a*b*a   (alphabet {a, b})")
    print("Enter strings terminated by '$'. Enter just '$' to quit.\n")

    while True:
        text = input("input = ")

        # check input string must end with a '$'
        if '$' not in text:
            print("  Error: input must end with '$'. Try again.")
            continue

        string_text1 = text[:len(text)-1]
        #string_text = text[:text.index('$')]      # everything before the first '$'

        if string_text1 == '':
            break                      # user entered just "$" -> quit

        result = "YES" if accepts_state(string_text1) else "NO"
        print(f"input = {string_text1}$ output={result}")


if __name__ == "__main__":
    main()
    