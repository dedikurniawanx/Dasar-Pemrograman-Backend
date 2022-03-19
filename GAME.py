l_genre = ['FPS', 'MOBA' , 'RPG']
l_fps = ['Apex Legends', 'Fornite' , 'PUBG MOBILE', 'PUBG NEW STATE']
l_moba = ['Arena of Valor', 'Mobile Legends', 'Vainglory', 'Heroes Arena']
l_rpg = ['Genshin Impact', 'Phantom of The Kill', 'Kingdom Hearts Unchained X', 'Granblue Fantasy']
cart = []
while True:
    print('========= Silahkan Pilih Genre Game =========')
    for item in range(0, len(l_genre)):
        print(f'{item + 1}. {l_genre[item]} ')
    genre = input('Silahkan Pilih Genre Game ')
    if genre == '1':
        for item_genre in range(0, len(l_fps)):
            print(f'{item_genre + 1}. {l_fps[item_genre]} ')
        ulang = True
        while ulang:
            select_genre = int(
                input(f'Silahkan Pilih Game Fps 1-{len(l_fps)} '))
            if select_genre <= 0 or select_genre > len(l_fps):
                print('Silahkan Masukan Pilihan')
                for item_genre in range(0, len(l_fps)):
                    print(f'{item_genre + 1}. {l_fps[item_genre]} ')
                continue
            else:
                cart.append(l_fps[select_genre - 1])
                print('==== Game Yang Terpilih ====')
                for list_cart in range(0, len(cart)):
                    print(f'{list_cart +1} . {cart[list_cart]}')
                ulang = False
            continue
    elif genre == '2':
        for item_genre2 in range(0, len(l_moba)):
            print(f'{item_genre2 + 1}. {l_moba[item_genre2]} ')
        ulang = True
        while ulang:
            select_genre = int(
                input(f'Silahkan Pilih Game FPS 1-{len(l_moba)} '))
            if select_genre <= 0 or select_genre > len(l_moba):
                print('Silahkan Masukkan Pilihan ')
                for item_genre2 in range(0, len(l_moba)):
                    print(
                        f'{item_genre2 + 1}. {l_moba[item_genre2]} ')
            else:
                cart.append(l_moba[select_genre - 1])
                print('==== Game Yang Terpilih ====')
                for list_cart in range(0, len(cart)):
                    print(f'{list_cart +1} . {cart[list_cart]}')
                    ulang = False
                continue
    elif genre == '3':
        for item_genre3 in range(0, len(l_rpg)):
            print(f'{item_genre3 + 1}. {l_rpg[item_genre3]} ')
        ulang = True
        while ulang:
            select_genre = int(
                input(f'Silahkan Pilih Game RPG 1-{len(l_rpg)} '))
            if select_genre <= 0 or select_genre > len(l_rpg):
                print('Silahkan Masukkan Pilihan')
                for item_genre3 in range(0, len(l_rpg)):
                    print(f'{item_genre3 + 1}. {l_rpg[item_genre3]} ')
            else:
                cart.append(l_rpg[select_genre - 1])
                print('==== Game Yang Terpilih ====')
                for list_cart in range(0, len(cart)):
                    print(f'{list_cart +1} . {cart[list_cart]}')
                    ulang = False
            continue
    else:
        print('Genre Game Belum Tersedia')
        continue
    pilih = input('Mau Memilih Game Lagi ? [y/n] ')
    if pilih == 'y':
        continue
    else:
        print('==== Game Yang Terpilih ====')
        for list_cart in range(0, len(cart)):
            print(f'{list_cart +1} . {cart[list_cart]}')
        break