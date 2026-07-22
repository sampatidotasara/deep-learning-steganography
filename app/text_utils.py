import base64
import hashlib
from cryptography.fernet import Fernet
from PIL import Image

DELIMITER = "#####"


def generate_key(password):
    key = hashlib.sha256(password.encode()).digest()
    return base64.urlsafe_b64encode(key)


def encrypt_message(message, password):
    cipher = Fernet(generate_key(password))
    return cipher.encrypt(message.encode()).decode()


def decrypt_message(message, password):
    cipher = Fernet(generate_key(password))
    return cipher.decrypt(message.encode()).decode()


def text_to_binary(text):
    return ''.join(format(ord(i), '08b') for i in text)


def encode_text(image, message, password=""):

    image = image.convert("RGB")

    if password:
        message = encrypt_message(message, password)

    message += DELIMITER

    binary = text_to_binary(message)

    pixels = image.load()

    width, height = image.size

    index = 0

    for y in range(height):

        for x in range(width):

            r, g, b = pixels[x, y]

            if index < len(binary):
                r = (r & ~1) | int(binary[index])
                index += 1

            if index < len(binary):
                g = (g & ~1) | int(binary[index])
                index += 1

            if index < len(binary):
                b = (b & ~1) | int(binary[index])
                index += 1

            pixels[x, y] = (r, g, b)

            if index >= len(binary):
                return image

    raise ValueError("Message too large.")


def decode_text(image, password=""):

    image = image.convert("RGB")

    pixels = image.load()

    width, height = image.size

    bits = ""

    for y in range(height):
        for x in range(width):

            r, g, b = pixels[x, y]

            bits += str(r & 1)
            bits += str(g & 1)
            bits += str(b & 1)

    chars = []

    for i in range(0, len(bits), 8):

        byte = bits[i:i+8]

        if len(byte) < 8:
            break

        chars.append(chr(int(byte, 2)))

        text = "".join(chars)

        if DELIMITER in text:

            text = text.replace(DELIMITER, "")

            if password:
                try:
                    text = decrypt_message(text, password)
                except Exception:
                    return "❌ Wrong password."

            return text

    return ""
