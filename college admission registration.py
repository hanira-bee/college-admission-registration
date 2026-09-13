import datetime
from os import system

hari = datetime.datetime.now()

class Mahasiswa:
    def __init__(self, nama, email, jurusan, biaya, kelas, program_studi, lulus, tidak_lulus, 
                 nilai_ujian, hasil, bayar, bank, lunas, hasil_pembayaran, terbayarkan):
        self.nama = nama
        self.email = email
        self.jurusan = jurusan
        self.biaya = biaya
        self.kelas = kelas
        self.program_studi = program_studi
        self.jadwal = {}
        self.tidak_lulus = tidak_lulus
        self.lulus = lulus
        self.nilai_ujian = nilai_ujian
        self.hasil = hasil
        self.bayar = bayar
        self.bank = bank
        self.lunas = lunas
        self.hasil_pembayaran = hasil_pembayaran
        self.terbayarkan = terbayarkan

    def memilih_jurusan_dan_kelas(self):
        print("Selamat datang, {}!".format(self.nama))
        print("Pilihan Jurusan:")
        print("1. Teknik Informatika (TI)")
        print("2. Rekayasa Perangkat Lunak (RPL)")
        print("3. Sistem Informasi (SI)")

        pilihan_jurusan = input("Pilih jurusan (1/2/3): ")
        if pilihan_jurusan == "1":
            self.jurusan = "Teknik Informatika (TI)"
            self.biaya = 5000000
        elif pilihan_jurusan == "2":
            self.jurusan = "Rekayasa Perangkat Lunak (RPL)"
            self.biaya = 7000000
        elif pilihan_jurusan == "3":
            self.jurusan = "Sistem Informasi (SI)"
            self.biaya = 5600000
        else:
            print("Pilihan jurusan tidak valid.")
            return 

        print("Pilihan Kelas:")
        print("1. Pagi")
        print("2. Malam")

        pilihan_kelas = input("Pilih kelas (1/2): ")
        if pilihan_kelas == "1":
            self.kelas = "Pagi"
            self.jadwal = {
                "Senin  ": "Algoritma",
                "Selasa ": "Entrepeneur",
                "Rabu   ": "Tidak ada Jadwal",
                "Kamis  ": "PTIK",
                "Jumat  ": "Pancasila",
                "Sabtu  ": "Tidak ada Jadwal",
                "Minggu ": "Libur",
            }
        elif pilihan_kelas == "2":
            self.kelas = "Malam"
            self.jadwal = {
                "Senin  ": "Entrepeneur",
                "Selasa ": "Tidak ada Jadwal",
                "Rabu   ": "PTIK",
                "Kamis  ": "Pancasila",
                "Jumat  ": "Tidak ada Jadwal",
                "Sabtu  ": "Algoritma",
                "Minggu ": "Libur",
            }
            self.biaya += 100000  # Tambahan biaya untuk kelas malam
        else:
            print("Pilihan kelas tidak valid.")
            return

        print("Pilihan Program Studi:")
        print("1. S1")
        print("2. D3")

        pilihan_program_studi = input("Pilih program studi (1/2): ")
        if pilihan_program_studi == "1":
            self.program_studi = "S1"
            self.biaya += 3000000
        elif pilihan_program_studi == "2":
            self.program_studi = "D3"
            self.biaya += 1500000
        else:
            print("Pilihan program studi tidak valid.")
            return
        print("\nAnda telah memilih jurusan {} dan kelas {}. Selamat belajar!".format(self.jurusan, self.kelas))
    
    def tampilkan_bukti_pembayaran(self):
        system("cls")
        print("-------------------------------------------------------")
        print("Bukti Pembayaran:".rjust(35))
        print(hari.strftime("%y-%m-%d %H:%M:%S").rjust(35))
        print("-------------------------------------------------------")
        print("Nama                 : {}".format(self.nama))
        print("Jurusan              : {}".format(self.jurusan))
        print("Kelas                : {}".format(self.kelas))
        print("Program Studi        : {}".format(self.program_studi))
        print("Biaya Kuliah         : {}".format(self.biaya))
        print("Metode Pembayaran    : {}".format(self.bayar))
        print("Nominal Pembayaran   : {}".format(self.biaya))

    def bayar_kuliah(self):
        print("Metode Pembayaran :")
        print("1. Digital")
        print("2. ATM")

        pilih_bayar = input("Pilih metode pembayaran kuliah (1/2): ")
        if pilih_bayar == "1":
            self.bayar = "Digital"
            print(f"Anda memilih metode pembayaran digital untuk mahasiswa {self.nama}.")

            while True:
                nomor_telepon = input("Masukkan nomor telepon (12 digit): ")

                if not nomor_telepon.isdigit():
                    print("Pembayaran gagal. Masukkan hanya angka.")
                elif len(nomor_telepon) != 12:
                    print("Pembayaran gagal. Nomor telepon harus memiliki 12 digit.")
                else:
                    self.hasil_pembayaran = "Pembayaran berhasil."
                    if self.hasil_pembayaran == "Pembayaran berhasil.":
                        self.lunas = "Biaya Kuliah Anda Sudah Lunas."
                    self.tampilkan_bukti_pembayaran()
                    self.kembali_ke_menu_login()
                    break

        elif pilih_bayar == "2":
            print(f"Anda memilih metode pembayaran via ATM untuk mahasiswa {self.nama}.")

            print("pilih bank:")
            print("1. BRI")
            print("2. BCA")
            print("3. BNI")

            pilih_bank = input("Silahkan pilih opsi (1/2/3): ")
            if pilih_bank == "1":
                bank = "BRI"
                print("Anda memilih pembayaran via Bank BRI.")
            elif pilih_bank == "2":
                bank = "BCA"
                print("Anda memilih pembayaran via Bank BCA.")
            elif pilih_bank == "3":
                bank = "BNI"
                print("Anda memilih pembayaran via Bank BNI.")
            self.bayar = ("Bank {}".format (bank))

            while True:
                if bank == "BRI":
                    nomor_rekening = input("Masukkan nomor rekening (15 digit): ")
                    if not nomor_rekening.isdigit():
                        print("Pembayaran gagal. Masukkan hanya angka")
                    elif len(nomor_rekening) != 15:
                        print("Pembayaran gagal. Nomor rekening harus memiliki 15 digit.")
                    else:
                        self.hasil_pembayaran = "Pembayaran berhasil."
                        if self.hasil_pembayaran == "Pembayaran berhasil.":
                            self.lunas = "Biaya Kuliah Anda Sudah Lunas."
                        self.tampilkan_bukti_pembayaran()
                        self.kembali_ke_menu_login()
                        break

                elif bank == "BCA" or bank == "BNI":
                    nomor_rekening = input("Masukkan nomor rekening (10 digit): ")
                    if not nomor_rekening.isdigit():
                        print("Pembayaran gagal. Masukkan hanya angka.")
                    elif len(nomor_rekening) != 10:
                        print("Pembayaran gagal. Nomor rekening harus memiliki 10 digit.")
                    else:
                        self.hasil_pembayaran = "Pembayaran berhasil."
                        if self.hasil_pembayaran == "Pembayaran berhasil.":
                            self.lunas = "Biaya Kuliah Anda Sudah Lunas"
                        self.tampilkan_bukti_pembayaran()
                        self.kembali_ke_menu_login()
                        break
                    
        else:
            self.lunas = "Biaya Kuliah Anda Belum Lunas."

    def info_pembayaran(self):
        system("cls")
        info()
        print("Info Pembayaran Mahasiswa.")
        print("Atas Nama: {}".format(self.nama))
        print("Silahkan bayar biaya kuliah anda sebesar : {}\n".format(self.biaya))

        if self.hasil_pembayaran == "Pembayaran berhasil.":
            self.terbayarkan = 'SUDAH TERBAYARKAN'
            print("pada {}".format(hari.strftime("%y-%m-%d %H:%M:%S")))

        else:
            self.terbayarkan = 'BELUM TERBAYARKAN'

        print("Biaya kuliah anda: [{}]".format(self.terbayarkan))
        input("Tekan enter untuk kembali ke halaman utama.")

    def tampilkan_jadwal_kuliah(self):
        print("\nJadwal Kuliah {}:".format(self.nama) )
        for hari, mata_kuliah in self.jadwal.items():
            print(f"{hari}  : {mata_kuliah}")
        self.kembali_ke_menu_login()

    def kembali_ke_menu_login(self):
        input("Tekan Enter untuk kembali ke menu login.")

    def __str__(self):
        return "\nNama: {}\nJurusan: {}\nKelas: {}\nProgram Studi: {}\nBiaya: {}\n{}".format(
            self.nama, self.jurusan, self.kelas, self.program_studi, self.biaya, self.lunas
        )
    
    def ujian_saringan(self):
        system('cls')
        biaya_pendaftaran_online()
        print("Atas nama : {} ".format(self.nama))
        print("Silahkan bayar biaya pendaftaran online")
        print("sebesar Rp.250.000,00 \n")
        print("Pembayaran dapat melalui supermarket atau bank.")
        print("*Jika Pembayaran sukses maka petunjuk ujian saringan akan dikirim ke pengguna ke alamat email yang di input.\n")
        print('1.Sudah mendapat email?')
        print('2.Belum mendapat email?')
        print('3.Kembali ke halaman utama.')

        bayar = input('Pilih opsi [1/2/3]: ')
        if bayar == '1':
            self.petunjuk_ujian_saringan()
        elif bayar == '2':
            print('\nSilahkan tunggu beberapa saat sampai email masuk atau silahkan melapor ke bagian administrasi kampus.')
            input('Silahkan tekan [ENTER]')
            self.ujian_saringan()
        elif bayar == '3':
            program_penerimaan_mahasiswa.tampilkan_tampilan_awal()
        else:
            self.ujian_saringan()
 
    def petunjuk_ujian_saringan(self):
        system('cls')
        print('=====================================================')
        print('|             PETUNJUK UJIAN SARINGAN               |')
        print('=====================================================')
        print('Ujian saringan dikerjakan di aplikasi atau website kampus: ')
        print('1. Login ke sistem menggunakan alamat email dan nomor handphone')
        print('2. Klik mulai ujian saringan')
        print('3. Kerjakan ujian saringan yang terdiri dari 3 materi :')
        print('   a. Pendidikan Pancasila')
        print('   b. Pengetahuan Umum')
        print('   c. Bahasa Inggris')
        print('4. Jika Lulus, silahkan lanjutkan prosedur pendaftaran selanjutnya.')
        print('5. Jika Tidak Lulus maka tidak bisa melanjutkan prosedur pendaftaran. \n')
        print('Terima kasih! \n')
        print('*Jika telah melakukan ujian saringan, nilai akan muncul otomatis untuk menentukan lulus atau tidaknya ujian.')
      
        nilai_ujian = int(input('Masukkan nilai ujian saringan: '))
        
        if nilai_ujian < 70:
            self.hasil = 'Tidak Lulus'
            print('\nAnda dinyatakan {} Ujian Saringan,'.format(self.hasil))
            print('Jangan menyerah, tetap semangat!')
        elif nilai_ujian >= 70:
            self.hasil = 'Lulus'
            print('\nAnda dinyatakan {} Ujian Saringan,'.format(self.hasil))
            print('Silahkan kembali ke halaman utama untuk login akun mahasiswa anda!')
        else:
            print('Nilai yang anda masukkan salah!')
            self.petunjuk_ujian_saringan()

        input('Tekan enter untuk kembali ke halaman utama.')

class PenerimaanMahasiswaBaru:
    def __init__(self):
        self.calon_mahasiswa = []

    def tampilkan_tampilan_awal(self):
        system('cls')
        judul()
        print("Selamat datang di Program Penerimaan Mahasiswa Baru!")
        print('-----------------------------------------------------')
        print("| 1. Registrasi Mahasiswa Baru                      |")
        print("| 2. Login                                          |")
        print("| 3. Tampilkan Data Mahasiswa                       |")
        print("| 4. Lihat Jadwal Kuliah                            |")
        print("| 5. Keluar                                         |")
        print('=====================================================')

    def registrasi_mahasiswa_baru(self):
        system('cls')
        judul()
        registrasi()
        nama = input("Masukkan nama: ")
        email = input("Masukkan alamat email aktif: ")

        mahasiswa = Mahasiswa(nama, email, "", 0, "", "", "", "", "", 0, "", 0, "", "", "")
        mahasiswa.memilih_jurusan_dan_kelas()

        self.calon_mahasiswa.append(mahasiswa)
        print("Registrasi berhasil. Selamat bergabung, {}!".format(nama))
        input('Tekan enter untuk melanjutkan proses pendaftaran mahasiswa baru.')
        biaya_pendaftaran_online()
        mahasiswa.ujian_saringan()

    def login(self):
        system('cls')
        judul()
        login()
        email = input("Masukkan alamat email: ")

        for mahasiswa in self.calon_mahasiswa:
            if mahasiswa.hasil == 'Lulus':
                if mahasiswa.email == email:
                    print("Login berhasil.")
                    while True:
                        self.tampilkan_menu_login()
                        opsi_login = input("Pilih opsi (1/2/3/4/5): ")

                        if opsi_login == "1":
                            mahasiswa.tampilkan_jadwal_kuliah()
                        elif opsi_login == "2":
                            mahasiswa.info_pembayaran()
                        elif opsi_login == "3":
                            mahasiswa.bayar_kuliah()
                        elif opsi_login == "4":
                            print(mahasiswa)
                            input("Tekan enter untuk kembali ke menu login.")
                        elif opsi_login == "5":
                            break
                        else:
                            print("Pilihan tidak valid. Silakan pilih opsi yang benar.")
                    return
                
        input("Mahasiswa tidak terdaftar.")

    def tampilkan_daftar_mahasiswa(self):
        system('cls')
        daftar_mahasiswa()
        if not self.calon_mahasiswa:
            print("Belum ada mahasiswa yang terdaftar.")
        else:
            print("Daftar Mahasiswa yang Terdaftar:")
            for index, mahasiswa in enumerate(self.calon_mahasiswa, start=1):
                print(f"{index}. {mahasiswa.nama} - {mahasiswa.jurusan}, {mahasiswa.kelas} [{mahasiswa.hasil}]")

        input("Tekan enter untuk kembali ke halaman pertama.")

    def tampilkan_menu_login(self):
        system('cls')
        judul()
        login()
        print("Menu Login:")
        print("1. Tampilkan Jadwal Kuliah")
        print("2. Info Pembayaran")
        print("3. Bayar Kuliah")
        print("4. Tampilkan Data Mahasiswa")
        print("5. Kembali ke Menu Utama")

    def jalankan_program(self):
        while True:
            self.tampilkan_tampilan_awal()
            pilihan = input("Pilih opsi (1/2/3/4/5): ")

            if pilihan == "1":
                self.registrasi_mahasiswa_baru()
            elif pilihan == "2":
                self.login()
            elif pilihan == "3":
                self.tampilkan_daftar_mahasiswa()
            elif pilihan == "4":
                for mahasiswa in self.calon_mahasiswa:
                    if mahasiswa.hasil == 'Lulus':
                        mahasiswa.tampilkan_jadwal_kuliah()
            elif pilihan == "5":
                input("Terima kasih telah menggunakan program. Sampai jumpa!")
                break
            else:
                input("Pilihan tidak valid. Silakan pilih opsi yang benar.")

def judul():
    print('=====================================================')
    print('|             PENDAFTARAN MAHASISWA BARU            |')
    print('=====================================================')

def registrasi():
    print('|                     REGISTRASI                    |')
    print('=====================================================')

def login():
    print('|                       LOGIN                       |')
    print('=====================================================')

def daftar_mahasiswa():
    print('=====================================================')
    print('|                   DAFTAR MAHASISWA                |')
    print('=====================================================')

def biaya_pendaftaran_online():
    print('=====================================================')
    print('|                  BIAYA PENDAFTARAN                |')
    print('=====================================================')

def info():
    print('=====================================================')
    print('|                    INFO PEMBAYARAN                |')
    print('=====================================================')


if __name__ == "__main__":
    program_penerimaan_mahasiswa = PenerimaanMahasiswaBaru()
    program_penerimaan_mahasiswa.jalankan_program()

