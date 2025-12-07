from Crypto.Cipher import DES,AES
from Crypto.Util.Padding import pad, unpad

key_des = b'8bytekey'     # must be 8 bytes
cipher_des = DES.new(key_des, DES.MODE_ECB)
pt_des = b"HELLODES"
enc_des = cipher_des.encrypt(pad(pt_des, DES.block_size))
dec_des = DES.new(key_des, DES.MODE_ECB)
pt_back_des = unpad(dec_des.decrypt(enc_des), DES.block_size)
print("DES ->", enc_des, pt_back_des.decode())



key_aes = b'8bytekey8bytekey'     # must be 16 bytes
cipher_aes = AES.new(key_aes, AES.MODE_ECB)
pt_aes = b"HELLODES"
enc_aes = cipher_aes.encrypt(pad(pt_aes, AES.block_size))
dec_aes = AES.new(key_aes, AES.MODE_ECB)
pt_back_aes = unpad(dec_aes.decrypt(enc_aes), AES.block_size)
print("AES ->", enc_aes, pt_back_aes.decode())
