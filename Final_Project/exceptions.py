class SportSpaceError(Exception):
    """Base class exception untuk aplikasi SportSpace."""
    pass


class DurasiInvalidError(SportSpaceError):
    """Dilemparkan ketika durasi sewa yang dimasukkan <= 0."""
    def __init__(self, pesan="Durasi sewa harus lebih besar dari 0 jam!"):
        self.pesan = pesan
        super().__init__(self.pesan)


class LapanganPenuhError(SportSpaceError):
    """Dilemparkan ketika lapangan yang dipilih tidak tersedia."""
    def __init__(self, pesan="Maaf, lapangan ini sudah direservasi pada jadwal tersebut!"):
        self.pesan = pesan
        super().__init__(self.pesan)


class InputPembayaranError(SportSpaceError):
    """Dilemparkan ketika jumlah pembayaran kurang dari total tagihan."""
    def __init__(self, pesan="Jumlah pembayaran tidak mencukupi!"):
        self.pesan = pesan
        super().__init__(self.pesan)