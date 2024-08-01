def solution(s):
    # 숫자에 대응되는 영단어를 사전으로 정의
    num_words = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
    }
    
    # 문자열 내 영단어를 숫자로 치환
    for word, num in num_words.items():
        s = s.replace(word, num)
    
    # 최종적으로 변환된 문자열을 정수로 변환하여 반환
    return int(s)