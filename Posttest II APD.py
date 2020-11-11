import os
import time

pesan_mkn = ['Undefined','Undefined','Undefined','0','0','0']

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def welcome():
    clear_screen()
    print()
    print("\t=======================================================")
    print("\t\tSelamat Datang di Warung Valorant")
    print("\t=======================================================")
    print()
    time.sleep(3)
    show_menu()
    

def show_menu():
    clear_screen()
    print("[1]Silahkan pilih 1 untuk memesan makanan")
    print("[2]Silahkan pilih 2 untuk memesan minuman")
    print("[3]Silahkan pilih 3 untuk memesan sambal")
    print("[5]Silahkan pilih 4 jika selesai memesan")
    print("[0]Silahkan pilih 0 untuk keluar dari warung kami")

    menu = str(input("Silah pilih menu yang anda inginkan: "))

    if menu == '1':
        makanan()
    elif menu == '2':
        minuman()
    elif menu == '3':
        sambal()
    elif menu == '4':
        kelar()
    elif menu == '0':
        clear_screen()
        print("\n==========================================================")
        print("\tTerima kasih telah mampir di warung kami")
        print("==========================================================\n")
        time.sleep(1.5)
        exit()

def back_to_menu():
    print("\n================================================")
    input("Apakah anda ingin memesan yang lain? Tekan Enter: ")
    print("================================================\n")
    show_menu()

def makanan():
    clear_screen()
    print("="*20)
    print("1. Nasi goreng biasa   Rp 12000")
    print("2. Nasi goreng spesial Rp 20000")
    print("3. Ayam goreng lalapan Rp 15000")
    print("4. Ayam geprek mercon  Rp 16000")
    print("0. Kembali ke menu utama")
    print("="*20)
    
    makan = str(input("Silahkan pilih nomor yang anda inginkan: "))

    if makan == '1':
        mkn = "Nasi goreng biasa seharga Rp 12000"
        print("%s" % (mkn))
        pesan_mkn.pop(0)
        pesan_mkn.insert(0,mkn)
        clear_screen()
        print("="*42)
        mkn_brp = int(input("\tAnda ingin pesan berapa? "))
        print("="*42)
        mkn_total = mkn_brp * 12000
        print("Total biaya makan sementara: Rp %d" % (mkn_total))
        pesan_mkn.pop(3)
        pesan_mkn.insert(3,mkn_total)
    elif makan == '2':
        mkn = "Nasi goreng spesial seharga Rp 20000"
        print("%s" % (mkn))
        pesan_mkn.pop(0)
        pesan_mkn.insert(0,mkn)
        clear_screen()
        print("="*42)
        mkn_brp = int(input("\tAnda ingin pesan berapa? "))
        print("="*42)
        mkn_total = mkn_brp * 20000
        print("Total biaya makan sementara: Rp %d" % (mkn_total))
        pesan_mkn.pop(3)
        pesan_mkn.insert(3,mkn_total)
    elif makan == '3':
        mkn = "Ayam goreng lalapan seharga Rp 15000"
        print("%s" % (mkn))
        pesan_mkn.pop(0)
        pesan_mkn.insert(0,mkn)
        clear_screen()
        print("="*42)
        mkn_brp = int(input("\tAnda ingin pesan berapa? "))
        print("="*42)
        mkn_total = mkn_brp * 15000
        print("Total biaya makan sementara: Rp %d" % (mkn_total))
        pesan_mkn.pop(3)
        pesan_mkn.insert(3,mkn_total)
    elif makan == '4':
        mkn = "Ayam geprek mercon seharga Rp 16000"
        print("%s" % (mkn))
        pesan_mkn.pop(0)
        pesan_mkn.insert(0,mkn)
        clear_screen()
        print("="*42)
        mkn_brp = int(input("\tAnda ingin pesan berapa? "))
        print("="*42)
        mkn_total = mkn_brp * 16000
        print("Total biaya makan sementara: Rp %d" % (mkn_total))
        pesan_mkn.pop(3)
        pesan_mkn.insert(3,mkn_total)
    elif makan == '0':
        print("Anda kembali ke menu utama")
    back_to_menu()

def minuman():
    clear_screen()
    print("="*20)
    print("1. Es teh        Rp 4000")
    print("2. Teh hangat    Rp 3000")
    print("3. Soda gembira  Rp 5000")
    print("4. Kopi susu     Rp 4000")
    print("0. Kembali ke menu utama")
    print("="*20)

    minum = str(input("Silahkan pilih nomor yang anda inginkan: "))

    if minum == '1':
        mnm = "Anda memesan Es teh seharga Rp 4000"
        print("%s" % (mnm))
        pesan_mkn.pop(1)
        pesan_mkn.insert(1,mnm)
        clear_screen()
        print("="*42)
        mnm_brp = int(input("\tAnda ingin pesan berapa? "))
        print("="*42)
        mnm_total = mnm_brp * 4000
        print("Total biaya minum sementara: %d" % (mnm_total))
        pesan_mkn.pop(4)
        pesan_mkn.insert(4,mnm_total)
    elif minum == '2':
        mnm = "Anda memesan Teh hangat seharga Rp 3000"
        print("%s" % (mnm))
        pesan_mkn.pop(1)
        pesan_mkn.insert(1,mnm)
        clear_screen()
        print("="*42)
        mnm_brp = int(input("\tAnda ingin pesan berapa? "))
        print("="*42)
        mnm_total = mnm_brp * 3000
        print("Total biaya minum sementara: %d" % (mnm_total))
        pesan_mkn.pop(4)
        pesan_mkn.insert(4,mnm_total)
    elif minum == '3':
        mnm = "Soda gembira seharga Rp 5000"
        print("%s" % (mnm))
        pesan_mkn.pop(1)
        pesan_mkn.insert(1,mnm)
        clear_screen()
        print("="*42)
        mnm_brp = int(input("\tAnda ingin pesan berapa? "))
        print("="*42)
        mnm_total = mnm_brp * 5000
        print("Total biaya minum sementara: %d" % (mnm_total))
        pesan_mkn.pop(4)
        pesan_mkn.insert(4,mnm_total)
    elif minum == '4':
        mnm = "Kopi susu seharga Rp 4000"
        print("%s" % (mnm))
        pesan_mkn.pop(1)
        pesan_mkn.insert(1,mnm)
        clear_screen()
        print("="*42)
        mnm_brp = int(input("\tAnda ingin pesan berapa? "))
        print("="*42)
        mnm_total = mnm_brp * 4000
        print("Total biaya minum sementara: %d" % (mnm_total))
        pesan_mkn.pop(4)
        pesan_mkn.insert(4,mnm_total)
    elif minum == '0':
        print("Anda kembali ke menu utama")
    back_to_menu()

def sambal():
    clear_screen()
    print("="*20)
    print("Untuk sambal kami berikan secara gratis")
    print("1. Sambal matah")
    print("2. Sambal terasi")
    print("3. Sambal ijo")
    print("4. Saos sambal")
    print("0. Kembali ke menu utama")
    print("="*20)

    sambal = str(input("Silahkan pilih nomor yang anda inginkan: "))

    if sambal == '1':
        smbl = "Sambal matah"
        pesan_mkn.pop(2)
        pesan_mkn.insert(2,smbl)
        print("Anda memesan sambal matah")
    elif sambal == '2':
        smbl = "Sambal terasi"
        pesan_mkn.pop(2)
        pesan_mkn.insert(2,smbl)
        print("Anda memesan sambal terasi")
    elif sambal == '3':
        smbl = "Sambal ijo"
        pesan_mkn.pop(2)
        pesan_mkn.insert(2,smbl)
        print("Anda memesan sambal ijo")
    elif sambal == '4':
        smbl = "Saos sambal"
        pesan_mkn.pop(2)
        pesan_mkn.insert(2,smbl)
        print("Anda memesan saos sambal")
    elif sambal == '5':
        print("Anda kembali ke menu utama")
    back_to_menu()

def kelar():
    clear_screen()
    print("=====================================\n")
    print("Anda memesan:")
    print("%s" % (pesan_mkn[0]))
    print("%s" % (pesan_mkn[1]))
    print("%s" % (pesan_mkn[2]))
    harga_makanan = int(pesan_mkn[3])
    harga_minuman = int(pesan_mkn[4])
    total = harga_makanan+harga_minuman
    print("Total: Rp. %s" % (total))
    print("=====================================")
    selesai()

def selesai():
    mesen = str(input("Apakah anda ingin menambah pesanan? (y/n): "))
    if mesen == 'y':
        show_menu()
    else:
        clear_screen()
        print("==============================================================")
        print("\tSelamat menikmati hidangan yang kami sediakan ^^")
        print("==============================================================")
        time.sleep(1.5)
        exit()

if __name__ == "__main__":
    while True:
        welcome()
