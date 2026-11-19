# ==============================================================================
# BLM101 Bilgisayar Mühendisliğine Giriş - Dönem Projesi
# Proje 4: Makine Döngüsü ve Akümülatör (Accumulator) CPU Simülatörü
# 
# Öğrenci Adı Soyadı : Feyza Güreşen
# Öğrenci Numarası   : 25360859088
# 
# AÇIKLAMA:
# Bu program, temel bir merkezi işlem biriminin (CPU) makine döngüsünü 
# (Fetch -> Decode -> Execute) simüle eden tek yazmaçlı (Akümülatör tabanlı)
# bir işlemci modelidir. Kod, sınavda kolay anlaşılması ve savunulabilmesi için
# yalnızca temel if-else şart blokları ve while döngüsü ile yazılmıştır.
# ==============================================================================

# ------------------------------------------------------------------------------
# BÖLÜM 1: CPU DONANIM VE YAZMAÇ (REGISTER) TANIMLAMALARI
# ------------------------------------------------------------------------------

# Akümülatör (ACC): Aritmetik ve mantıksal işlemlerin sonucunun tutulduğu ana yazmaç.
akumulator = 0

# Program Sayacı (PC - Program Counter): Sıradaki çalıştırılacak komutun bellek adresini tutar.
program_sayaci = 0

# Komut Yazmacı (IR - Instruction Register): Bellekten o an getirilen (Fetch edilen) komutu tutar.
komut_yazmaci = ""

# Bellek (RAM / Hafıza): Program komutlarının sırasıyla saklandığı liste.
bellek = []

# İşlemcinin çalışma durumunu kontrol eden bayrak (flag)
calisiyor = True

# ------------------------------------------------------------------------------
# BÖLÜM 2: KULLANICI KARŞILAMA VE KOMUTLARIN BELLEĞE YÜKLENMESİ
# ------------------------------------------------------------------------------

print("=" * 65)
print("     MINI CPU AKÜMÜLATÖR (ACCUMULATOR) SİMÜLATÖRÜ")
print("     Öğrenci: Feyza Güreşen | No: 25360859088")
print("=" * 65)
print("Desteklenen Temel Komutlar:")
print("  - LOAD X : Akümülatöre X sayısını yükler (Örn: LOAD 10)")
print("  - ADD X  : Akümülatöre X sayısını ekler  (Örn: ADD 5)")
print("  - SUB X  : Akümülatörden X sayısını çıkarır (Örn: SUB 3)")
print("  - MUL X  : Akümülatördeki sayıyı X ile çarpar (Örn: MUL 2)")
print("  - HALT   : Programı durdurur / sonlandırır")
print("-" * 65)
print("Program modu seçiniz:")
print("1 - Yönergedeki hazır örnek programı çalıştır (LOAD 10, ADD 5, SUB 3, HALT)")
print("2 - Kendi komutlarınızı klavyeden girin")
print("-" * 65)

secim = input("Seçiminiz (1 veya 2): ")

if secim == "1":
    # Yönergede örnek olarak verilen komut dizisi
    bellek = ["LOAD 10", "ADD 5", "SUB 3", "HALT"]
    print("\n[BİLGİ] Hazır komutlar belleğe yüklendi:")
    for satir in bellek:
        print("  ->", satir)
else:
    print("\nLütfen komutları sırayla giriniz. Bitirmek için HALT komutunu yazınız:")
    komut_sirasi = 1
    giris_devam = True
    while giris_devam:
        girilen = input(str(komut_sirasi) + ". Komut: ")
        # Boş giriş yapılmadıysa belleğe ekle
        if girilen.strip() != "":
            bellek.append(girilen.strip())
            # Kullanıcı HALT yazdıysa veya boş bıraktıysa giriş döngüsünden çık
            if girilen.strip().upper() == "HALT":
                giris_devam = False
            komut_sirasi = komut_sirasi + 1
        else:
            print("Boş komut girilemez!")

# Eğer kullanıcının girdiği listenin sonunda HALT yoksa güvenli durma için otomatik ekleyelim
if len(bellek) == 0:
    print("[UYARI] Belleğe komut girilmediği için varsayılan HALT yüklendi.")
    bellek = ["HALT"]
elif bellek[-1].upper() != "HALT":
    bellek.append("HALT")

print("\n" + "=" * 65)
print("           CPU ÇALIŞTIRMA VE MAKİNE DÖNGÜSÜ BAŞLIYOR")
print("=" * 65)

# ------------------------------------------------------------------------------
# BÖLÜM 3: MAKİNE DÖNGÜSÜ (FETCH - DECODE - EXECUTE)
# ------------------------------------------------------------------------------

adim = 1

while calisiyor:
    print("\n" + "-" * 65)
    print(f"ADIM {adim}:")
    print("-" * 65)

    # --------------------------------------------------------------------------
    # 1. AŞAMA: FETCH (KOMUTU GETİR)
    # --------------------------------------------------------------------------
    # Program Sayacının (PC) gösterdiği bellek adresindeki komut okunur ve
    # Komut Yazmacına (IR) aktarılır. Ardından PC bir sonraki adresi gösterir.
    if program_sayaci < len(bellek):
        komut_yazmaci = bellek[program_sayaci]
        print(f"1. FETCH (Getir)   : Bellek adresi [{program_sayaci}] okundu -> IR = '{komut_yazmaci}'")
        program_sayaci = program_sayaci + 1
        print(f"                     Program Sayacı (PC) güncellendi -> PC = {program_sayaci}")
    else:
        # Bellek sınırına ulaşıldıysa dur
        print("1. FETCH (Getir)   : Bellek sonuna ulaşıldı.")
        calisiyor = False
        break

    # --------------------------------------------------------------------------
    # 2. AŞAMA: DECODE (KOMUTU ÇÖZ)
    # --------------------------------------------------------------------------
    # Komut yazmacındaki metin parçalanarak işlem türü (Opcode) ve sayısal değer
    # (Operand) belirlenir.
    parcalar = komut_yazmaci.split()
    islem = parcalar[0].upper()
    sayi = 0

    if len(parcalar) > 1:
        sayi = int(parcalar[1])
        print(f"2. DECODE (Çöz)    : İşlem Kodu (Opcode) = '{islem}', Parametre (Operand) = {sayi}")
    else:
        print(f"2. DECODE (Çöz)    : İşlem Kodu (Opcode) = '{islem}' (Parametresiz komut)")

    # --------------------------------------------------------------------------
    # 3. AŞAMA: EXECUTE (KOMUTU YÜRÜT / ÇALIŞTIR)
    # --------------------------------------------------------------------------
    # Belirlenen işleme göre aritmetik-mantık işlemi doğrudan Akümülatör üzerinde yapılır.
    if islem == "LOAD":
        # Akümülatöre doğrudan yeni değer atanır
        akumulator = sayi
        print(f"3. EXECUTE (Yürüt) : LOAD işlemi yapıldı. Akümülatöre {sayi} değeri yüklendi.")

    elif islem == "ADD":
        # Akümülatördeki mevcut değere sayı eklenir
        onceki_deger = akumulator
        akumulator = akumulator + sayi
        print(f"3. EXECUTE (Yürüt) : ADD işlemi yapıldı. {onceki_deger} + {sayi} = {akumulator}")

    elif islem == "SUB":
        # Akümülatördeki mevcut değerden sayı çıkarılır
        onceki_deger = akumulator
        akumulator = akumulator - sayi
        print(f"3. EXECUTE (Yürüt) : SUB işlemi yapıldı. {onceki_deger} - {sayi} = {akumulator}")

    elif islem == "MUL":
        # Akümülatördeki mevcut değer sayı ile çarpılır
        onceki_deger = akumulator
        akumulator = akumulator * sayi
        print(f"3. EXECUTE (Yürüt) : MUL işlemi yapıldı. {onceki_deger} * {sayi} = {akumulator}")

    elif islem == "HALT":
        # Program durdurulur
        print("3. EXECUTE (Yürüt) : HALT komutu algılandı. İşlemci durduruluyor...")
        calisiyor = False

    else:
        # Tanımlanmayan geçersiz komut durumu
        print(f"3. EXECUTE (HATA)  : Geçersiz komut algılandı: '{islem}'. İşlem yapılmadı.")

    # --------------------------------------------------------------------------
    # 4. AŞAMA: DURUM RAPORU
    # --------------------------------------------------------------------------
    # Yönergede istenen format: "PC: X | Akümülatör: Y"
    print(f">> DURUM RAPORU    : [ PC: {program_sayaci} | Akümülatör (ACC): {akumulator} ]")

    adim = adim + 1

# ------------------------------------------------------------------------------
# BÖLÜM 4: PROGRAM BİTİŞ RAPORU
# ------------------------------------------------------------------------------
print("\n" + "=" * 65)
print("             SİMÜLASYON BAŞARIYLA TAMAMLANDI")
print("=" * 65)
print(f"Son Durum:")
print(f"  - Toplam Çalıştırılan Adım Sayısı : {adim - 1}")
print(f"  - Nihai Program Sayacı (PC)       : {program_sayaci}")
print(f"  - Akümülatördeki Nihai Sonuç (ACC): {akumulator}")
print("=" * 65)
