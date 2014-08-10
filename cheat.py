import Crypto.Cipher.AES as AES
 
 
### Data
cbckey1 = '140b41b22a29beb4061bda66b6747e14'
cbcct1 = '4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81'
 
cbckey2 = '140b41b22a29beb4061bda66b6747e14'
cbcct2 = '5b68629feb8606f9a6667670b75b38a5b4832d0f26e1ab7da33249de7d4afc48e713ac646ace36e872ad5fb8a512428a6e21364b0c374df45503473c5242a253'
 
ctrkey1 = '36f18357be4dbd77f050515c73fcf9f2'
ctrct1 = '69dda8455c7dd4254bf353b773304eec0ec7702330098ce7f7520d1cbbb20fc388d1b0adb5054dbd7370849dbf0b88d393f252e764f1f5f7ad97ef79d59ce29f5f51eeca32eabedd9afa9329'
 
ctrkey2 = '36f18357be4dbd77f050515c73fcf9f2'
ctrct2 = '770b80259ec33beb2561358a9f2dc617e46218c0a53cbeca695ae45faa8952aa0e311bde9d4e01726d3184c34451'
 
### Homework:
 
ckey1 = cbckey1.decode('hex')
ct1 = cbcct1.decode('hex')
 
ckey2 = cbckey2.decode('hex')
ct2 = cbcct2.decode('hex')
 
tk1 = ctrkey1.decode('hex')
tct1 = ctrct1.decode('hex')
 
tk2 = ctrkey2.decode('hex')
tct2 = ctrct2.decode('hex')
 
def strxor(s1, s2):
    return ''.join([ chr(ord(c1) ^ ord(c2)) for (c1, c2) in zip(s1, s2)])
 
 
class BlockAES:
    def __init__(self, key):
        self.key = key
        self.bs = 16
        self.aes = AES.new(key)
    
    def split_msg(self, msg):
        ms = [ msg[ self.bs*i : self.bs*(i+1) ] for i in range(len(msg)/self.bs + 1) ]
        while ms.count(''): ms.remove('')
        return ms
 
class CBC(BlockAES):
    def decrypt(self, msg):
        ms = self.split_msg(msg)
        pt = ''
        for i in xrange(len(ms) - 1, 0, -1):
            pt = strxor(ms[i - 1], self.aes.decrypt(ms[i])) + pt
        return pt
 
class CTR(BlockAES):
    def decrypt(self, msg):
        ms = self.split_msg(msg)
        pt = ''
        iv = ms[0]
        for b in ms[1:]:
            pt += strxor(self.aes.encrypt(iv), b)
            iv = iv[:-1] + chr(1 + ord(iv[-1]))
        return pt
 
if __name__ == '__main__':
    print CBC(ckey1).decrypt(ct1)
    print CBC(ckey2).decrypt(ct2)
    print CTR(tk1).decrypt(tct1)
    print CTR(tk2).decrypt(tct2)
