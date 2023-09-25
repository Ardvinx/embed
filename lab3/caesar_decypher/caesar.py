def caesar_decrypt(ciphertext):
    # Define a list of common English words for checking decryption results
    common_words = ["the", "and", "to", "in", "it", "is", "that", "you", "was", "for"]

    # Iterate through all possible keys (0 to 25)
    for key in range(26):
        decrypted_text = ""

        # Decrypt the message using the current key
        for char in ciphertext:
            if char.isalpha():
                # Shift the character by the key value and wrap around the alphabet
                shifted_char = chr(((ord(char) - ord("a") - key) % 26) + ord("a"))
                decrypted_text += shifted_char
            else:
                decrypted_text += char

        # Check if the decrypted text contains common words
        words = decrypted_text.split()
        common_word_count = sum(1 for word in words if word.lower() in common_words)

        # If the decryption contains at least two common words, consider it as a possible result
        if common_word_count >= 2:
            return key, decrypted_text

    # If no meaningful result is found, return None
    return None, None


# Example usage
encrypted_message = "iqfihhih"
key, decrypted_message = caesar_decrypt(encrypted_message)
if key is not None:
    print(f"Key: {key}")
    print(f"Decrypted Message: {decrypted_message}")
else:
    print("No valid decryption found.")
