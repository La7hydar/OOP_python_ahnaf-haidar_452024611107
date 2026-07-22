class AlatPembayaran:
    """Kelas induk untuk semua metode pembayaran."""

    def proses_bayar(self, jumlah):
        """Metode dasar yang dapat ditimpa oleh kelas anak."""
        raise NotImplementedError("Subkelas harus mengimplementasikan metode proses_bayar()")


class KartuKredit(AlatPembayaran):
    def __init__(self, nomor, pemegang):
        self.nomor = nomor
        self.pemegang = pemegang

    def proses_bayar(self, jumlah):
        print(f"[KartuKredit] Memproses pembayaran sebesar Rp{jumlah:,} dengan kartu kredit {self.nomor} milik {self.pemegang}.")
        print("[KartuKredit] Transaksi diverifikasi melalui jaringan kartu kredit.")


class EWallet(AlatPembayaran):
    def __init__(self, nama_wallet, saldo):
        self.nama_wallet = nama_wallet
        self.saldo = saldo

    def proses_bayar(self, jumlah):
        if jumlah > self.saldo:
            print(f"[EWallet] Saldo tidak cukup di {self.nama_wallet}. Sisa saldo: Rp{self.saldo:,}.")
        else:
            self.saldo -= jumlah
            print(f"[EWallet] Memproses pembayaran sebesar Rp{jumlah:,} via {self.nama_wallet}.")
            print(f"[EWallet] Sisa saldo sekarang: Rp{self.saldo:,}.")


class QRCodePembayaran:
    """Bukan turunan AlatPembayaran, tetapi memiliki proses_bayar() juga."""

    def __init__(self, kode_qr):
        self.kode_qr = kode_qr

    def proses_bayar(self, jumlah):
        print(f"[QRCodePembayaran] Memindai QR Code {self.kode_qr} untuk membayar Rp{jumlah:,}.")
        print("[QRCodePembayaran] Pembayaran berhasil dikonfirmasi lewat sistem QR.")


def jalankan_transaksi(objek, jumlah):
    """Fungsi duck typing yang memanggil proses_bayar() tanpa memeriksa tipe objek."""
    print("\n=== Menjalankan transaksi ===")
    objek.proses_bayar(jumlah)


if __name__ == "__main__":
    kartu = KartuKredit(nomor="1234-5678-9012-3456", pemegang="Alden")
    ewallet = EWallet(nama_wallet="GoPay", saldo=500_000)
    qr = QRCodePembayaran(kode_qr="QR-2026-05-29")

    jalankan_transaksi(kartu, 250_000)
    jalankan_transaksi(ewallet, 150_000)
    jalankan_transaksi(qr, 100_000)
