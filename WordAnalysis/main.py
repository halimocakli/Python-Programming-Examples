kelime = input("Analiz edilecek kelimeyi giriniz: ")
uzunluk = len(kelime)

harfler = ""

for harf in kelime:
    if harf not in harfler:
        harfler += harf

siklik = ""

for h in harfler:
    sayac = 0
    for k in kelime:
        if k == h:
            sayac += 1

    siklik += f"\n\t\t {h} harfi {sayac} kere geçiyor"

print("\n**********************************************************\n")
print(f"{kelime} kelimesi {uzunluk} harften oluşuyor")
print("Kelimede", end=" ")
print(*harfler, sep="-", end=" ")
print("harfleri bulunuyor.")
print("\n Kelimede, ")
print(siklik)
print("\n**********************************************************\n")