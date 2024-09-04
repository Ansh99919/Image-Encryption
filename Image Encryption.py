from PIL import Image
import numpy as np

def encrypt_image(image_path, key):
    # Open the image
    image = Image.open(image_path)
    image_array = np.array(image)
    
    # Encrypt the image by applying a mathematical operation
    encrypted_array = (image_array + key) % 256

    # Swap pixels
    encrypted_array = np.flipud(encrypted_array)

    # Create an encrypted image
    encrypted_image = Image.fromarray(np.uint8(encrypted_array))
    
    # Save the encrypted image
    encrypted_image.save('encrypted_image.png')
    print("Encryption complete. Encrypted image saved as 'encrypted_image.png'.")

def decrypt_image(image_path, key):
    # Open the encrypted image
    encrypted_image = Image.open(image_path)
    encrypted_array = np.array(encrypted_image)
    
    # Reverse pixel swapping
    decrypted_array = np.flipud(encrypted_array)

    # Decrypt the image by reversing the mathematical operation
    decrypted_array = (decrypted_array - key) % 256

    # Create the decrypted image
    decrypted_image = Image.fromarray(np.uint8(decrypted_array))
    
    # Save the decrypted image
    decrypted_image.save('decrypted_image.png')
    print("Decryption complete. Decrypted image saved as 'decrypted_image.png'.")

if __name__ == "__main__":
    # Example usage
    key = 42  # Example key for encryption/decryption
    encrypt_image('input_image.png', key)  # Replace 'input_image.png' with your image file
    decrypt_image('encrypted_image.png', key)
