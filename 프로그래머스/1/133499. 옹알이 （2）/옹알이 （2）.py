def solution(babbling):
    valid_sounds = ["aya", "ye", "woo", "ma"]
    count = 0

    for word in babbling:
        for sound in valid_sounds:
            # 연속된 같은 발음을 방지하기 위해 sound + sound로 된 부분이 있는지 확인
            if sound * 2 in word:
                break
            # 발음 가능한 단어일 경우, 해당 발음을 단어에서 제거
            word = word.replace(sound, " ")
        # 공백으로만 남으면 발음 가능한 단어로 카운트 증가
        if word.strip() == "":
            count += 1

    return count
