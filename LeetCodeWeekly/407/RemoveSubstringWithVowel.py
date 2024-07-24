def does_alice_win(self, s: str) -> bool:
    return any(c in "aeiou" for c in s)
