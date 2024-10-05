NO_OF_CHARS = 256

def badCharHeuristic(string, size):
    '''
    The preprocessing function for Boyer Moore's bad character heuristic
    '''
    # Initialize all occurrences as -1
    badChar = [-1] * NO_OF_CHARS

    # Fill the actual value of last occurrence
    for i in range(size):
        badChar[ord(string[i])] = i

    # return initialized list
    return badChar

def search(txt, pat):
    '''
    A pattern searching function that uses Bad Character
    Heuristic of Boyer Moore Algorithm
    '''
    m = len(pat)
    n = len(txt)

    # Create the bad character list
    badChar = badCharHeuristic(pat, m)

    # s is shift of the pattern with respect to text
    s = 0
    while s <= n - m:
        j = m - 1

        # Keep reducing index j of pattern while characters of pattern and text are matching
        while j >= 0 and pat[j] == txt[s + j]:
            j -= 1

        # If the pattern is present at the current shift
        if j < 0:
            print("Pattern occurs at shift = {}".format(s))

            # Shift the pattern so that the next character aligns with the last occurrence
            s += (m - badChar[ord(txt[s + m])] if s + m < n else 1)
        else:
            # Shift the pattern so that the bad character aligns with the last occurrence
            s += max(1, j - badChar[ord(txt[s + j])])

# Driver program to test above function
def main():
    txt = "ABAAABCD"
    pat = "ABC"
    search(txt, pat)

if __name__ == '__main__':
    main()
