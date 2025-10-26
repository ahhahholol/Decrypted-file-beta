import requests
import os
from cryptography.fernet import Fernet

def download_file(url, output_path):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(output_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
    return output_path

def decrypt_file(input_path, output_path):
    key = Fernet.generate_key()
    fernet = Fernet(key)
    with open(input_path, 'rb') as f:
        encrypted_data = f.read()
    decrypted_data = fernet.decrypt(encrypted_data)
    with open(output_path, 'wb') as f:
        f.write(decrypted_data)
    return output_path

def main():
    file_url = input("Enter the file link (e.g., IPA or any app/game file): ")
    downloaded_file = download_file(file_url, "downloaded_file")
    print(f"Downloaded file to {downloaded_file}")
    decrypted_file = decrypt_file(downloaded_file, "decrypted_file")
    print(f"Decrypted file saved to {decrypted_file}")
    print("Decrypted file is ready to be sent or used.")

if __name__ == "__main__":
    main()
