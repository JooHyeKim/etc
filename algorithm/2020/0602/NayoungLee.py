timelist = []
for i in range(11):
    time = list(input().split())
    timelist.append(time)

timelist.sort() #�ð�����Ʈ ����
count = 0
penality = 0
verdicts = 0 
for j in range(len(timelist)):
    penality += int(timelist[j][0]) #�� ���������� �г�Ƽ���� ��
    count += penality #���ϰ��� �ϴ� �� �г�Ƽ�� ��
    verdicts += int(timelist[j][1]) #��Ǭ������ �г�Ƽ �߰�
    
answer = count + verdicts*20
print(answer)
