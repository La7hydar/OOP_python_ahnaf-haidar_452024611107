import os 
class AbsensiDigital:
    def __init__(self, nama, id_karyawan, pin):
        self.__nama = nama
        self.__id_karyawan = id_karyawan
        self.__pin = pin
        self.__status_kehadiran = "Belum Absen"

    def get_nama(self):
        return self.__nama

    def lakukan_absensi(self, pin_input):
        os.system('cls')
        print(f"\n--- Mencoba Absensi untuk {self.__nama} ---")
        if pin_input == self.__pin:
            self.__status_kehadiran = "Hadir"
            print("Verifikasi Berhasil! Kehadiran Anda telah dicatat.")
        else:
            print("Verifikasi Gagal! PIN salah. Data tidak dapat diubah.")

    def cek_status(self, pin_input):
        if pin_input == self.__pin:
            print(f"ID Karyawan: {self.__id_karyawan}")
            print(f"Status Saat Ini: {self.__status_kehadiran}")
        else:
            print("Akses Ditolak! PIN salah.")

# --- Instansiasi ---
karyawan1 = AbsensiDigital("Aris", "EMP-2024-001", "1234")

# --- Pengujian dengan Input ---
print(f"Halo {karyawan1.get_nama()}, silakan masukkan PIN untuk Absen.")

# Minta input dari user di terminal
input_user = input("Masukkan PIN Anda: ")

# Jalankan validasi berdasarkan apa yang kamu ketik
karyawan1.lakukan_absensi(input_user)
karyawan1.cek_status(input_user)