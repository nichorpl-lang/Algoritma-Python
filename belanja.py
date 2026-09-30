# list Kosong
belanja = []

# 5 Nama Barang (Loop)
for i in range(5):
    belanja.append(input(f"Barang ke-{i+1}: "))

print("\nDaftar Belanja:")
for i, item in enumerate(belanja, 1):
    print(f"{i}. {item}")

# d) Total item dan item ke-3
print("Total item:", len(belanja))
print("Item ke-3:", belanja[2])