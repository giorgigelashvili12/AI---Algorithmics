def f(n, b):
    # monacemis gadamowmeba
    if n == 0:
        return "0"
    
    negative = n < 0

    if negative:
        n = abs(n)

    v = []
    #monacemis damushaveba
    r = n % b
    v.append(str(r))

    v.reverse()
    result = ''.join(v)

    if negative: 
        result = '-' + result 
    return result

print(f(45, 3))
print(f(25, 6))
print(f(-10, 3))