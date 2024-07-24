def max_ops_moving_ones(self, s: str) -> int:
    ans = cnt1 = 0
    for i, c in enumerate(s):
        if c == '1':
            cnt1 += 1
        elif i and s[i - 1] == '1':
            ans += cnt1
    return ans
