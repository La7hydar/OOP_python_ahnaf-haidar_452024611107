# 1. Custom Exception Class
class SaldoMinimalError(Exception):
    def __init__(self, pesan="Maaf, penarikan gagal. Saldo tidak mencukupi!"):
        self.pesan = pesan
        super().__init__(self.pesan)

# 2. Class Utama dengan Logika Validasi
class RekeningBank:
    def __init__(self, nama_pemilik, saldo_awal):
        self.nama_pemilik = nama_pemilik
        self.saldo = saldo_awal

    def tarik_tunai(self, jumlah_tarik):
        print(f"--- Mencoba menarik uang: Rp{jumlah_tarik} ---")
        
        # Memicu custom exception menggunakan 'raise'
        if jumlah_tarik > self.saldo:
            raise SaldoMinimalError(f"Gagal! Menarik Rp{jumlah_tarik}, saldo hanya Rp{self.saldo}.")
        
        self.saldo -= jumlah_tarik
        print(f"Berhasil! Sisa saldo: Rp{self.saldo}")

# 3. Implementasi Try-Except-Finally
if __name__ == "__main__":
    akun_saya = RekeningBank(nama_pemilik="Nama Kamu", saldo_awal=500000)

    try:
        # Penarikan pertama (Berhasil)
        akun_saya.tarik_tunai(200000)
        
        # Penarikan kedua (Gagal, memicu error karena saldo sisa Rp300.000)
        akun_saya.tarik_tunai(400000)
        
    except SaldoMinimalError as error:
        print(f"[Peringatan] {error}")
        
    finally:
        print("Sistem Bank: Proses pemeriksaan transaksi telah selesai dilakukan.")