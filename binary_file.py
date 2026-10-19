data = b"om namo shivaay"
with open("binary_file.bin","wb") as file:
    file.write(data)

with open("binary_file.bin","rb") as file:
    content = file.read()
    print(content)