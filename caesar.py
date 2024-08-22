# Implementing Caesar Cipher in Python


# Function to encrypt a message using Caesar cipher
def caesar_encrypt(message, offset, alphabet):
    encrypted_text = ""  # Initialize the encrypted text
    # Iterate through each character in the message
    for char in message.lower():
        # Append any non-letter character to the encrypted text
        if not char.isalpha():
            encrypted_text += char
        # Encrypt the letter using the Caesar cipher algorithm
        else:
            index = alphabet.find(char)
            new_index = (index + offset) % len(alphabet)
            encrypted_text += alphabet[new_index]

    # Return the encrypted text
    return encrypted_text


# Function to decrypt a message encrypted with Caesar cipher
def caesar_decrypt(message, offset, alphabet):
    decrypted_text = ""  # Initialize the decrypted text
    # Iterate through each character in the message
    for char in message.lower():
        # Append any non-letter character to the decrypted text
        if not char.isalpha():
            decrypted_text += char
        # Decrypt the letter using the Caesar cipher algorithm
        else:
            index = alphabet.find(char)
            new_index = (index - offset) % len(alphabet)
            decrypted_text += alphabet[new_index]

    # Return the decrypted text
    return decrypted_text


# Main function to demonstrate the Caesar cipher encryption and decryption
def main():
    alphabet = "abcdefghijklmnopqrstuvwxyz"  # Define the alphabet used for encryption
    while True:  # Infinite loop to keep the program running until exit option is chosen
        # Prompt user for encryption, decryption or exit option
        choice = int(
            input(
                "\n1. Encryption \n2. Decryption \n3. Exit \nChoose one of the above option: "
            )
        )
        match (choice):
            case 1:  # User chose encryption
                # Prompt user for text and shift input
                text = input("Enter the text to encrypt: ")
                shift = int(input("Enter the shift value: "))
                encrypted_text = caesar_encrypt(
                    text, shift, alphabet
                )  # Encrypt the text
                # Display the original and encrypted text
                print("\nPlain text: ", text)
                print("Encrypted text: ", encrypted_text)

            case 2:  # User chose decryption
                # Prompt user for text and shift input
                text = input("Enter the text to decrypt: ")
                shift = int(input("Enter the shift value: "))
                decrypted_text = caesar_decrypt(
                    text, shift, alphabet
                )  # Decrypt the text
                # Display the original and decrypted text
                print("\nPlain text: ", text)
                print("\nDecrypted text: ", decrypted_text)

            case 3:  # User chose to exit
                exit()  # Exit the program

            case _:  # User entered an invalid option
                print("Invalid Option. Choose a correct option.")


if __name__ == "__main__":
    main()  # Entry point of the program
