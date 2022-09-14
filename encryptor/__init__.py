import hashlib

from cryptography.fernet import Fernet

class encryptor:
	def encrypt(text: bytes, key: str) -> str:
		password = hashlib.sha256(key.encode())
		f = Fernet(f'{password.hexdigest()[0:43]}=')
		encrypted_text = f.encrypt(text)
		return encrypted_text.decode()

	def decrypt(text: str, key: str) -> bytes:
		password = hashlib.sha256(key.encode())
		f = Fernet(f'{password.hexdigest()[0:43]}=')
		encrypted_text = f.decrypt(text.encode())
		return encrypted_text