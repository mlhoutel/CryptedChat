# RSA encryption/decryption algorithm

# Euclide algorithm
def pgcd(a, b):
	while b > 0:
		a, b = b, a%b
	return a

# Modular reduction (a**k mod n)
def emr(a, k, n):
	if k == 0:
		return 1
	else:
		if k%2 == 0:
			return pow(emr(a, k//2, n), 2, n)
		else:
			return pow(a*emr(a, (k-1)//2, n), 2, n)

# Multiplicative inverse (ed-1//phi)
def mui(e,phi):
	d=1
	while ((e*d)%phi != 1):
		d=d+1
	return d
	
class Person:
	def __init__(self,p,q,e):
		self.p, self.q = p,q
		self.phi = (p-1)*(q-1) 
		self.d = mui(e ,self.phi)
		self.n = p*q
		self.e = e
	
	def publicKey(self):
		return (self.n,self.e)
	
	def privateKey(self):
		return (self.n,self.d)
	
	def toString(self):
		print(self.p,self.q,self.d,self.n,self.e)
	
	def encrypt(self, num):
		return pow(num, self.e, self.n)
	
	def decrypt(self, num):
		return pow(num, self.d, self.n)
	
	def encryptMsg(self, msg):
		return [self.encrypt(ord(char)) for char in msg]
	
	def decryptMsg(self, msg):
		chars = [chr(self.decrypt(char)) for char in msg]
		return "".join(chars)
		
sender = Person(41, 53, 17)
receiver = Person(41,53,3)
sender.toString()
print(sender.publicKey())

msg="message"
encrypted=sender.encryptMsg(msg)
decrypted=sender.decryptMsg(encrypted)
print(msg,"=>",encrypted,"=>",decrypted)

