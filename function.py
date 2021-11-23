def show_kontak(daftar_kontak):
    for kontak in daftar_kontak:
        print('====================')
        print(f"Nama : {kontak['nama']}")
        print(f"Email : {kontak['email']}")
        print(f"Telepon : {kontak['telepon']}")

def add_kontak():
    nama = input('Nama : ')
    email = input('Email : ')
    telepon = input('Telepon : ')
    kontak = {
        'nama' : nama,
        'email' : email,
        'telepon' : telepon
    }
    return kontak

def delete_kontak(daftar_kontak):
    nama = input('Nama Kontak Yang Akan Dihapus : ')

    index = -1

    for i in range(0, len(daftar_kontak)):
        kontak = daftar_kontak[i]
        if nama == kontak['nama']:
            index = i
            break

    if index == -1:
        print('Kontak Tidak Ditemukan')
    else:
        del daftar_kontak[index]
        print('Kontak Berhasil Dhapus')

def search_kontak(daftar_kontak):
    nama_yg_dicari = input('Nama Yang Dicari : ')

    for kontak in daftar_kontak:
        nama = kontak['nama']
        if nama.lower().find(nama_yg_dicari.lower()) != -1:
            print('====================')
            print(f"Nama : {kontak['nama']}")
            print(f"Email : {kontak['email']}")
            print(f"Telepon : {kontak['telepon']}")
