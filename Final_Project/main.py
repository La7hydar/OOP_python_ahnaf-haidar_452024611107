import sys
from models.lapangan_spesifik import LapanganFutsal, LapanganBadminton
from utils.helper import TransaksiHelper
from exceptions import (
    SportSpaceError, 
    DurasiInvalidError, 
    LapanganPenuhError, 
    InputPembayaranError
)


class ManajerSewa:
    """Class pengelola sistem reservasi (Instance Methods & Orchestrator)."""

    def __init__(self):
        self.daftar_lapangan = [
            LapanganFutsal("F01", "Futsal A (Vinyl)", 120000, "Vinyl Premium"),
            LapanganFutsal("F02", "Futsal B (Interlock)", 100000, "Interlock"),
            LapanganBadminton("B01", "Badminton A (Karpet BWF)", 50000, "Vinyl BWF"),
            LapanganBadminton("B02", "Badminton B (Kayu Standard)", 40000, "Kayu Parquet"),
        ]

    def tampilkan_daftar_lapangan(self):
        print("\n--- STATUS DAFTAR LAPANGAN ---")
        TransaksiHelper.cetak_tabel_lapangan(self.daftar_lapangan)

    def proses_reservasi(self):
        """Metode untuk melakukan transaksi penyewaan lapangan baru."""
        TransaksiHelper.bersihkan_layar()
        TransaksiHelper.cetak_header("SISTEM RESERVASI SPORTSPACE", lebar=100)
        self.tampilkan_daftar_lapangan()

        try:
            # 1. Pilih Lapangan
            pilihan = int(input("\nPilih nomor lapangan yang ingin disewa (1-4): "))
            if pilihan < 1 or pilihan > len(self.daftar_lapangan):
                raise IndexError("Nomor lapangan tidak valid dalam daftar!")

            lapangan_terpilih = self.daftar_lapangan[pilihan - 1]

            if not lapangan_terpilih.is_tersedia:
                raise LapanganPenuhError(f"Lapangan {lapangan_terpilih.nama} saat ini sedang TERISI!")

            # 2. Input Durasi
            durasi = int(input("Masukkan durasi sewa (jam): "))
            if durasi <= 0:
                raise DurasiInvalidError("Durasi sewa tidak boleh <= 0 jam!")

            # Logika Spesifik Lapangan
            info_tambahan = ""
            if isinstance(lapangan_terpilih, LapanganFutsal):
                opsi_peak = input("Apakah bermain di Jam Sibuk / Peak Hours? (y/n): ").strip().lower()
                is_peak = opsi_peak == 'y'
                subtotal = lapangan_terpilih.hitung_total_biaya(durasi, is_peak_hour=is_peak)
                info_tambahan = f"Jam Sibuk: {'Ya' if is_peak else 'Tidak'}"

            elif isinstance(lapangan_terpilih, LapanganBadminton):
                opsi_raket = input("Sewa raket tambahan? (y/n): ").strip().lower()
                sewa_raket = opsi_raket == 'y'
                jumlah_raket = 0
                
                if sewa_raket:
                    jumlah_raket = int(input("Masukkan jumlah raket yang disewa: "))
                    if jumlah_raket <= 0:
                        raise ValueError("Jumlah raket harus lebih dari 0!")

                subtotal = lapangan_terpilih.hitung_total_biaya(
                    durasi, sewa_raket=sewa_raket, jumlah_raket=jumlah_raket
                )
                info_tambahan = f"Sewa Raket: {jumlah_raket} buah" if sewa_raket else "Sewa Raket: Tidak"

            pajak = TransaksiHelper.hitung_ppn(subtotal)
            total_bayar = subtotal + pajak

            # 3. LOOP PEMBAYARAN
            pembayaran_berhasil = False
            nominal_bayar = 0.0
            kembalian = 0.0
            nama_metode = ""

            while not pembayaran_berhasil:
                print("\n" + "=" * 50)
                print("RINGKASAN TAGIHAN".center(50))
                print("=" * 50)
                print(f"Lapangan      : {lapangan_terpilih.nama}")
                print(f"Harga / Jam   : {TransaksiHelper.format_rupiah(lapangan_terpilih.harga_per_jam)}")
                print(f"Durasi        : {durasi} Jam")
                print(f"Opsi Tambahan : {info_tambahan}")
                print(f"Subtotal      : {TransaksiHelper.format_rupiah(subtotal)}")
                print(f"PPN (11%)     : {TransaksiHelper.format_rupiah(pajak)}")
                print(f"TOTAL TAGIHAN : {TransaksiHelper.format_rupiah(total_bayar)}")
                print("=" * 50)

                print("\n--- METODE PEMBAYARAN ---")
                print("1. Cash (Tunai)")
                print("2. Card (Debit/Kredit)")
                print("3. QRIS")
                print("4. Batal Transaksi")
                metode_opt = input("Pilih metode pembayaran (1-4): ").strip()

                try:
                    if metode_opt == "1":
                        nama_metode = "CASH (TUNAI)"
                        nominal_bayar = float(input("\nMasukkan nominal uang pembayaran: Rp"))
                        if nominal_bayar < total_bayar:
                            raise InputPembayaranError(
                                f"Uang Anda kurang {TransaksiHelper.format_rupiah(total_bayar - nominal_bayar)}!"
                            )
                        kembalian = nominal_bayar - total_bayar
                        pembayaran_berhasil = True

                    elif metode_opt in ["2", "3"]:
                        nama_metode = "CARD (DEBIT/KREDIT)" if metode_opt == "2" else "QRIS"
                        print(f"\n[INFO] Silahkan lakukan pembayaran via {nama_metode} sebesar {TransaksiHelper.format_rupiah(total_bayar)}")
                        verifikasi = input("Konfirmasi Admin: Apakah pembayaran sukses? (y/n): ").strip().lower()
                        
                        if verifikasi != 'y':
                            raise InputPembayaranError(f"Pembayaran via {nama_metode} Gagal / Dibatalkan!")
                        
                        nominal_bayar = total_bayar
                        kembalian = 0.0
                        pembayaran_berhasil = True

                    elif metode_opt == "4":
                        print("\n[INFO] Transaksi dibatalkan.")
                        input("\nTekan Enter untuk kembali ke menu utama...")
                        return

                    else:
                        raise ValueError("Pilihan metode pembayaran tidak valid!")

                except (InputPembayaranError, ValueError) as err:
                    print(f"\n[ERROR PEMBAYARAN] {err}")
                    print("--> Silahkan pilih ulang metode pembayaran atau masukkan nominal yang cukup.\n")

            # Update Status Lapangan Seketika (Real-time)
            lapangan_terpilih.is_tersedia = False
            lapangan_terpilih.durasi_sewa_terakhir = durasi

            # 4. CLEAR SCREEN & CETAK STRUK RESMI
            TransaksiHelper.bersihkan_layar()
            TransaksiHelper.cetak_header("STRUK / RECEIPT RESMI SPORTSPACE", lebar=55)
            print(f" Status Pembayaran : LUNAS / SUCCESS")
            print(f" Metode Pembayaran : {nama_metode}")
            print("-" * 55)
            print(f" Lapangan          : {lapangan_terpilih.nama}")
            print(f" Tarif / Jam       : {TransaksiHelper.format_rupiah(lapangan_terpilih.harga_per_jam)}")
            print(f" Durasi Sewa       : {durasi} Jam")
            print(f" Catatan Tambahan  : {info_tambahan}")
            print("-" * 55)
            print(f" Subtotal          : {TransaksiHelper.format_rupiah(subtotal)}")
            print(f" PPN (11%)         : {TransaksiHelper.format_rupiah(pajak)}")
            print(f" TOTAL TAGIHAN     : {TransaksiHelper.format_rupiah(total_bayar)}")
            print("-" * 55)
            print(f" Uang Diterima     : {TransaksiHelper.format_rupiah(nominal_bayar)}")
            print(f" Kembalian         : {TransaksiHelper.format_rupiah(kembalian)}")
            print("=" * 55)
            print("  Terima kasih telah berolahraga di SportSpace!  ".center(55))
            print("=" * 55 + "\n")
            input("Tekan Enter untuk kembali ke menu utama...")

        except ValueError:
            print("\n[ERROR INPUT] Harap masukkan angka / pilihan yang valid!")
            input("\nTekan Enter untuk kembali...")
        except (IndexError, SportSpaceError) as err:
            print(f"\n[ERROR SISTEM] {err}")
            input("\nTekan Enter untuk kembali...")

    def selesaikan_sewa(self):
        """Fitur Verifikasi Admin untuk mengosongkan kembali lapangan yang selesai dipakai."""
        TransaksiHelper.bersihkan_layar()
        TransaksiHelper.cetak_header("VERIFIKASI ADMIN: SELESAI BERMAIN", lebar=100)
        self.tampilkan_daftar_lapangan()

        # Filter lapangan yang sedang terisi
        lapangan_terisi = [lap for lap in self.daftar_lapangan if not lap.is_tersedia]

        if not lapangan_terisi:
            print("\n[INFO] Saat ini tidak ada lapangan yang sedang terisi/digunakan.")
            input("\nTekan Enter untuk kembali ke menu utama...")
            return

        try:
            pilihan = int(input("\nPilih nomor lapangan yang SUDAH SELESAI digunakan (1-4): "))
            if pilihan < 1 or pilihan > len(self.daftar_lapangan):
                raise IndexError("Nomor lapangan tidak valid!")

            lapangan_terpilih = self.daftar_lapangan[pilihan - 1]

            if lapangan_terpilih.is_tersedia:
                print(f"\n[INFO] Lapangan {lapangan_terpilih.nama} memang sudah dalam keadaan TERSEDIA.")
            else:
                verifikasi = input(f"Verifikasi Admin: Lapangan '{lapangan_terpilih.nama}' selesai bermain? (y/n): ").strip().lower()
                if verifikasi == 'y':
                    # UBAH DATA SECARA LANGSUNG
                    lapangan_terpilih.is_tersedia = True
                    lapangan_terpilih.durasi_sewa_terakhir = 0
                    print(f"\n[SUCCESS] Status lapangan '{lapangan_terpilih.nama}' BERHASIL diubah menjadi TERSEDIA kembali!")
                else:
                    print("\n[INFO] Pembatalan. Status lapangan tidak diubah.")

            input("\nTekan Enter untuk kembali ke menu utama...")

        except ValueError:
            print("\n[ERROR INPUT] Harap masukkan nomor yang valid!")
            input("\nTekan Enter untuk kembali...")
        except IndexError as err:
            print(f"\n[ERROR SISTEM] {err}")
            input("\nTekan Enter untuk kembali...")


def main():
    app = ManajerSewa()
    while True:
        TransaksiHelper.bersihkan_layar()
        TransaksiHelper.cetak_header("SISTEM MANAJEMEN SPORTSPACE", lebar=100)
        app.tampilkan_daftar_lapangan()

        print("\n--- MENU UTAMA ---")
        print("1. Reservasi / Sewa Lapangan")
        print("2. Selesaikan Sewa Lapangan (Verifikasi Admin)")
        print("3. Keluar Aplikasi")

        pilihan_menu = input("\nPilih menu (1-3): ").strip()

        if pilihan_menu == "1":
            app.proses_reservasi()
        elif pilihan_menu == "2":
            app.selesaikan_sewa()
        elif pilihan_menu == "3":
            print("\nTerima kasih telah menggunakan Sistem SportSpace. Sampai jumpa!")
            sys.exit()
        else:
            print("\n[ERROR] Pilihan menu tidak valid!")
            input("\nTekan Enter untuk mengulang...")


if __name__ == "__main__":
    main()