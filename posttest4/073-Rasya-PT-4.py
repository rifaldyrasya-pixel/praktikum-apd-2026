username_db = "rasya"
pin_db = "073"

saldo = 1000000

percobaan = 3
login_berhasil = False
while percobaan > 0:
    print("==========================================")
    print("          SISTEM LOGIN ATM BANK           ")
    print("==========================================")
    input_user = input("Masukkan Username : ")
    input_pin = input("Masukkan PIN (3 digit): ")
    print("==========================================")
    
    if input_user == username_db and input_pin == pin_db:
        print("Login Berhasil!")
        print("==========================================\n")
        login_berhasil = True
        break
    else:
        percobaan -= 1
        if percobaan > 0:
            print("Login Gagal! Sisa percobaan:", percobaan)
            print("==========================================\n")
        else:
            print("Login Gagal!")
            print("Akun Anda Terblokir!")
            print("==========================================")

while login_berhasil:
    print("\n==========================================")
    print("             MENU UTAMA ATM               ")
    print("==========================================")
    print("[1] Cek Saldo")
    print("[2] Tarik Tunai")
    print("[3] Setor Tunai")
    print("[4] Keluar")
    print("==========================================")
    
    pilihan = input("Pilih menu (1-4): ")
    print("==========================================")
    
    if pilihan == "1":
        print("Informasi Saldo")
        print("Saldo Anda saat ini: Rp", saldo)
        
    elif pilihan == "2":
        print("Tarik Tunai")
        print("Pilihan pecahan uang:")
        print("1. Kelipatan Rp 50.000")
        print("2. Kelipatan Rp 100.000")
        opsi_kelipatan = input("Pilih opsi kelipatan (1/2): ")
        
        if opsi_kelipatan == "1" or opsi_kelipatan == "2":
            nominal_input = input("Masukkan nominal tarik tunai: ")
            
            if nominal_input.isdigit():
                nominal = int(nominal_input)
                
                if opsi_kelipatan == "1" and nominal % 50000 != 0:
                    print("Nominal harus kelipatan Rp 50.000!")
                elif opsi_kelipatan == "2" and nominal % 100000 != 0:
                    print("Nominal harus kelipatan Rp 100.000!")
                elif nominal <= 0:
                    print("Nominal penarikan harus lebih dari 0!")
                elif nominal > saldo:
                    print("Saldo tidak mencukupi!")
                else:
                    saldo -= nominal
                    print("Penarikan Tunai Berhasil!")
                    print("Nominal ditarik : Rp", nominal)
                    print("Sisa Saldo Anda  : Rp", saldo)
            else:
                print("Input harus berupa angka!")
        else:
            print("Opsi kelipatan tidak valid!")
            
    elif pilihan == "3":
        print("Setor Tunai")
        nominal_input = input("Masukkan nominal setor tunai: ")
        
        if nominal_input.isdigit():
            nominal = int(nominal_input)
            
            if nominal <= 0:
                print("Nominal setor harus lebih dari 0!")
            elif nominal % 50000 != 0:
                print("Nominal harus kelipatan Rp 50.000!")
            else:
                saldo += nominal
                print("Setor Tunai Berhasil!")
                print("Nominal disetor : Rp", nominal)
                print("Total Saldo Anda: Rp", saldo)
        else:
            print("Input harus berupa angka!")
            
    elif pilihan == "4":
        print("Terima kasih telah menggunakan layanan ATM kami.")
        print("==========================================")
        break
        
    else:
        print("Pilihan menu tidak valid! Silakan pilih angka 1-4.")