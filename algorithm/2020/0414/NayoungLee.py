def solution(food_times, k):
    answer = 0
    first = 0
    orin_num = 0
    check = 0 #num2�� ���� ���� ã�� ����
    #�Դ½ð��� ������ ����ϴ� ���ο� �迭 ����
    new_f_t = []
    for i in range(len(food_times)):
        new_f_t.append([food_times[i],i+1])
    #new_f_t.sort()
    food_times.sort()

    #k�� �ð� ��
    while True:
        first += food_times[0] #�귯�� �ð� ����
        num = food_times[0] * len(food_times)
        
        #k���� ���� �ð� ���̱�
        if k > num:
            k -= num
        elif k == num:
            for u in range(len(new_f_t)):
                if new_f_t[u][0] < orin_num:
                    del new_f_t[u][0]
            answer = new_f_t[0][1]
            break
        else:
            num2 = k % len(food_times)
            for j in range(len(new_f_t)):
                if new_f_t[j][0] >= orin_num:
                    check += 1
                    if check == num2:
                        break
                    continue
                check += 1
            answer = new_f_t[check][1]
            break
        

        del food_times[0] #0��° ������ ����
        #���� ������ ���� �� -1 ��ȯ
        if not food_times:
            answer = -1
            break
        orin_num = food_times[0]
        food_times[0] -= first #0��°�� ������ �귯�� �ð��� ���ش�.

    return answer
