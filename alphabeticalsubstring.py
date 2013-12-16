def solve(s):
    first = 0
    last = 0
    max_s =[]
#max_s.append(s[0])
for i in range(len(s)+1):
    if  i !=(len(s)) and ord(s[i])>= ord(s[i-1]):
        last = i
    else:
        print first,last
        max_s.append(s[first:last+1])
        first = i
        last = i

    siz = len(max_s[0])
    ret = max_s[0]
    for i in max_s:
        if len(i) > siz:
            siz = len(i)
            ret = i
    print max_s
    return ret     
