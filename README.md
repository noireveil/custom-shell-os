# Custom Shell - Proyek Sistem Operasi

Proyek ini adalah implementasi antarmuka baris perintah (CLI) berbasis POSIX yang ditulis menggunakan Python. Proyek ini dibangun untuk mensimulasikan siklus hidup proses Sistem Operasi dari awal, mencakup Read-Evaluate-Print Loop (REPL), tokenisasi perintah, manajemen proses (forking & eksekusi eksternal), hingga manipulasi file descriptor untuk Inter-Process Communication (IPC).

## Roadmap Implementasi

Pengembangan sistem ini dibagi menjadi 6 tahap yang dikerjakan secara rolling dan paralel:
- Tahap 1: Membangun fondasi REPL (Infinite Loop & Custom Prompt).
- Tahap 2: Mesin Parser (Tokenisasi perintah dan argumen).
- Tahap 3: Implementasi Built-in Commands (cd, pwd).
- Tahap 4: Manajemen Child/Parent Process (os.fork(), os.execvp()).
- Tahap 5: Fitur Advanced Manipulasi I/O (Piping & Redirection).
- Tahap 6: Pengujian Beban dan Toleransi Kesalahan (Error Handling).

---

## Persyaratan Sistem & Setup Environment

Program ini secara intensif memanggil antarmuka sistem (system calls) tingkat rendah spesifik keluarga Unix/Linux, seperti os.fork(), os.execvp(), os.waitpid(), dan manipulasi kernel buffer. 

Oleh karena itu, tata cara penyiapan lingkungan kerja akan sangat bergantung pada Sistem Operasi yang Anda gunakan:

### Pengguna Linux & macOS
Karena macOS berbasis Unix (POSIX-compliant) dan Linux adalah habitat asli dari system calls ini, Anda tidak memerlukan konfigurasi tambahan. 
- Pastikan Python 3.x sudah terinstal.
- Anda bisa langsung mengeksekusi program di terminal bawaan (native terminal).

### Pengguna Windows (WAJIB DIBACA)
JANGAN menjalankan skrip ini menggunakan Command Prompt (CMD) atau PowerShell bawaan Windows. Windows memiliki arsitektur kernel yang berbeda dan tidak memiliki fungsi fork(). Menjalankan program ini di environment native Windows akan mengakibatkan CRASH (AttributeError: module 'os' has no attribute 'fork').

Anda WAJIB menggunakan WSL (Windows Subsystem for Linux). Berikut adalah cara instalasinya:
1. Buka aplikasi PowerShell dan jalankan sebagai Administrator (Run as Administrator).
2. Ketik perintah berikut dan tekan Enter:
   `wsl --install`
3. Tunggu hingga proses unduhan selesai, lalu Restart komputer/laptop Anda.
4. Setelah restart, sistem akan otomatis membuka terminal Linux (biasanya Ubuntu). Silakan buat username dan password Linux Anda.
5. Gunakan terminal Ubuntu (WSL) tersebut untuk melakukan clone repositori ini dan mengeksekusi program.

---

## Cara Menjalankan Program

1. Clone repositori ini ke dalam mesin lokal Anda:
   ```bash
   git clone https://github.com/noireveil/custom-shell-os.git
   ```
2. Masuk ke dalam direktori proyek:
   ```bash
   cd custom-shell-os
   ```
3. Eksekusi program utama menggunakan Python 3:
   ```bash
   python3 main.py
   ```
4. Untuk keluar dari Custom Shell, ketik `exit` lalu tekan Enter, atau gunakan kombinasi tombol Ctrl+D (EOF).

---

## SOP Kontribusi Tim (Workflow)

Untuk menjaga arsitektur kode dan mencegah konflik selama pengerjaan, seluruh anggota tim wajib mengikuti protokol berikut:
1. Perhatikan Tag TODO: Kerjakan kode HANYA di bawah blok `# TODO` yang sudah ditugaskan atas nama Anda pada minggu tersebut.
2. Jangan Mengubah Kode Tahap Lain: Dilarang keras memodifikasi transisi antar-tahap (seperti variabel `raw_input` atau `args`) tanpa koordinasi dan kesepakatan di grup.
3. Gunakan Conventional Commits: Wajib menggunakan prefix standar saat melakukan push untuk menjaga kerapian riwayat Git. Gunakan format bahasa Inggris berikut:
   - `feat:` untuk penambahan fitur baru (contoh: `feat: implement built-in cd command`)
   - `fix:` untuk perbaikan bug (contoh: `fix: handle force close on empty input`)
   - `docs:` untuk perubahan pada README (contoh: `docs: update wsl installation guide`)
   - `refactor:` untuk merapikan kode tanpa mengubah fungsi (contoh: `refactor: clean up loop flow`)