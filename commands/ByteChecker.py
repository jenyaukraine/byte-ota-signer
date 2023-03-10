import os
import struct
from exceptions.SignatureException import SignatureException 

class ByteChecker:
    def __init__(self, filename):
        self.filename = filename

    def run(self):
        try:
            self.verify_package()
        except SignatureException as e:
            print(f"Signature verification failed: {e}")

    def verify_package(self):
        package_file = os.path.join(self.filename)
        file_len = os.path.getsize(package_file)
        with open(package_file, "rb") as f:
            f.seek(file_len - 6)
            footer = f.read(6)
            print(f"Verified bytes: {footer}")
            if footer[2] != 255 or footer[3] != 255:
                raise SignatureException("no signature in file (no footer)")
            comment_size = (footer[4] & 255) | ((footer[5] & 255) << 8)
            signature_start = (footer[0] & 255) | ((footer[1] & 255) << 8)
            eocd = bytearray(comment_size + 22)
            f.seek(file_len - (comment_size + 22))
            f.readinto(eocd)
            print(f"Verified bytes: {eocd[:4]}")
            if eocd[0] != 80 or eocd[1] != 75 or eocd[2] != 5 or eocd[3] != 6:
                raise SignatureException("no signature in file (bad footer)")
            for i in range(4, len(eocd) - 3):
                if eocd[i] == 80 and eocd[i + 1] == 75 and eocd[i + 2] == 5 and eocd[i + 3] == 6:
                    raise SignatureException("EOCD marker found after start of EOCD")
