input = "abcba"

# 특정구조가 반복되는 양상을 보였을때에
# 문제를 좁혀 나간다!
# 탈출조건 is Must
# 소주만병만주소
# 주만병만주
# 만병만

def is_palindrome(string):
    if len(string) <= 1:
        return True

    if string[0] != string[-1]:
        return False

    return is_palindrome(string[1:-1])


print(is_palindrome(input))