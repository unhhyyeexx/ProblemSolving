def changeTime(time):
    return int(time[:2]) * 60 + int(time[3:])

def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    # 모든 시간 초 단위(정수)로 변환
    video_len = changeTime(video_len)
    pos = changeTime(pos)
    op_start = changeTime(op_start)
    op_end = changeTime(op_end)
    
    for command in commands:
        # 오프닝 건너뛰기
        if op_start <= pos < op_end :
            pos = op_end
        
        if command == 'prev':
            pos = pos - 10 if pos > 10 else 0
        elif command == 'next':
            pos = pos + 10 if pos < video_len-10 else video_len
        
        # 오프닝 건너뛰기
        if op_start <= pos < op_end :
            pos = op_end
    
    answer = str(pos//60).zfill(2) + ':' + str(pos%60).zfill(2)
    return answer