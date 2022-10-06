def solution(n, lost, reserve):
    origin = n - len(lost + reserve)
    max = len(reserve) + origin
    
    for i in reserve:
        if( ( (i-1) in lost ) or ( (i+1) in lost) ) :
            reserve.remove(i)
            max += 1
        else:
            continue
        if (len(reserve) == 0):
            break
    return max

print(solution(5, [2,4], [1,3,5]))