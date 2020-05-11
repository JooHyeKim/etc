def solution(maps):
    answer = 0
    directs = [(0,1),(1,0),(0,-1),(-1,0)] #�̵����� ����Ʈ
    n = len(maps) - 1
    m = len(maps[0]) - 1 #���� ũ��
    queue = []
    queue.append([0,0,1]) #������ ������ġ, count=1�� ����
    
    while queue:
        x, y, count = queue.pop(0) #������ġ
        #��θ��� count���� �ٸ��� ������ �� ����Ʈ�� �����ش�
        maps[x][y] = 0 #������ �� ������ �����
        for dx, dy in directs: #��,��,��,��� �̵�
            px, py = x + dx, y + dy
            #����� ������ ���� ������ ��θ� ���
            if px == n and py == m:
                return count + 1
            #�ִܰŸ��̹Ƿ� ������ ���� ������ �����
            if 0 <= px <= n and 0 <= py <= m and maps[px][py] == 1:
                maps[px][py] = 0
                queue.append([px, py, count+1])
    return -1
