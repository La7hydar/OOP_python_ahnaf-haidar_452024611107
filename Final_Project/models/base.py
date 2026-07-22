from abc import ABC, abstractmethod


class EntitasSewa(ABC):
    """Abstract Base Class yang bertindak sebagai cetak biru (Abstraction)."""

    @abstractmethod
    def hitung_total_biaya(self, durasi: int) -> float:
        """Method abstrak yang wajib diimplementasikan oleh setiap sub-class."""
        pass


class Lapangan(EntitasSewa):
    """Class Induk untuk entitas Lapangan (Inheritance dari EntitasSewa)."""

    def __init__(self, kode: str, nama: str, harga_per_jam: float):
        self.kode = kode
        self.nama = nama
        # Encapsulation: Atribut private (ditandai dengan __)
        self.__harga_per_jam = harga_per_jam
        self.is_tersedia = True
        self.durasi_sewa_terakhir = 0

    # Getter untuk mengakses atribut private __harga_per_jam
    @property
    def harga_per_jam(self) -> float:
        return self.__harga_per_jam

    # Setter untuk mengubah harga dengan logika validasi
    @harga_per_jam.setter
    def harga_per_jam(self, nilai_baru: float):
        if nilai_baru <= 0:
            raise ValueError("Harga per jam harus lebih dari 0!")
        self.__harga_per_jam = nilai_baru

    # Magic Method: __len__ untuk mengembalikan durasi sewa
    def __len__(self) -> int:
        return self.durasi_sewa_terakhir

    # Magic Method: __str__ untuk representasi string dari objek
    def __str__(self) -> str:
        status = "Tersedia" if self.is_tersedia else "Terisi"
        return f"[{self.kode}] {self.nama} - Rp{self.__harga_per_jam:,.0f}/jam ({status})"