"""
Check if card number is valid or not using Luhn Algorithm
"""


def verify_card_number(card_number):
    # Initialize sum of digits at odd positions and sum of digits at even positions
    sum_of_odd_digits = 0
    sum_of_even_digits = 0

    # Reverse the card number to facilitate processing from the rightmost digit
    card_number_reversed = card_number[::-1]

    # Extract digits at odd and positions in the reversed card number
    odd_digits = card_number_reversed[::2]
    even_digits = card_number_reversed[1::2]

    # Sum up the digits at odd positions
    for digit in odd_digits:
        sum_of_odd_digits += int(digit)

    # Double the digits at even positions and sum up the digits
    for digit in even_digits:
        number = int(digit) * 2
        # If doubling the digit results in a number >= 10, add the digits of the result
        if number >= 10:
            number = (number // 10) + (number % 10)
        sum_of_even_digits += number

    # Calculate the total sum of digits
    total = sum_of_odd_digits + sum_of_even_digits

    # Return True if the total modulo 10 is 0 (valid card), else False
    return total % 10 == 0


def main():
    # Prompt user for card number input
    card_number = input("Enter the card number to verify: ")

    # Remove dashes and spaces for clean processing
    card_translation = str.maketrans({"-": "", " ": ""})
    translated_card_number = card_number.translate(card_translation)

    # Verify the card number using Luhn's algorithm
    if verify_card_number(translated_card_number):
        print("VALID!")  # Card number is valid
    else:
        print("INVALID!")  # Card number is invalid


if __name__ == "__main__":
    main()  # Entry point of the program
