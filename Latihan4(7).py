# Nama : Maya Khansa Arissa
# NIM : 2605822
# Kelas : 1A

username = "dasproRPL"
password = "RPLfire!123"
MAKS_PERCOBAAN = 3

percobaan = 0

while percobaan < MAKS_PERCOBAAN:
    input_username = input("Masukkan username: ").strip()
    input_password = input("Masukkan password: ")

    if input_username == username and input_password == password:
        print("Login berhasil!")
        break
    else:
        percobaan += 1
        sisa = MAKS_PERCOBAAN - percobaan
        if sisa > 0:
            print(f"Username atau password salah. Sisa kesempatan: {sisa}")
        else:
            print("Username atau password salah. Akun terkunci, silakan coba lagi nanti.")