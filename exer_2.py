def biggerIsGreater(w):
    word = list(w)
    i = j = l = len(word) - 1
    while i > 0 and word[i - 1] >= word[i]:
        i -= 1
    if i <= 0:
        return 'no answer'
    while word[j] <= word[i - 1]:
        j -= 1
    word[i - 1], word[j] = word[j], word[i - 1]
    word[i:] = word[l:i - 1:-1]
    return ''.join(word)
