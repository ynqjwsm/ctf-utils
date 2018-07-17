import hashlib

# 待加密信息
str = 'aaa'

# 创建md5对象
hl = hashlib.sha1()

# Tips
# 此处必须声明encode
# 若写法为hl.update(str)  报错为： Unicode-objects must be encoded before hashing
hl.update(str.encode(encoding='utf-8'))

print('SHA-1加密前为 ：' + str)
print('SHA-1加密后为 ：' + hl.hexdigest())