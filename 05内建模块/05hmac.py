import hmac


mesage = b'gaohuan'
key = 'salt'.encode('utf8')
h = hmac.new(key, mesage, digestmod='MD5')
print(h.hexdigest())


k = 'salt'.encode('utf8')
h2 = hmac.new(k, b'gao', digestmod='MD5')
h2.update(b'huan')

print(h2.hexdigest())