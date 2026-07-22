
class Laptop:
    def __init__(self, merk, prosesor, ram):
        self.merk = merk          
        self.prosesor = prosesor  
        self.ram = ram            

    
laptop_kantor = Laptop("Lenovo", "Intel i5", "8GB")
laptop_gaming = Laptop("ASUS ROG", "AMD Ryzen 9", "32GB")

print(f"Laptop 1: Merk {laptop_kantor.merk}, Prosesor {laptop_kantor.prosesor}, RAM {laptop_kantor.ram}")
print(f"Laptop 2: Merk {laptop_gaming.merk}, Prosesor {laptop_gaming.prosesor}, RAM {laptop_gaming.ram}")