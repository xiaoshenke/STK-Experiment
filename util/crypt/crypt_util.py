#!/usr/bin/python
# coding=utf-8
import sys
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
AES_SECRET_KEY = 'secret5432154321'

class AES_ENCRYPT(object):
    def __init__(self,key=AES_SECRET_KEY):
        self.key = self.format_key(key)
        self.mode = AES.MODE_CBC

    def format_key(self,key):
	if len(key) > 16:
		return key[:16]
	count = len(key)
	length = 16
	add = length - (count % length)
	key = key + ('0' * add)
	return key
     
    #加密函数，如果text不是16的倍数【加密文本text必须为16的倍数！】，那就补足为16的倍数
    def encrypt(self, text):
        cryptor = AES.new(self.key, self.mode, self.key)
        #这里密钥key 长度必须为16（AES-128）、24（AES-192）、或32（AES-256）Bytes 长度.目前AES-128足够用
        length = 16
        count = len(text)
        add = length - (count % length)
        text = text + ('\0' * add)
        self.ciphertext = cryptor.encrypt(text)
        #因为AES加密时候得到的字符串不一定是ascii字符集的，输出到终端或者保存时候可能存在问题
        #所以这里统一把加密后的字符串转化为16进制字符串
        return b2a_hex(self.ciphertext)
     
    #解密后，去掉补足的空格用strip() 去掉
    def decrypt(self, text):
        cryptor = AES.new(self.key, self.mode,self.key)
        plain_text = cryptor.decrypt(a2b_hex(text))
        return plain_text.rstrip('\0')
 
if __name__ == '__main__':
    aes_encrypt = AES_ENCRYPT("12345678901234567890")      #初始化密钥
    customer_id = "hello world"
    e = aes_encrypt.encrypt(customer_id)
    d = aes_encrypt.decrypt(e)
    print customer_id
    print "after encrypt:%s"%e
    print "after decrypt:%s"%d

