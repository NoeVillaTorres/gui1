import tkinter as tk
from tkinter import ttk

def submit():
    # Función a ejecutar cuando se presione el botón "Submit"
    pass

# Crear ventana principal
window = tk.Tk()
window.title("Interfaz Gráfica")
window.geometry("600x450")
window.configure(bg="gray")

# Dividir ventana en 5 partes verticales del mismo tamaño
top_frame = tk.Frame(window, bg="gray", height=90)
top_frame.pack(fill="x")

middle_frame = tk.Frame(window, bg="gray", height=90)
middle_frame.pack(fill="x")

middle_frame2 = tk.Frame(window, bg="gray", height=90)
middle_frame2.pack(fill="x")

middle_frame3 = tk.Frame(window, bg="gray", height=90)
middle_frame3.pack(fill="x")

bottom_frame = tk.Frame(window, bg="gray", height=90)
bottom_frame.pack(fill="x")

# Parte 1: Tabs
tabs = ttk.Notebook(top_frame)

tab1 = ttk.Frame(tabs)
tab1.configure(bg="light blue")
tabs.add(tab1, text="Add")

tab2 = ttk.Frame(tabs)
tab2.configure(bg="light blue")
tabs.add(tab2, text="Delete")

tab3 = ttk.Frame(tabs)
tab3.configure(bg="light blue")
tabs.add(tab3, text="Search")

tab4 = ttk.Frame(tabs)
tab4.configure(bg="light blue")
tabs.add(tab4, text="Services")

tab5 = ttk.Frame(tabs)
tab5.configure(bg="light blue")
tabs.add(tab5, text="Help")

tabs.pack(fill="both", expand=True)

# Parte 2: Textfields
label1 = tk.Label(middle_frame, text="First Name", bg="gray")
label1.pack(side="left")
textfield1 = tk.Entry(middle_frame)
textfield1.pack(side="left")

label2 = tk.Label(middle_frame, text="Last Name", bg="gray")
label2.pack(side="left")
textfield2 = tk.Entry(middle_frame)
textfield2.pack(side="left")

label3 = tk.Label(middle_frame, text="Birthday", bg="gray")
label3.pack(side="left")
textfield3 = tk.Entry(middle_frame)
textfield3.pack(side="left")

label4 = tk.Label(middle_frame, text="Country", bg="gray")
label4.pack(side="left")
textfield4 = tk.Entry(middle_frame)
textfield4.pack(side="left")

# Parte 3: Tarjeta de Crédito y Radiobuttons
label5 = tk.Label(middle_frame2, text="Tarjeta de Crédito", bg="gray")
label5.pack(side="left")

credit_card_var = tk.StringVar()
radiobutton1 = tk.Radiobutton(middle_frame2, text="Visa", variable=credit_card_var, value="Visa", bg="gray")
radiobutton1.pack(side="left")

radiobutton2 = tk.Radiobutton(middle_frame2, text="Mastercard", variable=credit_card_var, value="Mastercard", bg="gray")
radiobutton2.pack(side="left")

# Parte 4: Room Type y Total Stay Time
label6 = tk.Label(middle_frame3, text="Room Type", bg="gray")
label6.pack(side="left")

room_type_var = tk.StringVar()
radiobutton3 = tk.Radiobutton(middle_frame3, text="Normal", variable=room_type_var, value="Normal", bg="gray")
radiobutton3.pack(anchor='w')
radiobutton4 = tk.Radiobutton(middle_frame3, text="Familiar", variable=room_type_var, value="Familiar", bg="gray")
radiobutton4.pack(anchor='w')

radiobutton5 = tk.Radiobutton(middle_frame3, text="Special", variable=room_type_var, value="Special", bg="gray")
radiobutton5.pack(anchor='w')

label7 = tk.Label(middle_frame3, text="Total Staying Time (days)", bg="gray")
label7.pack(side="left")

textfield5 = tk.Entry(middle_frame3, width=10)
textfield5.pack(side="left")
submit_button = tk.Button(bottom_frame, text="Submit", command=submit)

window.mainloop()
