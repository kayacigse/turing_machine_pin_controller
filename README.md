# turing_machine_pin_controller

## Proje Hakkında

Bu proje, Turing makinesi kuramını gerçek hayat uygulaması olarak modelleyen bir yazılım simülasyonudur. Kullanıcıdan alınan 4 haneli PIN kodunun, sistemde kayıtlı sabit PIN ile eşleşip eşleşmediğini kontrol eden bir Turing makinesi tasarlanmıştır. Proje, Turing makinelerinin temel çalışma prensiplerini anlamak ve gerçek bir doğrulama sürecini simüle etmek amacıyla geliştirilmiştir.

## Problem Tanımı

- **Alfabe:** {'0', '1', ..., '9', '#', 'X', 'Y', 'B'}
- **Girdi Yapısı:** `KullanıcıPIN#SabitPIN#`  
  Örnek: `1234#1234#`
- **Amaç:**  
  Kullanıcı tarafından girilen PIN ile sistemde saklanan sabit PIN aynı ise makine “kabul” durumuna geçer, değilse “reddet” durumuna geçer.

## Projenin Çalışma Mantığı

1. Kullanıcıdan 4 haneli PIN alınır.
2. Sistem PIN’i sabit olarak kod içinde tanımlıdır (örneğin `"1234"`).
3. Girdi, Turing makinesi formatına (kullanıcı PIN + `#` + sistem PIN + `#`) dönüştürülür.
4. Turing makinesi simülatörü bu bant üzerinde adım adım çalışarak her iki PIN’in karakterlerini karşılaştırır.
5. Her adımda bant durumu ve ok pozisyonu konsola yazdırılır.
6. Tüm karakterler eşleşirse **"Şifre doğru (KABUL EDİLDİ)"**, eşleşmezse **"Şifre hatalı (REDDEDİLDİ)"** mesajı verilir.

## Kullanılan Teknolojiler

- Programlama Dili: Python 3
- Konsol tabanlı uygulama

## Kurulum ve Çalıştırma

1. Python 3 yüklü olmalıdır.
2. Proje dosyasını indirin veya kopyalayın.
3. Komut satırında proje dizinine gidin.
4. Programı çalıştırmak için:

```bash
python turing_machine_pin.py
```

## Örnek Çıktılar

<img width="564" alt="Ekran Resmi 2025-06-03 20 28 52" src="https://github.com/user-attachments/assets/2a6a5a11-07dd-470f-b3b5-1f9ce6599da7" />

<img width="544" alt="Ekran Resmi 2025-06-03 20 29 21" src="https://github.com/user-attachments/assets/a9859a5a-4d31-4cc8-9533-181ef404425b" />

<img width="544" alt="Ekran Resmi 2025-06-03 20 29 21" src="https://github.com/user-attachments/assets/53a3eced-a27d-4750-a376-eba12bece6b5" />

<img width="542" alt="Ekran Resmi 2025-06-03 20 29 38" src="https://github.com/user-attachments/assets/df254256-6e9c-4443-81cc-e001a576da93" />

