print("Pilih operasi:")
print("1. Tambah")
print("2. Kurang")
print("3. Kali")
print("4. Bagi")

def tambah(num1, num2):
    return num1 + num2
def kurang(num1, num2):
    return num1 - num2
def kali(num1, num2):
    return num1 * num2
def bagi(num1, num2):

    if num2 == 0:
        return "Error: Pembagian dengan nol tidak diperbolehkan."
    return num1 / num2
while True:
    pilihan = input("Masukkan pilihan (1/2/3/4): ")

    if pilihan in ('1', '2', '3', '4'):
        angka1 = float(input("Masukkan angka pertama: "))
        angka2 = float(input("Masukkan angka kedua: "))

        if pilihan == '1':
            print(f"{angka1} + {angka2} = {tambah(angka1, angka2)}")
        elif pilihan == '2':
            print(f"{angka1} - {angka2} = {kurang(angka1, angka2)}")
        elif pilihan == '3':
            print(f"{angka1} * {angka2} = {kali(angka1, angka2)}")
        elif pilihan == '4':
            print(f"{angka1} / {angka2} = {bagi(angka1, angka2)}")

        lagi = input("Apakah Anda ingin melakukan perhitungan lain? (y/n): ")
        if lagi.lower() != 'y':
            break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
