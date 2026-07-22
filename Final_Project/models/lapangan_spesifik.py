from models.base import Lapangan


class LapanganFutsal(Lapangan):
    """Sub-class untuk Lapangan Futsal (Inheritance dari Lapangan)."""

    def __init__(self, kode: str, nama: str, harga_per_jam: float, jenis_rumput: str):
        super().__init__(kode, nama, harga_per_jam)
        self.jenis_rumput = jenis_rumput
        self.biaya_kebersihan = 15000.0

    def hitung_total_biaya(self, durasi: int, is_peak_hour: bool = False) -> float:
        total = self.harga_per_jam * durasi
        if is_peak_hour:
            total += total * 0.20
        total += self.biaya_kebersihan
        return total

    def __str__(self) -> str:
        base_str = super().__str__()
        return f"{base_str} | Rumput: {self.jenis_rumput}"


class LapanganBadminton(Lapangan):
    """Sub-class untuk Lapangan Badminton (Inheritance dari Lapangan)."""

    def __init__(self, kode: str, nama: str, harga_per_jam: float, jenis_karpet: str):
        super().__init__(kode, nama, harga_per_jam)
        self.jenis_karpet = jenis_karpet
        self.biaya_sewa_raket_per_jam = 10000.0  # Rp 10.000 / raket / jam

    # Polymorphism: Menambahkan parameter jumlah_raket
    def hitung_total_biaya(self, durasi: int, sewa_raket: bool = False, jumlah_raket: int = 0) -> float:
        total = self.harga_per_jam * durasi
        
        if sewa_raket and jumlah_raket > 0:
            total += (self.biaya_sewa_raket_per_jam * jumlah_raket * durasi)
            
        return total

    def __str__(self) -> str:
        base_str = super().__str__()
        return f"{base_str} | Karpet: {self.jenis_karpet}"