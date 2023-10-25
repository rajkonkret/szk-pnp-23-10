import chardet
# pip install chardet - instalacja modułu chardet

file_path = 'test.log'

with open(file_path, 'rb') as file:
    raw_data = file.read()

result = chardet.detect(raw_data)
print(result)
# przy odpowiednio duzej próbce dostajemy włąsciwe kodowanie:
# {'encoding': 'utf-8', 'confidence': 0.99, 'language': ''}
encoding = result['encoding']
print(encoding)

print(raw_data.decode(encoding=encoding))