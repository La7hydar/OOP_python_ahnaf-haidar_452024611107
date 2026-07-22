class Kendaraan:
    def __init__(self):
        print("Kendaraan dibuat")

    def info(self):
        print("Ini adalah kendaraan")


class Mobil(Kendaraan):
    def __init__(self):
        super().__init__()
        print("Mobil dibuat")

    def info(self):
        super().info()
        print("Memiliki 4 roda")


class Listrik(Kendaraan):
    def __init__(self):
        super().__init__()
        print("Sistem listrik aktif")

    def info(self):
        super().info()
        print("Menggunakan baterai listrik")


class MobilListrik(Mobil, Listrik):
    def __init__(self):
        super().__init__()
        print("Mobil listrik siap digunakan")

    def info(self):
        super().info()
        print("Gabungan mobil dan teknologi listrik")


objek = MobilListrik()

print("\n=== Informasi Kendaraan ===")
objek.info()