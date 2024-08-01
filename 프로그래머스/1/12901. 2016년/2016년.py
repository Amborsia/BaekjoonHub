def solution(a, b):
    # 요일 리스트, 금요일부터 시작
    days_of_week = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    days_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = sum(days_in_month[:a - 1]) + b - 1
    
    return days_of_week[days % 7]

print(solution(5, 24))