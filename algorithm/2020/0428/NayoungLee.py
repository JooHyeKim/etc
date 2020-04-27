def solution(n, t, m, timetable):
    answer = ''
    #timetable ������ ȯ�� �� ������� �����ϱ�
    timetable = [int(time[:2])*60 + int(time[3:5]) for time in timetable]
    timetable.sort()

    total = len(timetable) #�¿��� �� �� �ο� ��
    shuttle = 0 #��Ʋ������ ź �ο� ��
    last_bus = 0 #������ ���� �ð�
    last_bus = 540 + (n-1)*t #������ ���� �ð�(������ ȯ��)

    for i in range(n):
        bus_time = 540 + t * i #���� ��� �ð�
        if total < m: #�ο� ���� ���ٸ� ������ ���� �ð����� ����
            answer = '%02d:%02d' %(last_bus // 60, last_bus % 60)
            break
        
        while True:
            if timetable[0] <= bus_time:
                shuttle += 1 #���� �ð����� ���� �� ����� �� �� �¿��
                if shuttle == m:
                    break
                if len(timetable) == 0:
                    break
                if len(timetable) == 1:
                    del timetable[0]
                    break
                del timetable[0]
            else:
                break
            
        if i == n-1: #������ ������ ��
            if shuttle == m:
                timetable[0] -= 1
                answer = '%02d:%02d' %(timetable[0] // 60, timetable[0] % 60)
                break
            else:
                answer = '%02d:%02d' %(bus_time // 60, bus_time % 60)
                break
        else:
            if len(timetable) == 0: #������ ������ �ƴѵ� ��⿭�� ���ٸ�
                answer = '%02d:%02d' %(last_bus // 60, last_bus % 60)
                break
            if shuttle == m:
                del timetable[0]
            shuttle = 0 #���� �ο� �ʱ�ȭ
    return answer
