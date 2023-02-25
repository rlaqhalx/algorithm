# Use STACK
s = "(())()"

def is_correct_parenthesis(string):
    # 구현해보세요!
    stack = []
    for i in range(len(string)):
        if string[i] == "(":
            stack.append(i)
        elif string[i] == ")":
            if len(stack) == 0:
                return False
            stack.pop();

    if len(stack) != 0:
        return False
    else:
        return True
    return


print(is_correct_parenthesis(s))  # True 를 반환해야 합니다!
print("정답 = True / 현재 풀이 값 = ", is_correct_parenthesis("(())"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis(")"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())))"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("())()"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())"))

# 1) 닫는 괄호가 나오면 바로 직전에 열린 괄호가 있는지 봐야 한다.
# 2) 열린 괄호들을 다 저장해놔야겠다.
#
# 바로 직전 데이터를 쌓는 좋은 자료구조가 있었죠. 바로 스택입니다!
#
# 문자열을 돌면서 문자가 "(" 이라면 스택에 쌓아놓습니다.
# 그리고 ")" 가 나오면, 직전 스택에 저장되어 있는지 확인합니다.
# 만약 없다면? 닫는 것은 있는데 여는 게 없으니 False 를 반환합니다.
# 만약 있다면 가장 상위의 원소를 제거하면 되겠죠.
#
# 이 과정을 쭉 반복하다가, 문자열이 끝났는데 아직 stack 이 남아있다?
# 그러면 닫아주는 게 부족했으니 False 입니다! 만약 전부 없어졌다면 True 를 반환하시면 됩니다.됩니다