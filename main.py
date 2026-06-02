import os
import sys
import shlex

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
    # ===================== MULAI BAGIAN FARIS =====================

    # TODO [FARIS 1/3]: Cek apakah user_input kosong atau hanya whitespace (DONE)
    if user_input.strip() == "":
        return []

    # TODO [FARIS 2/3]: Pecah user_input menggunakan shlex.split() (DONE)
    try:
        tokens = shlex.split(user_input)
    except ValueError:
        print("ngawi-shell: error: unclosed quotation")
        return []

    # TODO [FARIS 3/3]: Return hasil tokenisasi (DONE)
    return tokens

    # ===================== BATAS BAGIAN FARIS =====================

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
            if raw_input.strip() == "exit":
                print(r"""   _____                 _ _                _ 
  / ____|               | | |              | |
 | |  __  ___   ___   __| | |__  _   _  ___| |
 | | |_ |/ _ \ / _ \ / _` | '_ \| | | |/ _ \ |
 | |__| | (_) | (_) | (_| | |_) | |_| |  __/_|
  \_____|\___/ \___/ \__,_|_.__/ \__, |\___(_)
                                  __/ |       
                                 |___/        """)
                print("\n")
                break

            
            # TODO [DANIEL]: Tangani poin pengujian agar program aman:
            # - Pastikan program tidak langsung menutup (force close) jika pengguna 
            #   menekan tombol Enter tanpa mengetik apa pun.
            if raw_input.strip() == "":
                continue
            
            # --- BATAS BAGIAN DANIEL ---


            # Transisi ke Tahap 2 (Faris & Hamim)
            args = parse_command(raw_input)

            # ===================== MULAI BAGIAN HAMIM =====================

            # TODO [HAMIM 1/3]: Validasi hasil parse_command() (DONE)
            # Kalau return [] jangan dieksekusi, langsung continue ke prompt berikutnya
            if not args:
                continue

            # TODO [HAMIM 2/3]: Pisahkan command utama dan argumennya (DONE)
            command = args[0]
            arguments = args[1:]

            # TODO [HAMIM 3/3]: Print DEBUG untuk verifikasi hasil parsing sudah benar (DONE)
            print(f"[DEBUG] Command: {command} | Args: {arguments}")

            # ===================== BATAS BAGIAN HAMIM =====================

        except KeyboardInterrupt:
            print()
            continue
        except EOFError:
            print()
            sys.exit(0)

if __name__ == "__main__":
    main()