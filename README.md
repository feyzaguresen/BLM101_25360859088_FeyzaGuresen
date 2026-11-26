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

- **Ders Kitabı Referansı:** Bölüm 2 (*2.1 Bilgisayar Mimarisi, 2.3 Programın Çalıştırılması: Alma, Çözümleme, Yürütme*)  
  *Referans Kitap:* J. Glenn Brookshear & Dennis Brylow, *Bilgisayar Bilimine Giriş* (12. Baskı - Çeviri: Pearson).

---

## 📂 Proje Dizin Yapısı

```text
BLM101_25360859088_FeyzaGuresen/
│
├── src/
│   └── main.py               # Ana CPU simülatörü programı
│
├── sunum.pdf                 # 27 sayfalık teorik sunum (PDF)
└── README.md                 # Proje dokümantasyonu (Bu dosya)
```

---

## ⚙️ Kurulum ve Çalıştırma

**Gereksinim:** Python 3.8 veya üzeri. Program saf standart Python ile yazılmıştır, harici kütüphane gerekmez.

1. Terminali proje klasöründe açınız:
   ```bash
   cd BLM101_25360859088_FeyzaGuresen
   ```

2. Simülatörü çalıştırınız:
   ```bash
   python src/main.py
   ```

3. Program açıldığında iki seçenek sunar:
   - `1`: Hazır komut dizisini (`LOAD 10`, `ADD 5`, `SUB 3`, `MUL 2`, `DIV 4`, `HALT`) çalıştırır.
   - `2`: Kullanıcıya adım adım sorular sorarak kendi programını oluşturur: önce başlangıç sayısı (`LOAD X`), ardından işlem (`1 = Toplama`, `2 = Çıkarma`, `3 = Çarpma`, `4 = Bölme`) ve sayı sorulur. *"Başka işlem eklemek ister misiniz? (e/h)"* sorusuna `h` denince giriş biter ve `HALT` komutu otomatik eklenir.

Desteklenen komutlar: `LOAD X`, `ADD X`, `SUB X`, `MUL X`, `DIV X`, `HALT`

---

## 🧠 Proje ve Algoritma Açıklaması

Bu proje, **tek yazmaçlı (Akümülatör tabanlı)** bir işlemcinin makine döngüsünü simüle eder. Kod; sınıflar (OOP) veya kendi yazılmış fonksiyonlar (`def`) kullanılmadan, `while` döngüsü ve `if-elif-else` karar blokları ile yazılmıştır.

### Donanım Bileşenlerinin Yazılımsal Temsili

| Donanım Bileşeni | Değişken Adı | Görevi |
| :--- | :--- | :--- |
| **Akümülatör (ACC)** | `akumulator = 0` | İşlem sonuçlarının tutulduğu ana çalışma yazmacı. |
| **Program Sayacı (PC)** | `pc = 0` | Sıradaki okunacak komutun bellek adresini tutar. |
| **Komut Yazmacı (IR)** | `ir = ""` | Bellekten o anda alınan komutu saklar. |
| **Ana Bellek (RAM)** | `bellek = []` | Komutların sırayla saklandığı liste. |
| **Çalışma Bayrağı** | `calisiyor = True` | HALT gelene veya bellek bitene kadar döngüyü sürdürür. |

### Desteklenen Komut Kümesi

| Komut | Açıklama | Donanımsal Karşılığı |
| :--- | :--- | :--- |
| `LOAD X` | Akümülatöre X sayısını yükler | `akumulator = sayi` |
| `ADD X` | Akümülatördeki sayıya X ekler | `akumulator = akumulator + sayi` |
| `SUB X` | Akümülatördeki sayıdan X çıkarır | `akumulator = akumulator - sayi` |
| `MUL X` | Akümülatördeki sayıyı X ile çarpar | `akumulator = akumulator * sayi` |
| `DIV X` | Akümülatördeki sayıyı X'e böler (Tamsayı bölmesi) | `akumulator = akumulator // sayi` *(0'a bölme korumalı)* |
| `HALT` | Programı ve işlemciyi durdurur | `calisiyor = False` |

### Makine Döngüsü (Fetch - Decode - Execute)

Her döngü adımında sırasıyla şu 3 aşama yürütülür:

```text
+-----------------------------------------------------------+
|                   1. FETCH (Komutu Getir)                 |
|  - Bellek[PC] okunur ve Komut Yazmacına (IR) aktarılır.   |
|  - Program Sayacı hemen 1 artırılır: PC = PC + 1          |
|  - PC bellek sınırını aşarsa döngü durdurulur.            |
+-----------------------------+-----------------------------+
                              |
                              v
+-----------------------------------------------------------+
|                   2. DECODE (Komutu Çöz)                  |
|  - IR'deki metin parçalanır (split).                      |
|  - İşlem Kodu (Opcode) ve Sayısal Değer (Operand) ayrılır.|
+-----------------------------+-----------------------------+
                              |
                              v
+-----------------------------------------------------------+
|                  3. EXECUTE (Komutu Yürüt)                |
|  - if-elif-else blokları ile ilgili işlem yapılır.        |
|  - Sonuç doğrudan Akümülatör (ACC) üzerine yazılır.       |
|  - "PC: X | Akümülatör: Y" durum raporu basılır.          |
+-----------------------------------------------------------+
```

### Örnek Yürütme ve İzleme (Trace) Tablosu

`LOAD 10`, `ADD 5`, `SUB 3`, `MUL 2`, `DIV 4`, `HALT` programının adım adım izlemesi:

| Döngü Adımı | Bellek Adresi | Yürütülen Komut (IR) | İşlem Mantığı | PC Değeri | Akümülatör (ACC) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **Başlangıç** | - | - | İşlemci sıfırlandı | 0 | 0 |
| **1. Adım** | `0` | `LOAD 10` | Akümülatöre 10 yazıldı | 1 | **10** |
| **2. Adım** | `1` | `ADD 5` | 10 + 5 toplandı | 2 | **15** |
| **3. Adım** | `2` | `SUB 3` | 15 - 3 çıkarıldı | 3 | **12** |
| **4. Adım** | `3` | `MUL 2` | 12 * 2 çarpıldı | 4 | **24** |
| **5. Adım** | `4` | `DIV 4` | 24 // 4 bölündü | 5 | **6** |
| **6. Adım** | `5` | `HALT` | İşlemci durduruldu | 6 | **6** |

> **Not:** PC, komut alındıktan (Fetch) hemen sonra artırıldığı için her adımın sonunda **bir sonraki komutun adresini** gösterir.

---

## 📊 Sunum Dosyası Bilgisi
- **sunum.pdf:** `src/main.py` simülatörü, komut kümesi (`LOAD`, `ADD`, `SUB`, `MUL`, `DIV`, `HALT`) ve makine döngüsü teorisini içeren 27 sayfalık sunum dosyasıdır.
