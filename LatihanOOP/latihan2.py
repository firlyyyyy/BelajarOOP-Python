import tkinter

main_window = tkinter.Tk()

label = tkinter.Label(main_window, text="Tes")
tombol = tkinter.Button(main_window, text="klik")

label.pack()
tombol.pack()

main_window.mainloop()