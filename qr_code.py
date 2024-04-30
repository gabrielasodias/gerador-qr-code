import tkinter as tk

# Configurações da janela principal
window = tk.Tk()
window.title(' QRCode')
window.geometry('350x500')
window.resizable(False, False)
window.anchor('center')
window.iconbitmap('ico-img/qrcode_edit_icon_138259.ico')
window.configure(background='black')

# Rótulo e entrada de texto
label_text = tk.Label(text="Digite o texto ou link que deseja gerar em QR Code: ", background='black', foreground='white', font='OpenSans 10 ')
label_text.grid(column=0, row=0, columnspan=2, pady=10,) 
textEntry = tk.Entry()
textEntry.grid(column=0, row=1, columnspan=2, padx=10)

# Botão para gerar QR Code
button = tk.Button(window, text="Gerar QR Code",)
button.grid(column=0, row=2, columnspan=2, pady=10)

# Label para exibir a imagem do QR Code
label_img = tk.Label(background='black')
label_img.grid(column=0, row=3, columnspan=2, pady=10)

# Loop principal
window.mainloop()