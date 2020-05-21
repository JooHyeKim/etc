def solution(answers):
    answer = []
    questions = len(answers)
    num1 = 0
    num2 = 0
    num3 = 0
    #������ 1,2,3�� ���� ����Ʈ
    student1 = [1,2,3,4,5]
    student2 = [2,1,2,3,2,4,2,5]
    student3 = [3,3,1,1,2,2,4,4,5,5]

    #������ 1,2,3�� ����� ������ ��
    for i in range(questions):
        if answers[i] == student1[i%len(student1)]:
            num1 += 1
        if answers[i] == student2[i%len(student2)]:
            num2 += 1
        if answers[i] == student3[i%len(student3)]:
            num3 += 1
            
    #���� ������ ���� ���� ���� ��
    MAX = max(num1, num2, num3)
    if num1 == MAX:
        answer.append(1)
    if num2 == MAX:
        answer.append(2)
    if num3 == MAX:
        answer.append(3)

    return answer
