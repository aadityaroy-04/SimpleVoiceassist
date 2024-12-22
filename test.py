from cryptography.fernet import Fernet

# Generate a random encryption key
key = Fernet.generate_key()

# Create a Fernet cipher object with the key
cipher = Fernet(key)

# Message to be encrypted
message = "hello I am ai"

# Encrypt the message
encrypted_message = cipher.encrypt(message.encode())

# Print the encrypted message and the key
print("Encrypted Message:", encrypted_message)
print("Encryption Key:", key)