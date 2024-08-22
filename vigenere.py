# Implementing Vigenere Cipher in Python


def vigenere(message, key, direction=1):
    # Initialize the key index, alphabet and the final message
    key_index = 0
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    final_message = ""

    for char in message.lower():

        # Append any non-letter character to the message
        if not char.isalpha():
            final_message += char
        else:
            # Find the right key character to encode/decode
            key_char = key[key_index % len(key)]
            key_index += 1

            # Define the offset and the encrypted/decrypted letter
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset * direction) % len(alphabet)
            final_message += alphabet[new_index]

    # Return the final message
    return final_message


# Main function to demonstrate the Caesar cipher encryption and decryption
def main():
    while True:  # Infinite loop to keep the program running unit exit option is chosen
        # Prompt user for encryption, decryption or exit option
        choice = int(
            input(
                "\n1. Encryption \n2. Decryption \n3. Exit \nChoose one of the above option: "
            )
        )
        match (choice):
            case 1:  # User chose encryption
                # Prompt user for text and key input
                text = input("Enter the text to encrypt: ")
                custom_key = input("Enter the key: ")
                encrypted_text = vigenere(text, custom_key, 1)  # Encrypt the text
                # Display the original and encrypted text
                print(f"\nPlain text: {text}")
                print(f"Encrypted text: {encrypted_text}")

            case 2:  # User chose decryption
                # Prompt user for text and key input
                text = input("Enter the text to decrypt: ")
                custom_key = input("Enter the key: ")
                decrypted_text = vigenere(text, custom_key, -1)  # Decrypt the text
                # Display the original and decrypted text
                print(f"\nPlain text: {text}")
                print(f"Decrypted text: {decrypted_text}")

            case 3:  # User chose to exit
                exit()  # Exit the program

            case _:  # User entered an invalid option
                print("Invalid Option. Choose a correct option.")


if __name__ == "__main__":
    main()  # Entry point of the program
