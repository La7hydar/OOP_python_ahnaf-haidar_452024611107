class Laptop:
    def __init__(self, merk, prosesor, ram):
        self.merk = merk
        self.prosesor = prosesor
        self.ram = ram

    def cek_spesifikasi(self):
        print(f"Laptop {self.merk} | Prosesor: {self.prosesor} | RAM: {self.ram}GB")

    def status_baterai(self, persen):
        print(f"Status Baterai {self.merk}: {persen}%")

    @staticmethod
    def konversi_ram_ke_mb(jumlah_gb):
        return jumlah_gb * 1024

laptop1 = Laptop("Lenovo", "Intel i5", 8)
laptop2 = Laptop("ASUS ROG", "AMD Ryzen 9", 32)

print("--- Output Instance Methods ---")
laptop1.cek_spesifikasi()
laptop1.status_baterai(85)
laptop2.cek_spesifikasi()
laptop2.status_baterai(15)

print("\n--- Output Static Method ---")
hasil1 = Laptop.konversi_ram_ke_mb(8)
hasil2 = laptop2.konversi_ram_ke_mb(32)
print(f"RAM 8GB = {hasil1} MB")
print(f"RAM 32GB = {hasil2} MB")