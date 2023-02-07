def solution(lottos, win_nums):
    same = 0
    prize = [6, 6, 5, 4, 3, 2, 1]
    zerocnt = lottos.count(0)
    for n in win_nums:
        if n in lottos:
            same += 1
    return [prize[zerocnt + same], prize[same]]