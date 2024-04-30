import tkinter as tk
import qrcode
from PIL import ImageTk

# Função para gerar o QR Code
def qrcode_generator():
    data_to_generate = textEntry.get() # Obtenção dos dados a serem gerados
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    ) # Criação do objeto QRCode

    qr.add_data(data_to_generate) # Adicionando os dados ao QRCode
    qr.make(fit=True)  # Gerando o QRCode
    img = qr.make_image(fill_color="black", back_color="white") # Criação da imagem do QRCode com as cores configuradas
    img.thumbnail((300, 300)) # Redimensionamento da imagem (tamanho máximo)
   
    # Configuração da imagem para exibição no widget
    show_img = ImageTk.PhotoImage(img)
    label_img.configure(image=show_img)
    label_img.image = show_img

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

# Botão para chamar a função que gera o QR Code
button = tk.Button(window, text="Gerar QR Code", command=qrcode_generator)
button.grid(column=0, row=2, columnspan=2, pady=10)

# Label para exibir a imagem do QR Code
label_img = tk.Label(background='black')
label_img.grid(column=0, row=3, columnspan=2, pady=10)

# Loop principal
window.mainloop()