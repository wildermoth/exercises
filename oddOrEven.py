def odd_or_even(provided_number: int) -> str: 
    """Takes an int and returns a string of "odd" or "even" depending on the number.
    
    Args:
        provided_number (int): the users input
        
    Returns:
        str: "odd" or "even" depending on the number"""
    
    if not isinstance(provided_number, int):
        return "Provide an Integer"

    is_even: bool = provided_number % 2 == 0

    if is_even:
        return "Even"
    else:
        return "Odd"
    
def main() -> None:
    print(odd_or_even(1.5))

if __name__ == "__main__":
    main()
    print("conflict feature")