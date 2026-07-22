class Produk:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

    def __str__(self):
        return f"Produk: {self.nama:10} | Harga: Rp{self.harga:>8}"

    def __eq__(self, other):
        return self.harga == other.harga

    def __lt__(self, other):
        return self.harga < other.harga

    def __gt__(self, other):
        return self.harga > other.harga

# 1. Instansiasi minimal 3 Object dengan data berbeda
p1 = Produk("Keyboard", 500000)
p2 = Produk("Mouse", 300000)
p3 = Produk("Monitor", 500000) # Sama dengan p1 untuk tes __eq__

# 2. Menampilkan fungsi __str__
print("=== DAFTAR PRODUK ===")
print(p1)
print(p2)
print(p3)

# 3. Pengujian Perbandingan (Minimal 3 Metode)
print("\n=== HASIL PENGUJIAN PERBANDINGAN ===")

# Tes Metode __lt__ (<)
print(f"Apakah {p2.nama} < {p1.nama}? {p2 < p1}")

# Tes Metode __gt__ (>)
print(f"Apakah {p1.nama} > {p2.nama}? {p1 > p2}")

# Tes Metode __eq__ (==)
print(f"Apakah {p1.nama} == {p3.nama}? {p1 == p3}")