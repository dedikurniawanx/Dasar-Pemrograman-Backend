topup = ['Mobile Legends','PUBGM','Genshin Impact','CODM','Higgs Domino']
nominal = [10000,25000,50000,75000,100000]
pembayaran = ['DANA','OVO','ShopeePay','Pulsa']
total = 0
while True:
    print('========= Mau Topup Game Apa =========')
    for item in range(0,len(topup)):
        print(f'{item + 1}. {topup[item]}')
    game = input('Silahkan Pilih Game :')
    print('========== Mau Topup Berapa ==========')
    for i in range(0,len(nominal)):
        print(f'{i + 1}. {nominal[i]}')
    jumlah = int(input('Silahkan Pilih Nominal Anda Topup :'))
    total = nominal[jumlah-1]
   
    print('Pilih Metode Pembayaran :')
    for b in range(0,len(pembayaran)):
        print(f'{b + 1}. {pembayaran[b]}')
    metodebayar = int(input('Pilih Metode Pembayaran :'))

    bayar = int(input('Bayar : '))
    if bayar < total:
        print('Mohon Maaf, Uangmu Belum Cukup Silahkan Menabung Lagi. . .')
    else:
        print(f'Metode Pembayaran {pembayaran[metodebayar]}')
        print('Permintaan Anda Sedang Diproses')
        
    pilih = input('Mau Melakukan Topup Lagi ? [y/n] ')
    if pilih == 'y':
        continue
    else:
        print('Terimakasih, Sudah Menggunakan Jasa Dari Kami . . .')
        break