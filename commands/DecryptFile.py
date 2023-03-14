import os
from Cryptodome.Cipher import AES


AES_KEY = b')1Zorxo^fAhGlh$#'
AES_IV = b'aoAkfwk+#1.6G{dE'

class DecryptFile:
    def __init__(self, filename):
        self.filename = filename

    def run(self):
        res = self.decrypt_file(self.filename, str.replace(self.filename, 'encrypt', 'decrypt'))
        print(res)

    def decrypt_file(self, in_file, out_file):
        enc_file_size = os.path.getsize(in_file)
        inf = open(in_file, 'rb')
        dec_file_size = inf.read(4)
        dec_file_size = int.from_bytes(dec_file_size, byteorder='little')
        # Skip 8 bytes
        _ = inf.read(8)
        pad_size = 0
        if dec_file_size % 16 != 0:
            pad_size = 16 - dec_file_size % 16
        if enc_file_size != dec_file_size + pad_size + 12:
            raise Exception('File size mismatch')
        outf = open(out_file, 'wb')
        num_chunks = (enc_file_size - 12) // 0x1000
        for i in range(num_chunks):
            cipher = AES.new(AES_KEY, AES.MODE_CBC, AES_IV)
            data = inf.read(0x1000)
            outf.write(cipher.decrypt(data))
        remainder = (enc_file_size - 12) % 0x1000
        if remainder > 0:
            cipher = AES.new(AES_KEY, AES.MODE_CBC, AES_IV)
            data = self.read_exactly(inf, remainder)
            outf.write(cipher.decrypt(data))
        inf.close()
        # truncate to strip the padding bytes if any
        outf.truncate(dec_file_size)
        outf.close()

    def read_exactly(self, f, num_bytes):
        ret = b''
        while len(ret) < num_bytes:
            data = f.read(num_bytes - len(ret))
            if not data:
                raise Exception('Unexpected end of file')
            ret += data
        return ret

