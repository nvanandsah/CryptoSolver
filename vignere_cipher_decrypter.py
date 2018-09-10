def solve(key,text):
	key = key.lower() + key +'()1234567890 ,.-'
	t  =  'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ()1234567890 ,.-'
	value = ''
	for i in text:
		value = value + t[key.find(i)]
	return value


Cipher_key = 'BIRDWATCHNGEFJKLMOPQSUVXYZ'
Cipher_text = '''Qcw Hjdhbj lbobdhpw aeyrbqrcwo (Qwolphlckjw lbobdhph) hp b fwdhsf-phzwd lbppwohjw ihod jbqhuw qk Bphb qcbq hp vhdwey dhpqohisqwd. Bp qcw tekibe lklsebqhkj hp rkjphdwowd
pqbiew, hq cbp iwwj ehpqwd bp Ewbpq Rkjrwoj kj qcw HSRJ Owd Ehpq phjrw 2004. Hq hp jbqhuw qk qcw Hjdhbj psirkjqhjwjq, Rwjqobe Bphb bjd Fybjfbo'''
print(solve(Cipher_key,Cipher_text))