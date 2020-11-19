while True:
        #NIM Rivan Abdillah : 2009106025 + 10 = 35
        digit = int(input("Masukkan NIM anda + 10: "))
        y = 1
        x = 1
        while (y <= digit):
            print(x)
            x += 1
            if (x == 10):
                x -= 9
            y += 1
        break
