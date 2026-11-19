# BLM101 Bilgisayar Mühendisliğine Giriş - Dönem Projesi

## 📌 Öğrenci Bilgileri
- **Adı Soyadı:** Feyza Güreşen
- **Öğrenci Numarası:** 25360859088
- **Üniversite:** Bursa Teknik Üniversitesi
- **Bölüm:** Bilgisayar Mühendisliği
- **Ders:** BLM101 Bilgisayar Mühendisliğine Giriş
- **Repo Formatı:** `BLM101_25360859088_FeyzaGuresen`

---

## 🎯 Proje Konusu
**4. Proje: Makine Döngüsü ve Akümülatör (Accumulator) CPU Simülatörü**  
*(Öğrenci numarasının son rakamı 3 veya 8 olan öğrenciler için tanımlanan proje konusu)*

- **Ders Kitabı Referansı:** Chapter 2 (*2.1 Computer Architecture, 2.3 Program Execution: Fetch, Decode, Execute*)  
  *Referans Kitap:* J. Glenn Brookshear & Dennis Brylow, *Computer Science: An Overview* (13th Edition).

---

## 📂 Proje Dizin Yapısı

```text
BLM101_25360859088_FeyzaGuresen/
│
├── src/                      # Python kaynak kodları dizini
│   └── main.py               # Ana CPU simülatörü programı
│
├── sunum.pdf                 # En az 25-30 sayfa kuralına uygun 28 sayfalık teorik sunum (PDF)
├── sunum.pptx                # Sunumun düzenlenebilir PowerPoint formatı (28 Slayt)
└── README.md                 # Proje dokümantasyonu (Bu dosya)
```

---

## ⚙️ Kurulum ve Çalıştırma

### Gereksinimler
- **Python Sürümü:** Python 3.8 veya üzeri (Tavsiye edilen: Python 3.10+)
- **İşletim Sistemi:** Windows / macOS / Linux (Platform bağımsız)
- **Ekstra Kütüphane:** Simülatörün kendisi (`src/main.py`) tamamen saf standart Python ile yazılmıştır; **hiçbir harici kütüphane kurulumu gerektirmez**.

### Çalıştırma Adımları

1. Terminali (PowerShell veya Komut Satırı) proje klasöründe açınız:
   ```bash
   cd c:\Users\feyyz\OneDrive\Desktop\proje
   ```

2. Simülatörü çalıştırınız:
   ```bash
   python src/main.py
   ```

3. Program açıldığında karşınıza iki seçenek gelecektir:
   - `1`: Yönergede verilen hazır örnek komut dizisini (`LOAD 10`, `ADD 5`, `SUB 3`, `HALT`) otomatik çalıştırır.
   - `2`: Kendi komutlarınızı klavyeden girmenizi sağlar.

---

## 🧠 Proje ve Algoritma Açıklaması

### 1. Temel Mimari Yaklaşımı
Bu proje, bilgisayar mimarisinin en temel taşlarından biri olan **tek yazmaçlı (Akümülatör tabanlı)** bir işlemcinin donanım döngüsünü simüle eder.

Gereksiz karmaşıklıktan kaçınmak ve kısa sınavda (quiz) her satıra tam hakimiyet sağlayabilmek amacıyla kod; sınıflar (OOP) veya karmaşık harici fonksiyonlar yerine, donanımın doğal akışını taklit eden **modüler bölümler**, **`while` döngüsü** ve **`if-elif-else` karar blokları** ile tasarlanmıştır.

### 2. Donanım Bileşenlerinin Yazılımsal Temsili
İşlemcinin fiziksel donanım parçaları programda şu değişkenlerle modellenmiştir:

| Donanım Bileşeni | Değişken Adı | Görevi ve Açıklaması |
| :--- | :--- | :--- |
| **Akümülatör (ACC)** | `akumulator = 0` | Aritmetik işlemlerin bir terimini ve işlem sonucunu tutan ana çalışma yazmacı. |
| **Program Sayacı (PC)** | `program_sayaci = 0` | Bellekten sıradaki okunacak komutun adres/indis numarasını tutar. |
| **Komut Yazmacı (IR)** | `komut_yazmaci = ""` | Bellekten o anda çekilmiş (Fetch edilmiş) ham komut dizesini saklar. |
| **Ana Bellek (RAM)** | `bellek = [...]` | Komut satırlarının sırayla saklandığı liste veri yapısı. |
| **Çalışma Bayrağı** | `calisiyor = True` | HALT komutu gelene veya bellek bitene kadar işlemcinin saat vuruşunu sürdüren kontrol bayrağı. |

---

### 3. Makine Döngüsü (Machine Cycle) Aşamaları

Her bir saat vuruşunda (`while` döngüsü adımında) sırasıyla 3 aşama yürütülür:

```text
+-----------------------------------------------------------+
|                   1. FETCH (Komutu Getir)                 |
|  - Bellek[PC] okunur ve Komut Yazmacına (IR) aktarılır.   |
|  - Program Sayacı hemen 1 artırılır: PC = PC + 1          |
+-----------------------------+-----------------------------+
                              |
                              v
+-----------------------------------------------------------+
|                   2. DECODE (Komutu Çöz)                  |
|  - IR'deki metin parçalanır (split).                     |
|  - İşlem Kodu (Opcode) ve Sayısal Değer (Operand) ayrılır.|
+-----------------------------+-----------------------------+
                              |
                              v
+-----------------------------------------------------------+
|                  3. EXECUTE (Komutu Yürüt)                |
|  - if-elif-else blokları ile ilgili ALU işlemi yapılır.   |
|  - Sonuç doğrudan Akümülatör (ACC) üzerine yazılır.       |
|  - "PC: X | Akümülatör: Y" durum raporu basılır.         |
+-----------------------------------------------------------+
```

---

### 4. Desteklenen Komut Kümesi

| Komut | Açıklama | Donanımsal Karşılığı |
| :--- | :--- | :--- |
| `LOAD X` | Akümülatöre X değerini yükler | `akumulator = sayi` |
| `ADD X` | Akümülatördeki mevcut değere X ekler | `akumulator = akumulator + sayi` |
| `SUB X` | Akümülatördeki mevcut değerden X çıkarır | `akumulator = akumulator - sayi` |
| `MUL X` | Akümülatördeki mevcut değeri X ile çarpar | `akumulator = akumulator * sayi` |
| `HALT` | Programı ve işlemciyi durdurur | `calisiyor = False` |

---

### 5. Örnek Yürütme ve İzleme (Trace) Tablosu

Yönergede belirtilen `LOAD 10`, `ADD 5`, `SUB 3`, `HALT` komutları çalıştırıldığında simülasyonun adım adım izleme tablosu:

| Döngü Adımı | Bellek Adresi | Yürütülen Komut (IR) | İşlem Mantığı | PC Değeri | Akümülatör (ACC) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **Başlangıç** | - | - | İşlemci sıfırlandı | 0 | 0 |
| **1. Adım** | `0` | `LOAD 10` | Akümülatöre 10 yazıldı | 1 | **10** |
| **2. Adım** | `1` | `ADD 5` | 10 + 5 toplandı | 2 | **15** |
| **3. Adım** | `2` | `SUB 3` | 15 - 3 çıkarıldı | 3 | **12** |
| **4. Adım** | `3` | `HALT` | İşlemci durduruldu | 4 | **12** |

---

## 🎤 Bireysel Kısa Sınav (Quiz) Hazırlık Rehberi (35 Puan)

Hocaların sözlü sınavda kod üzerinden yöneltebileceği muhtemel sorular ve net cevapları:

1. **Soru:** *"Program Sayacı (PC) neden komut okunur okunmaz hemen 1 artırılıyor?"*  
   **Cevap:** Çünkü işlemci komutu bellekten çeker çekmez bir sonraki çevrimde hangi adrese gideceğini şimdiden hazır etmek zorundadır. Aksi halde bir sonraki Fetch adresi bilinemez.

2. **Soru:** *"ADD 5 komutunda toplanacak birinci sayı nerede saklanıyor?"*  
   **Cevap:** Akümülatör mimarisinde komutlar tek adreslidir. Birinci sayı her zaman zaten Akümülatör'ün içinde bulunan mevcut değerdir. Komut sadece ikinci sayıyı (5) belirtir.

3. **Soru:** *"Kodunuza bölme (DIV X) komutu eklemek istesem ne yaparsınız?"*  
   **Cevap:** `src/main.py` dosyasındaki `EXECUTE` bölümüne bir `elif islem == "DIV":` şartı açarak `akumulator = akumulator // sayi` satırını ve durum çıktısını eklerim.

4. **Soru:** *"HALT komutunun gerçek donanımdaki karşılığı nedir?"*  
   **Cevap:** İşlemciye giden saat sinyalini (clock pulse) durdurarak işlemciyi uyku / bekleme moduna geçirmektir. Kodumuzda ise `calisiyor = False` yapılarak `while` döngüsünden çıkılır.

---

## 📊 Sunum Dosyası Bilgisi
- **sunum.pdf:** Yönergedeki *"en az 25-30 sayfalık detaylı bir sunum"* kuralına tam uygun olarak hazırlanmış **28 sayfalık** PDF dosyası reponun ana dizinindedir.
- **sunum.pptx:** Microsoft PowerPoint ile sunum yapabilmeniz veya slaytları düzenleyebilmeniz için hazırlanan 28 slaytlık sunum dosyasıdır.
