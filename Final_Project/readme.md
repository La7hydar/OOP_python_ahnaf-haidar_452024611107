# 🏢 Final Project: Sistem Reservasi Lapangan SportSpace

Aplikasi CLI (*Command Line Interface*) untuk manajemen reservasi dan penyewaan lapangan olahraga (Futsal & Badminton) berbasis Object-Oriented Programming (OOP) dengan Python.

---

## 🛠️ Implementasi Persyaratan Teknis (Pilar OOP)

1. **Inheritance (Pewarisan):**
   * Class `LapanganFutsal` dan `LapanganBadminton` menginduk pada class `Lapangan` (`models/lapangan_spesifik.py`).
   * Hierarchy Custom Exception menginduk pada class `SportSpaceError` (`exceptions.py`).

2. **Encapsulation (Enkapsulasi):**
   * Atribut harga dibuat Private (`__harga_per_jam`) pada `models/base.py`.
   * Akses dan modifikasi harga dilindungi menggunakan `@property` (getter) dan `@harga_per_jam.setter` dengan validasi nilai $\ge 0$.

3. **Polymorphism (Banyak Bentuk):**
   * Method Overriding pada `hitung_total_biaya()` di mana Lapangan Futsal menghitung *surcharge peak hour*, sedangkan Lapangan Badminton menghitung *sewa raket*.

4. **Special / Magic Methods:**
   * Menggunakan `__init__`, `__str__` untuk format tampilan string object, dan `__len__` pada `models/base.py`.

5. **Advanced Methods:**
   * **Instance Methods:** Digunakan pada `ManajerSewa` (`main.py`) untuk mengelola alur reservasi dan verifikasi admin.
   * **Static Methods:** Digunakan pada `TransaksiHelper` (`utils/helper.py`) untuk hitung PPN 11%, format Rupiah, dan render tabel CLI.

6. **Robustness & Exception Handling:**
   * Custom Exception di `exceptions.py` (`DurasiInvalidError`, `LapanganPenuhError`, `InputPembayaranError`).
   * Handling bertingkat (`try-except`) di `main.py` agar aplikasi anti-*crash*.

---

## 🚀 Cara Menjalankan Aplikasi

1. Pastikan Python 3.x sudah terpasang.
2. Buka Terminal / PowerShell dan arahkan ke folder `Final_Project`.
3. Jalankan perintah:
   ```bash
   python main.py
