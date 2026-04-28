import rsa

# 生成RSA密钥
def generate_keys():
    (public_key, private_key) = rsa.newkeys(512)
    with open("public.pem", "wb") as f:
        f.write(public_key.save_pkcs1())
    with open("private.pem", "wb") as f:
        f.write(private_key.save_pkcs1())

# 加密
def encrypt_message(message, public_key):
    return rsa.encrypt(message.encode(), public_key)

# 解密
def decrypt_message(encrypted, private_key):
    return rsa.decrypt(encrypted, private_key).decode()

if __name__ == "__main__":
    generate_keys()
    print("密钥生成完成 public.pem 和 private.pem 已生成")