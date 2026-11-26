
# BLM101 Bilgisayar Mühendisliğine Giriş - Dönem Projesi
# Feyza Güreşen - 25360859088
# Proje 4: Makine Döngüsü ve Akümülatör (Accumulator) CPU Simülatörü

# --------------------------------------------------
# 1. Donanım ve Yazmaçlar (Registers)
# --------------------------------------------------
akumulator = 0       # Akümülatör (ACC): Sonuçların tutulduğu ana yazmaç
pc = 0               # Program Sayacı (PC): Sıradaki komutun bellek adresi
ir = ""              # Komut Yazmacı (IR): Bellekten getirilen o anki komut
bellek = []          # Bellek (RAM): Komutların sırayla tutulduğu liste
calisiyor = True     # İşlemcinin çalışıp çalışmadığını tutan değişken

# --------------------------------------------------
# 2. Kullanıcı Girişi ve Belleğe Komut Yükleme
# --------------------------------------------------
print("==================================================")
print("   Mini CPU ve Akümülatör (ACC) Simülatörü")
print("   Öğrenci: Feyza Güreşen | No: 25360859088")
print("==================================================")
print("Desteklenen komutlar: LOAD X, ADD X, SUB X, MUL X, DIV X, HALT\n")
print("1 - Hazır komut dizisini çalıştır (LOAD 10, ADD 5, SUB 3, DIV 2, HALT)")
print("2 - Kendi komutlarını klavyeden gir")

secim = input("\nSeçiminiz (1 veya 2): ").strip()

bellek = []

if secim == "1":
    bellek = ["LOAD 10", "ADD 5", "SUB 3", "DIV 2", "HALT"]
    print("\nHazır komutlar belleğe yüklendi:")
    for k in bellek:
        print(" ->", k)
else:
    print()

    # 1. Başlangıç sayısı
    while True:
        sayi = input("Başlangıç sayısını giriniz: ").strip()
        if sayi.lstrip("-").isdigit():
            bellek.append("LOAD " + sayi)
            break
        print("Lütfen geçerli bir tam sayı giriniz!")

    # 2. İşlem ve sayı
    devam = True
    while devam:
        while True:
            print("\nYapmak istediğiniz işlemi giriniz:")
            islem = input(
                "(1 = Toplama, 2 = Çıkarma, 3 = Çarpma, 4 = Bölme): "
            ).strip()

            if islem in ("1", "2", "3", "4"):
                break
            print("Lütfen 1, 2, 3 veya 4 giriniz!")

        komut_adi = {
            "1": "ADD",
            "2": "SUB",
            "3": "MUL",
            "4": "DIV"
        }[islem]

        while True:
            sayi = input("İşlemde kullanılacak sayıyı giriniz: ").strip()
            if sayi.lstrip("-").isdigit():
                bellek.append(komut_adi + " " + sayi)
                break
            print("Lütfen geçerli bir tam sayı giriniz!")

        cevap = input(
            "\nBaşka işlem eklemek ister misiniz? (e/h): "
        ).strip().lower()

        if cevap != "e":
            devam = False

    print("\nBelleğe yüklenen komutlar:")
    for k in bellek:
        print(" ->", k)

# Listenin sonunda HALT yoksa ekle
if len(bellek) == 0:
    bellek = ["HALT"]
elif bellek[-1].upper() != "HALT":
    bellek.append("HALT")

    
print("\n==================================================")
print("         MAKİNE DÖNGÜSÜ BAŞLATILIYOR")
print("==================================================")

# --------------------------------------------------
# 3. Makine Döngüsü (Fetch - Decode - Execute)
# --------------------------------------------------
adim = 1

while calisiyor:
    print(f"\n--- ADIM {adim} ---")

    # 1. FETCH (Alma) Aşaması:
    # PC'deki adresten komutu alıp IR'ye aktarıyoruz, ardından PC'yi 1 artırıyoruz.
    if pc < len(bellek):
        ir = bellek[pc]
        print(f"1. Fetch  : Bellek[{pc}] okundu -> IR = '{ir}'")
        pc = pc + 1
        print(f"            Program Sayacı güncellendi -> PC = {pc}")
    else:
        # Bellek bittiyse durdur
        print("Fetch hatası: Bellek sonuna ulaşıldı.")
        calisiyor = False
        break

    # 2. DECODE (Çözümleme) Aşaması:
    # Komut yazmacındaki metni ayırıp işlem kodunu (Opcode) ve sayıyı (Operand) buluyoruz.
    parcalar = ir.split()
    islem = parcalar[0].upper()
    sayi = 0

    if len(parcalar) > 1:
        sayi = int(parcalar[1])
        print(f"2. Decode : İşlem Kodu (Opcode) = {islem}, Sayı (Operand) = {sayi}")
    else:
        print(f"2. Decode : İşlem Kodu (Opcode) = {islem}")

    # 3. EXECUTE (Yürütme) Aşaması:
    # Çözülen komuta göre işlemi Akümülatör üzerinde yapıyoruz.
    if islem == "LOAD":
        # Akümülatöre doğrudan yeni sayıyı yüklüyoruz
        akumulator = sayi
        print(f"3. Execute: LOAD çalıştı. Akümülatöre {sayi} yüklendi.")

    elif islem == "ADD":
        # Akümülatördeki sayıya yeni sayıyı ekliyoruz
        onceki = akumulator
        akumulator = akumulator + sayi
        print(f"3. Execute: ADD çalıştı. {onceki} + {sayi} = {akumulator}")

    elif islem == "SUB":
        # Akümülatördeki sayıdan sayıyı çıkarıyoruz
        onceki = akumulator
        akumulator = akumulator - sayi
        print(f"3. Execute: SUB çalıştı. {onceki} - {sayi} = {akumulator}")

    elif islem == "MUL":
        # Akümülatördeki sayıyı yeni sayıyla çarpıyoruz
        onceki = akumulator
        akumulator = akumulator * sayi
        print(f"3. Execute: MUL çalıştı. {onceki} * {sayi} = {akumulator}")

    elif islem == "DIV":
        # Akümülatördeki sayıyı yeni sayıya bölüyoruz (tamsayı bölmesi)
        if sayi != 0:
            onceki = akumulator
            akumulator = akumulator // sayi
            print(f"3. Execute: DIV çalıştı. {onceki} // {sayi} = {akumulator}")
        else:
            print("3. Execute: HATA! 0'a bölme yapılamaz (Divide by Zero). İşlem atlandı.")

    elif islem == "HALT":
        # İşlemciyi durduruyoruz
        print("3. Execute: HALT komutu geldi, işlemci durduruluyor.")
        calisiyor = False

    else:
        print(f"3. Execute: Hatalı komut! '{islem}' tanınmıyor, atlandı.")

    # Yönergede istenen format: "PC: X | Akümülatör: Y"
    print(f"-> DURUM: PC: {pc} | Akümülatör: {akumulator}")

    adim = adim + 1

# --------------------------------------------------
# 4. Program Sonu Özeti
# --------------------------------------------------
print("\n==================================================")
print("             SİMÜLASYON BİTTİ")
print("==================================================")
print(f"Toplam Döngü Adımı : {adim - 1}")
print(f"Son Program Sayacı : {pc}")
print(f"Son Akümülatör     : {akumulator}")
print("==================================================")
