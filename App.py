import function

daftar_kontak = []
daftar_kontak.append({
    'nama' : 'Dedi',
    'email' : 'dedikurniawan@yahoo.com',
    'telepon' : '082'
})

while True:
    print('## Menu')
    print('1. Daftar Kontak')
    print('2. Tambah Kontak')
    print('3. Hapus Kontak ')
    print('4. Cari Kontak')
    print('0. Exit')

    menu = input('Pilih Menu : ')

    if menu == '0':
        break
    elif menu == '1':
        function.show_kontak(daftar_kontak)
    elif menu == '2':
        kontak = function.add_kontak()
        daftar_kontak.append(kontak)
    elif menu == '3':
        function.delete_kontak(daftar_kontak)
    elif menu == '4':
        function.search_kontak(daftar_kontak)
    else:
            print('Menu Belum Tersedia')

print('Program Selesai')



