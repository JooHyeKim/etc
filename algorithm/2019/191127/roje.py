def solution(begin,target,words):
    ans_cnt = 0
    # target이 words에 존재하지 않으면 바로 return 0
    if target not in words:
        return 0
    # target이 words에 존재할 때
    else:
        # words에 단어들이 존재할때까지
        while(len(words) != 0):
            for word in words:
                count = 0
                for idx in range(len(begin)):
                    if begin[idx] != word[idx]:
                        count += 1
                    if count == 2:
                        break
                if count == 1:
                    temp = word
                    words.remove(word)
            ans_cnt += 1
            if target == temp:
                return ans_cnt
            else:
                begin = temp
    return ans_cnt
