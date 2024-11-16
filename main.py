import tkinter as tk
import random
from tkinter import simpledialog

class TahminOyunu:
    def __init__(self, root):
        self.root = root
        self.root.title("Tahmin Oyunu")

        self.seviyeKatsayisi = 1
        self.dogruSayisi = 0
        self.yanlisSayisi = 0

        self.create_widgets()

    def create_widgets(self):
        self.seviye_label = tk.Label(self.root, text="Seviye seçiniz (Kolay:1, Orta:2, Zor:3):")
        self.seviye_label.pack()

        self.seviye_entry = tk.Entry(self.root)
        self.seviye_entry.pack()

        self.seviye_button = tk.Button(self.root, text="Seviye Ayarla", command=self.ayarla_seviye)
        self.seviye_button.pack()

        self.devam_button = tk.Button(self.root, text="Devam Et", command=self.devam_et)
        self.devam_button.pack()

        self.sonuc_label = tk.Label(self.root, text="", font=("Helvetica", 12))
        self.sonuc_label.pack()

    def ayarla_seviye(self):
        seviye = self.seviye_entry.get()
        if seviye == "1":
            self.seviyeKatsayisi = 10
        elif seviye == "2":
            self.seviyeKatsayisi = 5
        elif seviye == "3":
            self.seviyeKatsayisi = 1
        else:
            self.sonuc_label.config(text="Lütfen geçerli bir seviye seçiniz!")
            return
        self.sonuc_label.config(text="Seviye ayarlandı!")

    def devam_et(self):
        rastgeleSayisi = random.randint(1, 100 // self.seviyeKatsayisi) * self.seviyeKatsayisi
        metin = "{:>" + str(rastgeleSayisi) + "}"
        self.root.update()
        tahmin = simpledialog.askstring("Tahmin", "Aşağıda yazılan 0 rakamının sol tarafında olan boşluk sayısını tahmin ediniz. 0-100 arası " + str(self.seviyeKatsayisi) + " katları olan bir sayıdır.")
        if tahmin == str(rastgeleSayisi):
            self.dogruSayisi += 1
            sonuc_text = f"Tebrikler. Doğru cevap sayınız= {self.dogruSayisi}, Yanlış cevap sayınız= {self.yanlisSayisi}"
        else:
            self.yanlisSayisi += 1
            sonuc_text = f"Maalesef bilemediniz. Doğru cevap {rastgeleSayisi} olacaktı. Doğru cevap sayınız= {self.dogruSayisi}, Yanlış cevap sayınız= {self.yanlisSayisi}"
        self.sonuc_label.config(text=sonuc_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = TahminOyunu(root)
    root.mainloop()
