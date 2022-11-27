# 가위바위보
def solution(rsp):
    answer = ''
    for i in rsp:
        if i == '2':
            answer += '0'
        if i == '0':
            answer += '5'
        if i == '5':
            answer += '2'
    return answer
# 가위바위보 2번째 방법
def solution(rsp):
    answer = []
    rsp = list(rsp)
    for i in range(len(rsp)):
        if rsp[i] == '2':
            answer.append('0')
        if rsp[i] == '0':
            answer.append('5')
        if rsp[i] == '5':
            answer.append('2')
    answer = ''.join(answer)
    return answer

# 자릿수 더하기
def solution(n):
    answer = 0
    n = list(str(n))
    for i in range(len(n)):
        answer += int(n[i])
    return answer
