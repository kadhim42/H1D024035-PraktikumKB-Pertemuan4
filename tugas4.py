import tkinter as tk
from tkinter import messagebox

#kerusakan dan gejala
database_kerusakan = {
    "RAM Rusak": {"blue_screen", "restart_sendiri", "tidak_booting"},
    "Hardisk Rusak": {"loading_lama", "file_hilang", "suara_aneh"},
    "Overheat (Prosesor)": {"panas", "mati_sendiri", "kipas_kencang"},
    "VGA Bermasalah": {"layar_blank", "artefak", "no_signal"},
    "Power Supply (PSU) Lemah": {"tidak_nyala", "mati_total", "restart_sendiri"}
}

#solusi
solusi = {
    "RAM Rusak": "Coba bersihkan pin RAM dengan penghapus atau ganti RAM.",
    "Hardisk Rusak": "Lakukan pengecekan dengan CHKDSK atau ganti hardisk.",
    "Overheat (Prosesor)": "Bersihkan kipas dan ganti thermal paste.",
    "VGA Bermasalah": "Periksa kabel VGA atau coba ganti GPU.",
    "Power Supply (PSU) Lemah": "Ganti power supply dengan daya yang sesuai."
}

#daftar pertanyaan
semua_gejala = [
    ("blue_screen", "Apakah muncul blue screen?"),
    ("restart_sendiri", "Apakah komputer sering restart sendiri?"),
    ("tidak_booting", "Apakah komputer tidak bisa booting?"),
    ("loading_lama", "Apakah loading sangat lama?"),
    ("file_hilang", "Apakah file sering hilang/corrupt?"),
    ("suara_aneh", "Apakah terdengar suara aneh dari hardisk?"),
    ("panas", "Apakah komputer cepat panas?"),
    ("mati_sendiri", "Apakah komputer mati sendiri?"),
    ("kipas_kencang", "Apakah kipas berbunyi sangat kencang?"),
    ("layar_blank", "Apakah layar blank?"),
    ("artefak", "Apakah muncul garis/artefak di layar?"),
    ("no_signal", "Apakah muncul 'no signal'?"),
    ("tidak_nyala", "Apakah komputer tidak menyala sama sekali?"),
    ("mati_total", "Apakah komputer mati total tiba-tiba?")
]

#class aplikasi pakar
class AplikasiPakar:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistem Pakar Diagnosa Komputer")
        self.root.geometry("450x300")

        self.gejala_terpilih = []
        self.index_pertanyaan = 0

        self.label_tanya = tk.Label(root, text="Selamat datang di Sistem Pakar", font=("Arial", 12))
        self.label_tanya.pack(pady=20)

        self.button_mulai = tk.Button(root, text="Mulai Diagnosa", command=self.mulai_tanya)
        self.button_mulai.pack(pady=10)

        self.frame_jawaban = tk.Frame(root)

        self.button_ya = tk.Button(self.frame_jawaban, text="Ya", width=10,
                                   command=lambda: self.jawab("y"))
        self.button_tidak = tk.Button(self.frame_jawaban, text="Tidak", width=10,
                                      command=lambda: self.jawab("t"))

        self.button_ya.pack(side=tk.LEFT, padx=10)
        self.button_tidak.pack(side=tk.LEFT, padx=10)

    #mulai diagnosa
    def mulai_tanya(self):
        self.gejala_terpilih = []
        self.index_pertanyaan = 0

        self.button_mulai.pack_forget()
        self.frame_jawaban.pack(pady=20)

        self.tampilkan_pertanyaan()

    #menampilkan pertanyaan
    def tampilkan_pertanyaan(self):
        if self.index_pertanyaan < len(semua_gejala):
            kode, teks = semua_gejala[self.index_pertanyaan]
            self.label_tanya.config(text=teks)
        else:
            self.proses_hasil()

    #jawaban
    def jawab(self, respon):
        if respon == 'y':
            kode = semua_gejala[self.index_pertanyaan][0]
            self.gejala_terpilih.append(kode)

        self.index_pertanyaan += 1
        self.tampilkan_pertanyaan()

    #proses hasil diagnosa
    def proses_hasil(self):
        hasil = []

        for kerusakan, syarat in database_kerusakan.items():
            if all(s in self.gejala_terpilih for s in syarat):
                hasil.append(kerusakan)

        if hasil:
            message = "Kerusakan terdeteksi:\n\n"
            for h in hasil:
                message += f"{h}\nSolusi: {solusi[h]}\n\n"
        else:
            message = "Tidak ada kerusakan yang cocok dengan gejala."

        messagebox.showinfo("Hasil Diagnosa", message)

        # Reset
        self.frame_jawaban.pack_forget()
        self.button_mulai.pack(pady=10)
        self.label_tanya.config(text="Diagnosa selesai. Ingin mengulangi?")

#main
if __name__ == "__main__":
    root = tk.Tk()
    app = AplikasiPakar(root)
    root.mainloop()