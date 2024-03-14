import os

from PIL import Image


def swap_pixels(r, g, b):
    return g, r, b

def encrypt_image(image_path):
    original_img = Image.open(image_path)

    img = original_img.copy()

    width, height = img.size

    for x in range(width):
        for y in range(height):

            r, g, b = img.getpixel((x, y))

            g, r = r, g

            img.putpixel((x, y), (r, g, b))

    return img

def decrypt_image(image_path):

    encrypted_img = Image.open(image_path)

    img = encrypted_img.copy()

    width, height = img.size

    for x in range(width):
        for y in range(height):
            r, g, b = img.getpixel((x, y))

            g, r = r, g

            img.putpixel((x, y), (r, g, b))

    return img

def main():
    while True:
        image_path = r"E:\Prodigy Infotech\building.jpg"

        # Choose operation
        operation = input("Choose an operation (encrypt, decrypt, exit): ")

        if operation == 'encrypt':
            encrypted_image = encrypt_image(image_path)
            encrypted_path = "encrypted_" + os.path.basename(image_path)
            encrypted_image.save(encrypted_path)
            print(f"Image encrypted (swapped red and green channels) and saved as '{encrypted_path}'")

        elif operation == 'decrypt':
            decrypted_image = decrypt_image("encrypted_" + os.path.basename(image_path))
            decrypted_path = "decrypted_" + os.path.basename(image_path)
            decrypted_image.save(decrypted_path)
            print(f"Image decrypted (swapped back red and green channels) and saved as '{decrypted_path}'")

        elif operation == 'exit':
            print("Exiting the program.")
            break

        else:
            print("Invalid operation. Please choose encrypt, decrypt, or exit.")

if __name__ == "__main__":
    main()
