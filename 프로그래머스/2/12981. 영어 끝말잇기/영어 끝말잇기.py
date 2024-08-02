def solution(n, words):
    used = set()
    result = words[0][0]

    for i, word in enumerate(words):
        person = (i%n)+1
        turn = (i//n)+1

        if word in used or word[0] != result:
            return [person, turn]
        used.add(word)
        result = word[-1]

    return [0, 0]