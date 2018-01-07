def tic_tac_toe():
    canvas = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    end = False
    kemenangan_kombinasi = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

    def pilih():
        print(canvas[0], canvas[1], canvas[2])
        print(canvas[3], canvas[4], canvas[5])
        print(canvas[6], canvas[7], canvas[8])
        print()

    def player1():
        n = pilih_nomor()
        if canvas[n] == "X" or canvas[n] == "O":
            print("\nTempat Sudah Terisi, Silahkan Pilih Tempat Lain")
            player1()
        else:
            canvas[n] = "X"

    def player2():
        n = pilih_nomor()
        if canvas[n] == "X" or canvas[n] == "O":
            print("\nTempat Sudah Terisi, Silahkan Pilih Tempat Lain")
            player2()
        else:
            canvas[n] = "O"

    def pilih_nomor():
        while True:
            while True:
                a = input()
                try:
                    a  = int(a)
                    a -= 1
                    if a in range(0, 9):
                        return a
                    else:
                        print("\nKamu Tidak berada di Canvas, Coba Lagi")
                        continue
                except ValueError:
                   print("\nItu Bukan Angka, Coba Lagi")
                   continue

    def cek_canvas():
        jumlah = 0
        for a in kemenangan_kombinasi:
            if canvas[a[0]] == canvas[a[1]] == canvas[a[2]] == "X":
                print("Player 1 Menang!\n")
                print("Selamat!\n")
                return True

            if canvas[a[0]] == canvas[a[1]] == canvas[a[2]] == "O":
                print("Player 2 Menang!\n")
                print("Selamat!\n")
                return True
        for a in range(9):
            if canvas[a] == "X" or canvas[a] == "O":
                jumlah += 1
            if jumlah == 9:
                print("Game Berakhir Seri\n")
                return True

    while not end:
        pilih()
        end = cek_canvas()
        if end == True:
            break
        print("Player 1 Pilih Tempat Anda")
        player1()
        print()
        pilih()
        end = cek_canvas()
        if end == True:
            break
        print("Player 2 Pilih Tempat Anda")
        player2()
        print()

    if input("Mulai Lagi (y/n)\n") == "y":
        print()
        tic_tac_toe()

tic_tac_toe()
