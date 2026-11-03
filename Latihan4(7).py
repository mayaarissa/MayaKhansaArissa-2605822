# Nama : Maya Khansa Arissa
# NIM : 2605822
# Kelas : 1A

username = "dasproRPL"
password = "RPLfire!123"

while True:
    input_username = input("Masukkan username: ")
    input_password = input("Masukkan password: ")

    if input_username == username and input_password == password:
        print("Login berhasil!")
        break
    else:
        print("Username atau password salah. Silakan coba lagi.")