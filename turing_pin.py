def turing_machine(input_tape):
    tape = list(input_tape)   # Giriş bandını karakter listesine çevir
    head = 0                  # Başlangıçta ok (head) en solda
    state = 'q0'              # Başlangıç durumu

    print(f"Başlangıç Bandı: {''.join(tape)}")

    while True:
        # Her adımda geçerli durumu ve head konumunu yazdır
        print(f"[{state}] {''.join(tape)}  (ok => {head})")

        if state == 'q0':
            # Kullanıcı PIN'indeki rakamı al
            if tape[head].isdigit():
                current_digit = tape[head]  # Rakamı kaydet
                tape[head] = 'X'           # İşlenmiş olarak işaretle
                state = 'q1'
                head += 1
            elif tape[head] == '#':
                # Tüm karakterler karşılaştırıldıysa kabul
                state = 'q_accept'
            else:
                state = 'q_reject'

        elif state == 'q1':
            # Kullanıcı PIN'ini geç, sistem PIN'ine ulaş
            while tape[head] != '#':
                head += 1
            head += 1
            state = 'q2'

        elif state == 'q2':
            # Sabit PIN'den karşılık gelen rakamı bul
            if tape[head].isdigit():
                if tape[head] == current_digit:
                    tape[head] = 'Y'       # Eşleşme varsa işaretle
                    state = 'q3'
                    head -= 1
                else:
                    state = 'q_reject'     # Uyuşmazlık varsa reddet
            else:
                head += 1                  # Diğer karakterleri geç

        elif state == 'q3':
            # Ayıraca kadar geri dön
            while tape[head] != '#':
                head -= 1
            head -= 1
            state = 'q4'

        elif state == 'q4':
            # Yeni karşılaştırılmamış kullanıcı PIN rakamını bul
            if tape[head] == 'X':
                head += 1
                state = 'q0'
            else:
                head -= 1

        elif state == 'q_accept':
            print(f"[{state}] {''.join(tape)}")
            print("Şifre doğru (KABUL EDİLDİ)")
            break

        elif state == 'q_reject':
            print(f"[{state}] {''.join(tape)}")
            print("Şifre hatalı (REDDEDİLDİ)")
            break


# Kullanıcıdan PIN girişi alınır
kullanici_pin = input("Lütfen 4 haneli PIN kodunuzu girin: ")

# Giriş doğrulama
if len(kullanici_pin) != 4 or not kullanici_pin.isdigit():
    print("PIN kodu 4 haneli sayılardan oluşmalıdır!")
    exit()

# Sabit sistem PIN’i
sabit_pin = "1234"

# Bant oluşturma: kullanıcıPIN#sabitPIN#
tape = kullanici_pin + "#" + sabit_pin + "#"

# Turing makinesini çalıştır
turing_machine(tape)
