import os
import sys
import shlex

def parse_command(user_input):

    if user_input.strip() == "":
        return []

    try:
        tokens = shlex.split(user_input)
    except ValueError:
        print("ngawi-shell: error: unclosed quotation")
        return []

    return tokens


def main():

    while True:
        try:
            user = os.environ.get('USER', 'user')
            cwd = os.getcwd()
            prompt = f"{user}@ngawi-shell:{cwd}$ "
            
            raw_input = input(prompt)
            
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

            
            if raw_input.strip() == "":
                continue
            

            args = parse_command(raw_input)

            if not args:
                continue

            command = args[0]
            arguments = args[1:]

            # ===================== MULAI BAGIAN YASYFI =====================
            
            # [YASYFI - SELESAI] Implementasi built-in command 'cd' menggunakan os.chdir()
            if command == "cd":
                # Jika user hanya mengetik 'cd' tanpa argumen, arahkan ke direktori Home (~)
                if not arguments:
                    target_dir = os.path.expanduser("~")
                else:
                    target_dir = arguments[0]
                
                try:
                    os.chdir(target_dir)
                except FileNotFoundError:
                    print(f"ngawi-shell: cd: {target_dir}: No such file or directory")
                except NotADirectoryError:
                    print(f"ngawi-shell: cd: {target_dir}: Not a directory")
                except PermissionError:
                    print(f"ngawi-shell: cd: {target_dir}: Permission denied")
                
                # Continue agar perintah built-in tidak diteruskan ke proses eksekusi tahap 4 nanti
                continue
            
            # ===================== BATAS BAGIAN YASYFI =====================


            # ===================== MULAI BAGIAN DANIEL =====================

            if command == "pwd":
                current_directory = os.getcwd() # fungsi os.getcwd() untuk mendapatkan direktori aktif saat ini
                print(current_directory)

                # Panggil 'continue' di akhir agar program langsung kembali ke awal loop prompt
                continue
            
            # ===================== BATAS BAGIAN DANIEL =====================

            print(f"[DEBUG] Command: {command} | Args: {arguments}")

            # debug untuk melihat command dan argumen yang diparsing, bisa dihapus nanti setelah implementasi selesai


        except KeyboardInterrupt:
            print()
            continue
        except EOFError:
            print()
            sys.exit(0)

if __name__ == "__main__":
    main()