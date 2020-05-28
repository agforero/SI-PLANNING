def mix(word1, word2):
    total = 0
    longer = 0
    ret = ""

    if len(word1) >= len(word2):
        total = len(word2)
        longer = 1
    else:
        total = len(word1)
        longer = 2

    for i in range(total):
        ret += word1[i]
        ret += word2[i]

    if longer == 1:
        ret += word1[total-len(word2):]

    if longer == 2:
        ret += word2[total-len(word1):]

    return ret

def main():
    print(mix("aaaaaaaaaa", "bbb"))

main()