while True:
        os.system('cls' if os.name == 'nt' else 'clear')
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
        
