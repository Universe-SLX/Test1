def bisect (a , x , lo = 0 , hi = None ) :
    if hi is None :
        hi = len (a)
    while lo < hi :
        mid = (lo + hi) >>1
        if x < a[mid] :
            hi = mid
        else :
            lo = mid +1
    return lo

a = [1,9,9,9,200,500]
print(bisect(a, 9))  # Output: 4
print(bisect(a, 700)) # Output: 6