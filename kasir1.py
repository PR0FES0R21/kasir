# code by sayoga pratama
import os
import sys
import time
from datetime import datetime
from prettytable import PrettyTable
from colorama import Fore, Back, Style
from tabulate import tabulate


x = True


menu = [
    {"id": 1, "jenis_menu": "minuman", "nama": "kopi", "harga": 10000},
    {"id": 2, "jenis_menu": "makanan", "nama": "ayam geprek", "harga": 15000},
    { "id": 3, "jenis_menu": "minuman", "nama": "es teh anget", "harga": 5000},
    {"id": 4, "jenis_menu": "makanan", "nama": "pecel lele", "harga": 10000},
    {"id": 5, "jenis_menu": "makanan", "nama": "ayam goreng", "harga": 12000},
    {"id": 6, "jenis_menu": "minuman", "nama": "jus jeruk", "harga": 5000}
    
]

members = [
    {"id": 79111952, "no_handpone": "085814015797", "nama": "sayoga", "tanggal_gabung": "20-11-2022"},
    {"id": 79111953, "no_handpone": "083178865134", "nama": "sandika", "tanggal_gabung": "3-8-2020"},
    {"id": 79111954, "no_handpone": "083178865134", "nama": "samsudin", "tanggal_gabung": "12-5-22020"},
    {"id": 79111955, "no_handpone": "083178865134", "nama": "azka", "tanggal_gabung": "26-3-2019"}
]


temp_pesanan = []


figlet_welcome = f"""\033[92m
___________________________________________________\033[95m
 _    _  _____  _      _____   _____ ___  ___ _____ 
| |  | ||  ___|| |    /  __ \ |  _  ||  \/  ||  ___|
| |  | || |__  | |    | /  \/ | | | || .  . || |__  
| |/\| ||  __| | |    | |     | | | || |\/| ||  __| 
\  /\  /| |___ | |___ | \__/\ \ \_/ /| |  | || |__ 
 \/  \/ \____/ \_____/ \____/  \___/ \_|  |_/\____/
\033[92m---------------------------------------------------
|{Back.WHITE+Fore.GREEN+Style.BRIGHT}-----------\033[94mAuthor: \033[91mSayoga \033[92m| \033[91mProfesor21\033[92m-----------{Style.RESET_ALL}\033[92m|
\033[92m==================================================="""


figlet_kasir = f""""\033[92m
============================================{Fore.MAGENTA}
  _  __              ____     ____   _____  
 | |/ /     /\      / ___|   |   _| |  __ \ 
 | ' /     /  \    | (___     | |   | |__) |
 |  <     / /\ \    \___ \    | |   |  _  / 
 | . \   / ____ \   ___)  |  _| |_  | | \ \ 
 |_|\_\ /_/    \_\ |_____/  |_____| |_|  \_
{Fore.GREEN}============================================"""

def mengetik(z):
    for i in z + "\n":
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.0001)


figlet_register = f"""\033[95m
  ____      _     _____   _____     _      ____  
 |  _ \    / \   |  ___| |_   _|   / \    |  _ \ 
 | | | |  / _ \  | |_      | |    / _ \   | |_) |
 | |_| | / ___ \ |  _|     | |   / ___ \  |  _ < 
 |____/ /_/   \_\|_|       |_|  /_/   \_\ |_| \_\ 
\033[92m=================================================="""
                                                    


struk = f"""
                            ______________________
 CV.PROFESORDS              | ___ ____ ____ ____ |
 JL.MERPATI RAYA            | |_] |__/ |  | |__  |
 SAWAH BARU CIP.15413       | |   |  \ |__| |    |
 NPWP : 902 9832-62         ----------------------"""


while True:
# Fungsi untuk menampilkan informasi member dalam bentuk tabel
    def lihat_member(id=None):
        table = PrettyTable()
        table.field_names = ['\033[91m\033[1mID\033[0m\033[95m', '\033[1m\033[91mNAMA MEMBER\033[0m\033[95m', '\033[1m\033[91mTANGGAL GABUNG\033[0m\033[95m']
        if id:
            # Jika ID member diberikan, tampilkan informasi member tersebut
            for member in members:
                if member['id'] == id:
                    table.add_row([f"\033[91m{member['id']}\044[95m", f"\033[94m{member['nama']}\033[95m", f"\033[94m{member['tanggal_gabung']}\033[95m"])
        else:
            # Jika ID member tidak diberikan, tampilkan semua member
            for member in members:
                table.add_row([f"\033[91m{member['id']}\033[95m", f"\033[94m{member['nama']}\033[95m", f"\033[94m{member['tanggal_gabung']}\033[95m"])
            print(table.get_string(title='\033[92m\033[1mDAFTAR MEMBER\033[0m\033[95m'))
            ask = input("\033[93mTekan ENTER")
            home()

    # function cek data
    def cek_data(id = None, hp = None):
        result = {'status': 1}
        if hp:
            for cek in members:
                if cek['no_handpone'] == hp:
                    result = {'status': 0, "error": f"\033[91mid sudah terdaftar sebagai {cek['nama']}", "nama": {cek['nama']}}
        if id:
            for cek in members:
                if cek['id'] == id:
                    result = {'status': 0, "error": f"\033[91mid sudah terdaftar sebagai {cek['nama']}", "nama": {cek['nama']}}
        return result

    # function tambah member
    def tambah_member():
        global x
        # input data
        os.system('clear') if x == True else ''
        print(figlet_register) if x == True else ""
        mengetik('\033[94mSILAHKAN MASUKAN NOMOR HANDPONE DAN NAMA DI BAWAH\n') if x == True else ""
        while True:
            try:
                hp = input(f"\033[93mINPUT NOMOR HP: ")
                nama = input(f"\033[93mINPUT NAMA: ")
                # cek apakah data sudah terdaftar
                # jika belum
                cek = cek_data(hp)
                if cek['status'] == 1:
                    now = datetime.now()
                    members.append({'id': members[-1]['id'] + 1, "no_handpone": hp, 'nama': nama, 'tanggal_gabung': now.strftime("%d %m %Y")})
                    print("\033[92mdata berasil ditambahkan\033[95m")
                    x = True
                    lihat_member()
                # jika sudah
                else:
                    print(cek['error'],'\033[0;37m')
                    time.sleep(2)
                    x = False
                    tambah_member()
            except ValueError:
                print('masukan id(angka) dan nama(huruf)')
                time.sleep(2)

    # function daftar_menu
    def daftar_menu(jenis):
        table = PrettyTable(['\033[92m\033[1mCODE\033[0m\033[95m',f'\033[92m\033[1mNAMA {jenis.upper()}\033[0m\033[95m', '\033[92m\033[1mHARGA BARANG\033[0m\033[95m'])
        for dm in menu:
            if dm['jenis_menu'] == jenis:
                code = f"\033[91m{dm['id']}\033[95m"
                nama = f"\033[94m{dm['nama']}\033[95m"
                harga = f"\033[94m{dm['harga']}\033[95m"
                table.add_row([code, nama, harga ])
        print('\033[95m')
        print(table)


    def get_menu(code):
        no = 1
        for get in menu:
            if get['code'] == code:
                print(f"{no}. nama {get['nama']} harga {get['harga']}")
        

    # function konfirmasi
    def konfirmasi():
            # declarator statement
            nama = []
            jumlah = []
            # total baris(35) - hasil len(nama[0]) + len(str(jumlah[0])) + 7
            # space = len(nama[0]) + len(jumlah)
            for confirm in temp_pesanan:
                for mn in menu:

                    if mn['id'] == confirm['code']:
                        nama.append(mn['nama'])
                        jumlah.append(confirm['jumlah'])

                        # print(' ' * (35 - space), 'anjay')
                        result = (len(nama[0]) + len(jumlah)) + 17
                        print(" ",nama[0],' ' * (35 - result), 'jumlah :',' ' * 3, jumlah[0])
                        nama.clear()
                        jumlah.clear()


    # function pembayran
    def pembayaran():
        no = 1
        total_harga = 0
        total_harga_final = 0
        member_status = ['status']
        jumlah_bayar = 0
        kembalian = 0
        harga_produk = 0

        # hitung total harga
        for conf in temp_pesanan:
            for mn in menu:
                if mn['id'] == conf['code']:
                    total_harga += (mn['harga'] * conf['jumlah'])


        # cek apakah konsumen terdaftar sebagai member            
        ask3 = input("\033[93mapakah konsumen terdaftar sebagai member? y/t: ")
        if ask3 == 'y' or ask3 == 'Y':

            a = 'y'
            while a != 'n':
                try:
                    id = int(input("\033[93mINPUT ID MEMBER: "))
                    cek = cek_data(id)
                    member_status = cek_data(id)['status']
                    if cek['status'] == 0:
                        nama = str(cek['nama'])
                        print(f"\033[0;37m\033[1mmember ditemukan a/n", (nama[2:len(nama) - 2])+'\033[0m')
                    # jika iya, naka diskon 10%
                        total_harga_final = total_harga - (total_harga*0.1)
                        print(f"\033[0;37m\033[1mharga awal \033[91m{total_harga} \033[0;37mdiskon 10% menjadi \033[92m{int(total_harga_final)}\033[0m")
                        while True:
                            jumlah_bayar = int(input("\033[93mmasukan nominal uang: "))
                            if jumlah_bayar < total_harga_final:
                                print("\033[91mMAAF UANG ANDA TIDAK CUKUP")
                                time.sleep(1)
                            else:
                                kembalian = jumlah_bayar - total_harga_final
                                a = 'n'
                                break

                    # jika tidak, bayar harga normal
                    else:
                        print("member tidak ditemukan")
                        time.sleep(1)
                        ask = input("COBA LAGI? y/t: ")
                        if ask == 't':
                            member_status = False
                            print("pembyaran normal :",total_harga)
                            jumlah_bayar = int(input("\033[93mmasukan nominal uang: "))
                            kembalian = int(jumlah_bayar) - int(total_harga)
                            break
                except ValueError:
                    print('masukan angka (tidak boleh huruf)')

        else:
            total_harga_final = total_harga
            print("\033[0;37mpembayaran normal", total_harga_final)
            while True:
                jumlah_bayar = int(input("\033[93mmasukan nominal uang: "))
                if jumlah_bayar < total_harga_final:
                    print("\033[91mmaff uang anda tidak cukup")
                    time.sleep(1)
                else:
                    kembalian = jumlah_bayar - total_harga_final
                    break
        cetak_struk(member_status, total_harga, total_harga_final, jumlah_bayar, kembalian)


    # function cetak struk
    def cetak_struk(member_status, total_harga, total_harga_final, jumlah_bayar, kembalian):
        global menu
        result = []
        x = total_harga * (5/100)
        dpp = total_harga - x
        ppn = dpp * (10/100)
        total_harga = "{:,}".format(int(total_harga)).replace('.',',')
        total_harga_final = "{:,}".format(int(total_harga_final)).replace(',','.')
        jumlah_bayar = "{:,}".format(int(jumlah_bayar)).replace(',','.')
        kembalian = "{:,}".format(int(kembalian)).replace(',','.')

        now = datetime.now()
        print('\n'+Back.WHITE+Fore.BLACK+Style.BRIGHT+struk+'\n')
        print(f"        jl.merpati raya sawah baru ciputat,")
        print("            kota tangerang selatan 15413")
        print("---------------------------------------------------")
        mengetik(now.strftime("%d %b %Y, %X   2.1.27  22797/SAYOGA  TR/01"))
        print("---------------------------------------------------\n")
        for confirm in temp_pesanan:
            for mn in menu:

                if mn['id'] == confirm['code']:
                    nama = (mn['nama'])
                    jumlah = (confirm['jumlah'])

                    # print(' ' * (35 - space), 'anjay')
                    result = (len(nama) + len(str(jumlah))) + 10
                    space = 8 - len(str(mn['harga']))
                    result1 = mn['harga'] * confirm['jumlah']
                    space3 = 11 - (len(str(result1)))
                    print(' '+nama,' ' * (30 - result), jumlah,' '*space, mn['harga'],' ' * space3, mn['harga'] * confirm['jumlah'])
                    nama = ''
                    jumlah = 0
                    

                    # 12
        space_total_harga = 11 - len(total_harga)
        space_kembali = 11 - len(kembalian)
        space_diskon = 11 - len(total_harga_final)
        space_tunai = 11 - len(jumlah_bayar)
        print(' ' * (17),'    ________________________')
        print(' ' * (17),"    HARGA JUAL :"+' '* space_total_harga,total_harga)
        print(' ' * (17),'    ------------------------')
        print(' ' * (17),"        DISKON :"+' '* space_diskon,total_harga_final) if member_status == 0 else ''
        print(' ' * (17),"         TUNAI :"+' '* space_tunai,jumlah_bayar)
        print(' ' * (17),"       KEMBALI :"+' '* space_kembali,kembalian)
        print(f" PPN    : DPP= {dpp}  PPN= {ppn}")
        mengetik("       TERIMAKASIH SELAMAT BERBELANJA KEMBALI")
        print('==================LAYANAN KONSUMEN=================')
        print('      CALL 18023  SMS/WA : +62 858 1401 5797')
        print('        EMAIL : sayogapratama565@gmail.com        .'+Style.RESET_ALL)
        temp_pesanan.clear()
        x = input("\033[93mtransaksi lagi? y/t: ")
        if x != 'y':
            home()


    # function kasir
    def kasir():
        os.system('clear')
        print(figlet_kasir)
        print("\033[94m1. pesan makanan / minuman")
        print("2. lihat pesanan")
        print("3. bayar")
        print("4. kembali kemenu awal")
        while True:
            try:
                option = int(input("\033[93mSILAHKAN PILIH: \033[95m"))
                if option == 1:
                    ask = 'y'
                    z = False
                    while ask == 'y':    
                        ask1 = 'y'
                        while ask1 == 'y':
                            daftar_menu('makanan')
                            daftar_menu('minuman')
                            try:
                                print("\n\033[92m+===================================+") if z == True else ''
                                print(f"            \033[0;1m\033[1mPESANAN KAMU\033[92m") if z == True else ''
                                print("+===================================+\033[0;1m") if z == True else ''
                                konfirmasi() if z == True else ''
                                print('')

                                menu_pilihan = int(input("\033[93mPILIH SESUAI CODE => "))
                                jumlah = int(input("mau berapa banyak? > "))
                                temp_pesanan.append({"code": menu_pilihan, "jumlah": jumlah})
                                asks = input('\033[92mADA LAGI YANG MAU DI BELI? y/t > \033[93m')
                                if asks == 'y':
                                    z = True
                                    ask1 = 'y'
                                else:
                                    # 35 - len(jumlah keseluruhan) hsilnya * ''
                                    print("\033[92m+===================================+")
                                    print(f"            \033[0;1m\033[1mPESANAN KAMU\033[92m")
                                    print("+===================================+\033[0;1m")
                                    konfirmasi()
                                    ask2 = input("\033[93m\n\033[1mtekan\033[0m ENTER \033[93m\033[1muntuk melanjutkan\33[0m ")
                                    if ask2 == 'y':
                                        pembayaran()
                                    else:
                                        pembayaran()
                            except ValueError:
                                print('masukan angka tidak boleh huruf')
                elif option == 2:
                    if konfirmasi() == None:
                        print("belum ada pesanan")
                        time.sleep(2)
                        kasir()
                    else:
                        print("1. bayar")
                        print("ENTER KELUAR >")
                        ask = input("pilih opsi > ")
                        if ask == '1':
                            pembayaran()
                        else:
                            home()
                elif option == 3:
                    if temp_pesanan:
                        konfirmasi()
                        pembayaran()
                    else:
                        print("tidak ada pesanan")
                        time.sleep(1)
                        kasir()
                        
                elif option == 4:
                    print("kembali kemenu awal")
                    temp_pesanan.clear()
                    home()
                else:
                    print("error, pilihan tidak tersedia")
                    time.sleep(2)
                    kasir()
            except ValueError:
                print('masukan angka yang benar/sesuai')

    # function lihat menu
    def lihat_menu(jenis):
        i = 0
        no = 1
        if jenis == "minuman":
            print("DAFTAR MINUMAN")
            while i < len(menu):
                if menu[i]["jenis_menu"] == "minuman":
                    print(no, ".", menu[i]["nama"], "harga", menu[i]["harga"])
                    no += 1
                i += 1
        if jenis == "makanan":
            print("DAFTAR MAKANAN")
            while i < len(menu):
                if menu[i]["jenis_menu"] == "makanan":
                    print((f"{no}. {menu[i]['nama']} harga {menu[i]['harga']}"))
                    no += 1
                i += 1
            

    def home():
        y = True
        os.system('clear') if y == True else ''
        print('')
        print(figlet_welcome)
        print("\033[94m1. Lihat member                      4. Lihat menu")
        print("2. Tambah member baru                \033[91m5. Keluar")
        print("\033[94m3. Kasir")

        while True:
            try:
                option = int(input("\033[93mSILAHKAN PILIH => "))
                if option == 1:
                    print('\033[95m')
                    lihat_member()
                elif option == 2:
                    tambah_member()
                elif option == 3:
                    kasir()
                elif option == 4:
                    daftar_menu("makanan")
                    daftar_menu("minuman")
                    input("\033[93mENTER untuk kembali ke menu")
                    home()
                elif option == 5:
                    print("PROGRAM DIHENTIKAN!")
                    sys.exit()
                else:
                    print('masukan perintah yang sesuai')
                    time.sleep(2)
            except ValueError:
                y == True
                print("masukan angka yang benar/sesuai")
                time.sleep(2)

    
    home()



