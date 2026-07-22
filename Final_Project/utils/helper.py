import os


class TransaksiHelper:
    """Class utilitas yang berisi Static Methods untuk kalkulasi keuangan dan tampilan CLI."""

    @staticmethod
    def hitung_ppn(subtotal: float, tarif_pajak: float = 0.11) -> float:
        if subtotal < 0:
            return 0.0
        return subtotal * tarif_pajak

    @staticmethod
    def format_rupiah(nominal: float) -> str:
        return f"Rp{nominal:,.0f}".replace(",", ".")

    @staticmethod
    def bersihkan_layar():
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def cetak_header(judul: str, lebar: int = 100):
        """Mencetak banner header yang pas sejajar dengan lebar tabel."""
        print("=" * lebar)
        print(f"{judul.center(lebar)}")
        print("=" * lebar)

    @staticmethod
    def cetak_tabel_lapangan(daftar_lapangan):
        """Mencetak daftar lapangan dalam format tabel rapi bergaris presisi 100 karakter."""
        # Total lebar: 5 + 8 + 30 + 15 + 12 + 25 + (pembatas) = 100 karakter
        garis = "+" + "-"*5 + "+" + "-"*8 + "+" + "-"*30 + "+" + "-"*15 + "+" + "-"*12 + "+" + "-"*25 + "+"
        
        print(garis)
        print(f"| {'No':<3} | {'Kode':<6} | {'Nama Lapangan':<28} | {'Harga/Jam':<13} | {'Status':<10} | {'Spesifikasi':<23} |")
        print(garis)

        for idx, lap in enumerate(daftar_lapangan, start=1):
            status = "Tersedia" if lap.is_tersedia else "Terisi"
            harga_str = TransaksiHelper.format_rupiah(lap.harga_per_jam)
            
            if hasattr(lap, 'jenis_rumput'):
                spek = f"Rumput: {lap.jenis_rumput}"
            elif hasattr(lap, 'jenis_karpet'):
                spek = f"Karpet: {lap.jenis_karpet}"
            else:
                spek = "-"

            print(f"| {idx:<3} | {lap.kode:<6} | {lap.nama:<28} | {harga_str:<13} | {status:<10} | {spek:<23} |")

        print(garis)