import hashlib


# md5加密
md5 = hashlib.md5()
md5.update('gaohuan'.encode('utf8'))
print(md5.hexdigest())


md5_ = hashlib.md5()
md5_.update('gao'.encode('utf8'))
md5_.update('huan'.encode('utf8'))
print(md5_.hexdigest())
print(len(md5_.hexdigest()))

# sha1
sha1 = hashlib.sha1()
sha1.update('gaohuan'.encode('utf8'))
print(sha1.hexdigest())

sha1_ = hashlib.sha1()
sha1_.update('gao'.encode('utf8'))
sha1_.update('huan'.encode('utf8'))
print(sha1_.hexdigest())
print(len(sha1_.hexdigest()))