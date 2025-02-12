def custom_max(n1, n2: int) -> int:
    """Return the maximum of two numbers."""
    if n2 > n1:
        return n2
    elif n1 > n2:
        return n1
    else:
        return "The numbers are equal."


def max_three(n1, n2, n3: int) -> int:
    """Return the maximum of three numbers."""
    n = custom_max(n1, n2)
    return custom_max(n, n3)


if __name__ == "__main__":
    print(custom_max(10, 20))  # 20
    print(custom_max(20, 10))  # 20
    print(custom_max(10, 10))  # Equal
