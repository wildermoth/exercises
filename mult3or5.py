def main(maximum_number: int) -> int:
    """Takes an int and gets the sum of all multiples of 3 or 5 below it.

    Args:
        maximum_number (int): the users input

    Returns:
        int: the sum of all multiples of 3 or 5 below the number"""

    total_sum: int = 0

    for current_number in range(1, maximum_number):
        is_divisible_by_3: bool = current_number % 3 == 0
        is_divisible_by_5: bool = current_number % 5 == 0

        if is_divisible_by_3 or is_divisible_by_5:
            total_sum += current_number

    return total_sum


if __name__ == "__main__":
    print(main(10))
    print("clean slate")
