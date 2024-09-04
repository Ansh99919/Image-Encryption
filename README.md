How It Works
Encrypting the Image:

The script loads the image and converts it into a NumPy array.
It then applies a basic mathematical operation (adding a key) to each pixel value.
The pixel values are wrapped around using modulo 256 to ensure they remain within the valid range (0-255).
The pixels are then flipped vertically to add an additional layer of encryption.
The encrypted image is saved as encrypted_image.png.
Decrypting the Image:

The script loads the encrypted image and reverses the pixel flipping.
It then reverses the mathematical operation (subtracting the key) to recover the original pixel values.
The decrypted image is saved as decrypted_image.png.
Running the Script
Replace 'input_image.png' with the path to your image file when running the script.
The key used for encryption and decryption should be the same to correctly recover the original image.
