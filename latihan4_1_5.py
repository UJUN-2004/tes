print(f"<{' TOKO SEGAR MANIS ':=^40}>")
print("Jenis buah yang tersedia")
print("1. Kiwi")
print("2. Mangga")
print("3. Alpukat")
print("4. Apel")

buah = input("\nPilih Buah : ")
kg_pembelian = int(input("\nKilo pembelian : "))

hadiah = "tidak ada"

match buah :
    case "1" | "kiwi"  :
        if kg_pembelian >= 5 and kg_pembelian < 20 : 
            diskon = 0.05
        elif kg_pembelian >= 20:
            diskon = 0.07
    case "2" | "mangga" : 
        if kg_pembelian >= 5 and kg_pembelian < 20 : 
            diskon = 0.025
        elif kg_pembelian >= 20:
            diskon = 0.07
    case "3" | "alpukat" :
        if kg_pembelian >= 5: 
            diskon = 0.07
        if kg_pembelian >= 10 and  kg_pembelian < 10:
            hadiah = "patung"
        elif kg_pembelian >= 15:
            hadiah = "tas"
    case "4" | "alpukat" :
        if kg_pembelian >= 5 : 
            diskon = 0.1
    case _ :
        print("Tidak ada opsi yang sesuai")
        diskon = 0

print(f"\nTotal diskon : {diskon:.2%}")
print(f"Dapat hadiah : {hadiah}")
        