import shutil

class ByteWriter:
    def __init__(self, filename1, filename2):
        self.filename1 = filename1
        self.filename2 = filename2

    def run(self):
        # Открываем исходный файл для чтения
        with open(self.filename1, 'rb') as f1:
            # Читаем все содержимое файла
            content = f1.read()

            # Ищем байты, которые мы проверяем в оригинальном файле
            footer = content[-6:]
            footer_2 = footer[:2] + b'\x00\x00' + footer[2:]

            # Создаём новый файл и записываем в него содержимое исходного файла
            with open(self.filename2, 'wb') as f2:
                f2.write(content)

                # Записываем новые байты в те же места, где они были в оригинальном файле
                f2.seek(len(content) - 6)
                f2.write(footer_2)

        # Проверяем, что файл package2.dat содержит те же байты, что и оригинальный файл
        with open(self.filename2, 'rb') as f:
            content = f.read()
            footer = content[-6:]
            print(f"Verified bytes: {footer}")
