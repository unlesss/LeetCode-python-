def min_changes(self, n: int, k: int) -> int:
    return -1 if (n & k) != k else (n ^ k).bit_count()
