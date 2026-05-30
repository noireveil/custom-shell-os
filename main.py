import os
import sys

def parse_command(user_input):
    """
    Tahap 2: Parsing Perintah (Command Tokenization): Target: Memisahkan perintah
    utama dan argumen.
    Input string yang dimasukkan pengguna harus dipecah (tokenize) berdasarkan karakter
    spasi.
    Contoh: Jika pengguna mengetik cp file1.txt file2.txt, program harus
    memecahnya menjadi array: args[0] = "cp", args[1] = "file1.txt", args[2] =
    "file2.txt". Di bahasa C, gunakan fungsi strtok().
    
    [JADWAL: MINGGU 2 | OLEH: FARIS & HAMIM]
    """
    # TODO [FARIS & HAMIM]: Tulis logika pemecahan string di sini
    
    return []


def main():
    """
    Tahap 1: Membangun REPL (Read-Evaluate-Print Loop): Target: CLI bisa menerima
    input terus-menerus.
    Buat struktur utama program yang berjalan dalam infinite loop (perulangan tanpa henti).
    Program harus menampilkan prompt kustom (misalnya user@myshell:~$), membaca
    input string dari pengguna menggunakan fungsi seperti fgets() di C atau input() di
    Python, dan berhenti hanya jika pengguna mengetik perintah exit.
    
    [JADWAL: MINGGU 1 | OLEH: YASYFI & DANIEL]
    """
    
    # [BAGIAN YASYFI - SELESAI] Setup loop utama dan prompt kustom
    while True:
        try:
            user = os.environ.get('USER', 'user')
            cwd = os.getcwd()
            prompt = f"{user}@ngawi-shell:{cwd}$ "
            
            raw_input = input(prompt)
            
            # --- MULAI BAGIAN DANIEL ---
            
            # TODO [DANIEL]: Tangani poin dari Tahap 1: 
            # - Berhenti hanya jika pengguna mengetik perintah exit.
            
            # TODO [DANIEL]: Tangani poin pengujian agar program aman:
            # - Pastikan program tidak langsung menutup (force close) jika pengguna 
            #   menekan tombol Enter tanpa mengetik apa pun.
            
            # --- BATAS BAGIAN DANIEL ---


            # Transisi ke Tahap 2 (Faris & Hamim)
            args = parse_command(raw_input)
            if not args:
                continue

            # Tahap 3 dan seterusnya akan dikerjakan pada minggu berikutnya
            # Untuk sekarang print aja hasil dari Tahap 2 untuk ngetes
            print(f"[DEBUG] Args yang akan dieksekusi nanti: {args}")

        except KeyboardInterrupt:
            print()
            continue
        except EOFError:
            print()
            sys.exit(0)

if __name__ == "__main__":
    main()