
def brute_waviness(x):
    s = list(map(int, str(x)))
    if len(s) < 3:
        return 0
    res =0
    for i in range(1, len(s)-1):
        prev = s[i-1]
        curr = s[i]
        next_d = s[i+1]
        if (curr > prev and curr > next_d) or (curr < prev and curr < next_d):
            res +=1
    return res

print("brute_waviness(4848):", brute_waviness(4848))
print("brute_waviness(120):", brute_waviness(120))
print("brute_waviness(121):", brute_waviness(121))
print("brute_waviness(130):", brute_waviness(130))
