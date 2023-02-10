from string import ascii_uppercase

realname = list(input())
changename = realname

alphabet = list(ascii_uppercase)
realphabet = alphabet.reverse()
result = 0
up = 0
down = 0
left = 0
right = 0

def solution(changename):
    count = len(changename)
    for i in range(count):
        changename[i] = 'A'
        if realname[i] == changename[i]:
            if realname[i+1] == count-1:
                left += 1
            else:
            right += 1
        if realname[i] != changename[i]:
            for a in alphabet:
                if a == realname[i]:
                    break
                    right += 1
                up += 1
            for b in alphabet:
                if a == realname[i]:
                    break
                    right += 1
                down += 1
            result += min(up,down)
            
solution(changename)
print(result+left+right)
        
            
            