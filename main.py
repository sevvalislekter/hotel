from  tkinter import *
from tkinter import messagebox

root = Tk()
root.title("hotel kullanıcı giriş ekranı")
root.geometry("300x200")


b1=Label(root,text="giriş").pack()







def giris_yap():
    mail = mail_entry.get()
    sifre = sifre_entry.get()



def kayit_ol():
    kayit_ekrani = Toplevel(root)

    mail_label = Label(kayit_ekrani, text="Mail:")
    mail_label.pack()
    mail_entry = Entry(kayit_ekrani)
    mail_entry.pack()

    sifre_label = Label(kayit_ekrani, text="Şifre:")
    sifre_label.pack()
    sifre_entry = Entry(kayit_ekrani)
    sifre_entry.pack()

    ulke_label = Label(kayit_ekrani, text="Ülke:")
    ulke_label.pack()
    ulke_entry = Entry(kayit_ekrani)
    ulke_entry.pack()

    sehir_label = Label(kayit_ekrani, text="Şehir:")
    sehir_label.pack()
    sehir_entry = Entry(kayit_ekrani)
    sehir_entry.pack()

    kayit_button = Button(kayit_ekrani, text="Kayıt Ol", command=giris_yap())
    kayit_button.pack()

def  hotelbilgileri():
            hotelekrani=Toplevel(root)

            hotel1 = Label(hotelekrani, text="bodrum ada hotel\n özellikleri \n havuzlu,klimalı,1 gece 20000").pack()

            hotel2 = Label(hotelekrani, text="bodrum marmaris hotel \n özellikleri \nhavuz,bar,tek gece 2070").pack()
            hotelb=Button(hotelekrani,text=" uygun olanlar").pack()


mail_label = Label(root, text="Mail:")
mail_label.pack()
mail_entry = Entry(root)
mail_entry.pack()

sifre_label = Label(root, text="Şifre:")
sifre_label.pack()
sifre_entry = Entry(root)
sifre_entry.pack()

giris_button = Button(root, text="Giriş Yap", command=giris_yap)
giris_button.pack()

kayit_button = Button(root, text="Kayıt Ol", command=kayit_ol)
kayit_button.pack()

hotelb=Button(root,text="seçenkler",command=hotelbilgileri())
hotelb.pack()









root.mainloop()








