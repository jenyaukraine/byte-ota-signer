import shutil

class ByteWriter:
    def __init__(self, filename1, filename2):
        self.filename1 = filename1
        self.filename2 = filename2

    def run(self):
        with open(self.filename1, 'rb') as f1:
            buffer = bytearray(4096)
            f1.seek(0)
            f1.readinto(buffer)

            with open(self.filename2, 'r+b') as f2:
                f2.seek(0)
                f2.write(buffer)
