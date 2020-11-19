import os
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def welcome():
    print()
    print("===============================================")
    print("\tSelamat Datang di Toko Kue Sule")
    print("===============================================")
    print()
    time.sleep(2)
    menu()

def menu():
    clear_screen()
    print("\nDi sini kami mengadakan berbagai promo")
    print("- Jika membeli 5 hingga 20 kue coklat akan mendapat diskon 7%")
    print("- Jika membeli 21 hingga 35 kue coklat akan mendapat diskon 12%")
    print("- Jika membeli 4 hingga 15 kue keju akan mendapat diskon 10%")
    print("- Jika membeli 16 hingga 25 kue keju akan mendapat diskon 15%")
    print()
    print("Anda ingin membeli kue apa?")
    print("1. Kue Keju")
    print("2. Kue Coklat")

    menu_kue = str(input("Masukkan opsi yang anda inginkan: "))

    if menu_kue == "1":
        kue_keju()
    elif menu_kue == "2":
        kue_coklat()
    else:
        print("Kesalahan input opsi")
        time.sleep(2)
        menu()

def kue_keju():
    clear_screen()
    keju = int(input("Masukkan jumlah kue keju yang anda ingin beli: "))

    if (keju >= 4) and (keju <= 15):
        keju_int = keju * 6000
        diskon = keju_int * (10/100)
        total_keju = keju_int - diskon
        keju_blm = "Total biaya anda adalah Rp. {}".format(keju_int)
        print(keju_blm)
        print("Selamat anda mendapatkan diskon 10%")
        keju_total = "Total biaya anda setelah diskon adalah Rp. {}".format(total_keju)
        print(keju_total)
        back_to_menu()
    elif (keju >= 16) and (keju <= 25):
        keju_int = keju * 6000
        diskon = keju_int * (15/100)
        total_keju = keju_int - diskon
        keju_blm = "Total biaya anda adalah Rp. {}".format(keju_int)
        print(keju_blm)
        print("Selamat anda mendapatkan diskon 15%")
        keju_total = "Total biaya anda setelah diskon adalah Rp. {}".format(total_keju)
        print(keju_total)
        back_to_menu()
    else:
        print("Nominal tidak diketahui")
        print("Harap masukkan kembali")
        time.sleep(3)
        kue_keju()

def kue_coklat():
    clear_screen()
    coklat = int(input("Masukkan jumlah kue coklat yang anda ingin beli: "))

    if (coklat >= 5) and (coklat <= 20):
        coklat_int = coklat * 3500
        diskon = coklat_int * (7/100)
        total_coklat = coklat_int - diskon
        coklat_blm = "Total biaya anda adalah Rp. {}".format(coklat_int)
        print(coklat_blm)
        print("Selamat anda mendapatkan diskon 7%")
        coklat_total = "Total biaya anda setelah diskon adalah Rp. {}".format(total_coklat)
        print(coklat_total)
        back_to_menu()
    elif (coklat >= 21) and (coklat <= 35):
        coklat_int = coklat * 3500
        diskon = coklat_int * (12/100)
        total_coklat = coklat_int - diskon
        coklat_blm = "Total biaya anda adalah Rp. {}".format(coklat_int)
        print(coklat_blm)
        print("Selamat anda mendapatkan diskon 12%")
        coklat_total = "Total biaya anda setelah diskon adalah Rp. {}".format(total_coklat)
        print(coklat_total)
        back_to_menu()
    else:
        print("Nominal tidak diketahui")
        print("Harap masukkan kembali")
        time.sleep(3)
        kue_coklat()


def back_to_menu():
    print()
    print("============================================")
    back = str(input("Tertarik untuk membeli kue yang lain? (y/n):"))
    print("============================================")
    print()

    if back == "y":
        menu()
    elif back == "n":
        clear_screen()
        print("\t\t===============================================================")
        print("\t\t\tTerima kasih telah berkunjung ke toko kue Sule")
        print("\t\t===============================================================")
        time.sleep(3)
        exit()
    else:
        print("Variabel tidak diketahui")
        time.sleep()
        back_to_menu()

if __name__ == "__main__":
    while True:
        welcome()