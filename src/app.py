def add(a: int, b: int) -> int:
    """Return the sum of two integers."""
    return a + b


if __name__ == "__main__":
    # Local quick test (not used in CI)
    print(add(2, 3) + add(2, 5))
