
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

def count_waviness_brute(x):
    total = 0
    for i in range(1, x+1):
        total += brute_waviness(i)
    return total

print("count_waviness_brute(4847):", count_waviness_brute(4847))
print("count_waviness_brute(4848):", count_waviness_brute(4848))
print("difference:", count_waviness_brute(4848) - count_waviness_brute(4847))
