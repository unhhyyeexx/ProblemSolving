def solution(expressions):
    def convert(n, q):
        if n == 0:
            return '0'
        rev_base = ''

        while n > 0:
            n, mod = divmod(n, q)
            rev_base += str(mod)

        return rev_base[::-1] 

    answer = []
    real = 0
    
    able = 0
    for exp in expressions:
        exp = exp.split(" ")
        a,op,b,_,c = exp
        
        if len(a) == 1:
            a = '0' + a
        if len(b) == 1:
            b = '0' +b
        if len(c) < 3:
            c = ('0'*(3-len(c))) + c
        if c == '00X':
            answer.append(exp)
            able = max(able, max(int(a[0]), int(a[1]), int(b[0]), int(b[1])) + 1)
            continue
        
        if real:
            continue
        cand = max(int(a[0]), int(a[1]), int(b[0]), int(b[1]), int(c[0]), int(c[1]), int(c[2])) + 1
        if op == "+":
            if (int(a[1]) + int(b[1]) == int(c[2])):
                cand = max(cand, int(c[2]) + 1)
                if (int(a[0]) + int(b[0]) == int(c[1])):
                    cand = max(cand, int(c[2])+1)
                else :
                    real = (int(a[0]) + int(b[0])) - int(c[1])
            else :
                real = (int(a[1]) + int(b[1])) - int(c[2])
                
        else :
            if (int(a[1]) - int(b[1]) == int(c[2])):
                cand = max(cand, int(a[1])+1, int(a[0])+1)
            else:
                if (10+int(a[1]) - int(b[1]) == int(c[2])):
                    cand = max(cand, int(b[1])+1, int(a[0])+1)
                else:
                    real = int(c[2]) + int(b[1]) - int(a[1])
        if real:
            continue
        else :
            able = max(able, cand)
    print(able)

    result = []
    if real:
        for ex in answer:
            a, op, b, eq, c = ex
            ia = int(a, real)
            ib = int(b, real)
            if (op == '+'):
                c = convert(ia+ib, real)
            else:
                c = convert(ia-ib, real)
            result.append(" ".join([a,op,b,eq,c]))
    
    else:
        for ex in answer:
            a, op, b, eq, c = ex
            opresult = set()
            for i in range(able, 10):
                ia = int(a, i)
                ib = int(b, i)
                if (op == '+'):
                    c = convert(ia+ib, i)
                else:
                    c = convert(ia-ib, i)
                opresult.add(c)
            if len(opresult) == 1:
                result.append(" ".join([a,op,b,eq,c]))
            else:
                result.append(" ".join([a,op,b,eq,'?']))

            
    return result