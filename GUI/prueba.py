from tkinter import *


ventana = Tk()
ventana.geometry("1120x630")
ventana.config(background="#9ad0dc")
ventana.title("DESAFIO SIMU")
ventana.resizable(False,False)
img1 = PhotoImage(file=r"C:\Users\kevin\OneDrive\Escritorio\GUI\planteamiento.png")
img2 = PhotoImage(file=r"C:\Users\kevin\OneDrive\Escritorio\GUI\tabladeconectividad.png")
img3 = PhotoImage(file=r"C:\Users\kevin\OneDrive\Escritorio\GUI\localizacion.png")




def func0():
    frame1.lift()
    Button(ventana, text="PLANTEAMIENTIO",width=23,command=func0,height=2,background="#2740A5",foreground="#2FB7C6").grid(row=0,column=20,columnspan=5)
    Button(ventana, text="LOCALIZACIÓN", command=func1,width=23,height=2).grid(row=1,column=20,columnspan=5)
    Button(ventana, text="INTERPOLACION", command=func2,width=23,height=2).grid(row=2,column=20,columnspan=5)
    Button(ventana, text="RESIDUALES", command=func3,width=23,height=2).grid(row=3,column=20,columnspan=5)
    Button(ventana, text="RESIDUOS PONDERADOS", command=func4,width=23,height=2).grid(row=4,column=20,columnspan=5)
    Button(ventana, text="GALERKIN", command=func5,width=23,height=2).grid(row=5,column=20,columnspan=5)
    Button(ventana, text="INTEGRACIÓN POR PARTES", command=func6,width=23,height=2).grid(row=6,column=20,columnspan=5)
    Button(ventana, text="COMPONENTES DE MATRIZ", command=func7,width=23,height=2).grid(row=7,column=20,columnspan=5)
    Button(ventana, text="CONDICIONES DE CONTORNO ", command=func8,width=23,height=2).grid(row=8,column=20,columnspan=5)
    Button(ventana, text="ENSAMBLAJE", command=func9,width=23,height=2).grid(row=9,column=20,columnspan=5)

def func1():
    frame2.lift()
    Button(ventana, text="TABLA DE CONECTIVIDADES",width=23,command=func0,height=2).grid(row=0,column=20,columnspan=5)
    Button(ventana, text="LOCALIZACIÓN", command=func1,width=23,height=2).grid(row=1,column=20,columnspan=5)
    Button(ventana, text="INTERPOLACION", command=func2,width=23,height=2).grid(row=2,column=20,columnspan=5)
    Button(ventana, text="RESIDUALES", command=func3,width=23,height=2).grid(row=3,column=20,columnspan=5)
    Button(ventana, text="RESIDUOS PONDERADOS", command=func4,width=23,height=2).grid(row=4,column=20,columnspan=5)
    Button(ventana, text="GALERKIN", command=func5,width=23,height=2).grid(row=5,column=20,columnspan=5)
    Button(ventana, text="INTEGRACIÓN POR PARTES", command=func6,width=23,height=2).grid(row=6,column=20,columnspan=5)
    Button(ventana, text="COMPONENTES DE MATRIZ", command=func7,width=23,height=2).grid(row=7,column=20,columnspan=5)
    Button(ventana, text="CONDICIONES DE CONTORNO ", command=func8,width=23,height=2).grid(row=8,column=20,columnspan=5)
    Button(ventana, text="ENSAMBLAJE", command=func9,width=23,height=2).grid(row=9,column=20,columnspan=5)

def func2():
    frame3.lift()
    Button(ventana, text="TABLA DE CONECTIVIDADES",width=23,command=func0,height=2).grid(row=0,column=20,columnspan=5)
    Button(ventana, text="LOCALIZACIÓN", command=func1,width=23,height=2).grid(row=1,column=20,columnspan=5)
    Button(ventana, text="INTERPOLACION", command=func2,width=23,height=2).grid(row=2,column=20,columnspan=5)
    Button(ventana, text="RESIDUALES", command=func3,width=23,height=2).grid(row=3,column=20,columnspan=5)
    Button(ventana, text="RESIDUOS PONDERADOS", command=func4,width=23,height=2).grid(row=4,column=20,columnspan=5)
    Button(ventana, text="GALERKIN", command=func5,width=23,height=2).grid(row=5,column=20,columnspan=5)
    Button(ventana, text="INTEGRACIÓN POR PARTES", command=func6,width=23,height=2).grid(row=6,column=20,columnspan=5)
    Button(ventana, text="COMPONENTES DE MATRIZ", command=func7,width=23,height=2).grid(row=7,column=20,columnspan=5)
    Button(ventana, text="CONDICIONES DE CONTORNO ", command=func8,width=23,height=2).grid(row=8,column=20,columnspan=5)
    Button(ventana, text="ENSAMBLAJE", command=func9,width=23,height=2).grid(row=9,column=20,columnspan=5)

def func3():
    frame1.lift()
    Button(ventana, text="TABLA DE CONECTIVIDADES",width=23,command=func0,height=2).grid(row=0,column=20,columnspan=5)
    Button(ventana, text="LOCALIZACIÓN", command=func1,width=23,height=2).grid(row=1,column=20,columnspan=5)
    Button(ventana, text="INTERPOLACION", command=func2,width=23,height=2).grid(row=2,column=20,columnspan=5)
    Button(ventana, text="RESIDUALES", command=func3,width=23,height=2).grid(row=3,column=20,columnspan=5)
    Button(ventana, text="RESIDUOS PONDERADOS", command=func4,width=23,height=2).grid(row=4,column=20,columnspan=5)
    Button(ventana, text="GALERKIN", command=func5,width=23,height=2).grid(row=5,column=20,columnspan=5)
    Button(ventana, text="INTEGRACIÓN POR PARTES", command=func6,width=23,height=2).grid(row=6,column=20,columnspan=5)
    Button(ventana, text="COMPONENTES DE MATRIZ", command=func7,width=23,height=2).grid(row=7,column=20,columnspan=5)
    Button(ventana, text="CONDICIONES DE CONTORNO ", command=func8,width=23,height=2).grid(row=8,column=20,columnspan=5)
    Button(ventana, text="ENSAMBLAJE", command=func9,width=23,height=2).grid(row=9,column=20,columnspan=5)

def func4():
    frame2.lift()
    Button(ventana, text="TABLA DE CONECTIVIDADES",width=23,command=func0,height=2).grid(row=0,column=20,columnspan=5)
    Button(ventana, text="LOCALIZACIÓN", command=func1,width=23,height=2).grid(row=1,column=20,columnspan=5)
    Button(ventana, text="INTERPOLACION", command=func2,width=23,height=2).grid(row=2,column=20,columnspan=5)
    Button(ventana, text="RESIDUALES", command=func3,width=23,height=2).grid(row=3,column=20,columnspan=5)
    Button(ventana, text="RESIDUOS PONDERADOS", command=func4,width=23,height=2).grid(row=4,column=20,columnspan=5)
    Button(ventana, text="GALERKIN", command=func5,width=23,height=2).grid(row=5,column=20,columnspan=5)
    Button(ventana, text="INTEGRACIÓN POR PARTES", command=func6,width=23,height=2).grid(row=6,column=20,columnspan=5)
    Button(ventana, text="COMPONENTES DE MATRIZ", command=func7,width=23,height=2).grid(row=7,column=20,columnspan=5)
    Button(ventana, text="CONDICIONES DE CONTORNO ", command=func8,width=23,height=2).grid(row=8,column=20,columnspan=5)
    Button(ventana, text="ENSAMBLAJE", command=func9,width=23,height=2).grid(row=9,column=20,columnspan=5)

def func5():
    frame3.lift()
    Button(ventana, text="TABLA DE CONECTIVIDADES",width=23,command=func0,height=2).grid(row=0,column=20,columnspan=5)
    Button(ventana, text="LOCALIZACIÓN", command=func1,width=23,height=2).grid(row=1,column=20,columnspan=5)
    Button(ventana, text="INTERPOLACION", command=func2,width=23,height=2).grid(row=2,column=20,columnspan=5)
    Button(ventana, text="RESIDUALES", command=func3,width=23,height=2).grid(row=3,column=20,columnspan=5)
    Button(ventana, text="RESIDUOS PONDERADOS", command=func4,width=23,height=2).grid(row=4,column=20,columnspan=5)
    Button(ventana, text="GALERKIN", command=func5,width=23,height=2).grid(row=5,column=20,columnspan=5)
    Button(ventana, text="INTEGRACIÓN POR PARTES", command=func6,width=23,height=2).grid(row=6,column=20,columnspan=5)
    Button(ventana, text="COMPONENTES DE MATRIZ", command=func7,width=23,height=2).grid(row=7,column=20,columnspan=5)
    Button(ventana, text="CONDICIONES DE CONTORNO ", command=func8,width=23,height=2).grid(row=8,column=20,columnspan=5)
    Button(ventana, text="ENSAMBLAJE", command=func9,width=23,height=2).grid(row=9,column=20,columnspan=5)

def func6():
    frame1.lift()
    Button(ventana, text="TABLA DE CONECTIVIDADES",width=23,command=func0,height=2).grid(row=0,column=20,columnspan=5)
    Button(ventana, text="LOCALIZACIÓN", command=func1,width=23,height=2).grid(row=1,column=20,columnspan=5)
    Button(ventana, text="INTERPOLACION", command=func2,width=23,height=2).grid(row=2,column=20,columnspan=5)
    Button(ventana, text="RESIDUALES", command=func3,width=23,height=2).grid(row=3,column=20,columnspan=5)
    Button(ventana, text="RESIDUOS PONDERADOS", command=func4,width=23,height=2).grid(row=4,column=20,columnspan=5)
    Button(ventana, text="GALERKIN", command=func5,width=23,height=2).grid(row=5,column=20,columnspan=5)
    Button(ventana, text="INTEGRACIÓN POR PARTES", command=func6,width=23,height=2).grid(row=6,column=20,columnspan=5)
    Button(ventana, text="COMPONENTES DE MATRIZ", command=func7,width=23,height=2).grid(row=7,column=20,columnspan=5)
    Button(ventana, text="CONDICIONES DE CONTORNO ", command=func8,width=23,height=2).grid(row=8,column=20,columnspan=5)
    Button(ventana, text="ENSAMBLAJE", command=func9,width=23,height=2).grid(row=9,column=20,columnspan=5)

def func7():
    frame2.lift()
    Button(ventana, text="TABLA DE CONECTIVIDADES",width=23,command=func0,height=2).grid(row=0,column=20,columnspan=5)
    Button(ventana, text="LOCALIZACIÓN", command=func1,width=23,height=2).grid(row=1,column=20,columnspan=5)
    Button(ventana, text="INTERPOLACION", command=func2,width=23,height=2).grid(row=2,column=20,columnspan=5)
    Button(ventana, text="RESIDUALES", command=func3,width=23,height=2).grid(row=3,column=20,columnspan=5)
    Button(ventana, text="RESIDUOS PONDERADOS", command=func4,width=23,height=2).grid(row=4,column=20,columnspan=5)
    Button(ventana, text="GALERKIN", command=func5,width=23,height=2).grid(row=5,column=20,columnspan=5)
    Button(ventana, text="INTEGRACIÓN POR PARTES", command=func6,width=23,height=2).grid(row=6,column=20,columnspan=5)
    Button(ventana, text="COMPONENTES DE MATRIZ", command=func7,width=23,height=2).grid(row=7,column=20,columnspan=5)
    Button(ventana, text="CONDICIONES DE CONTORNO ", command=func8,width=23,height=2).grid(row=8,column=20,columnspan=5)
    Button(ventana, text="ENSAMBLAJE", command=func9,width=23,height=2).grid(row=9,column=20,columnspan=5)

def func8():
    frame3.lift()
    Button(ventana, text="TABLA DE CONECTIVIDADES",width=23,command=func0,height=2).grid(row=0,column=20,columnspan=5)
    Button(ventana, text="LOCALIZACIÓN", command=func1,width=23,height=2).grid(row=1,column=20,columnspan=5)
    Button(ventana, text="INTERPOLACION", command=func2,width=23,height=2).grid(row=2,column=20,columnspan=5)
    Button(ventana, text="RESIDUALES", command=func3,width=23,height=2).grid(row=3,column=20,columnspan=5)
    Button(ventana, text="RESIDUOS PONDERADOS", command=func4,width=23,height=2).grid(row=4,column=20,columnspan=5)
    Button(ventana, text="GALERKIN", command=func5,width=23,height=2).grid(row=5,column=20,columnspan=5)
    Button(ventana, text="INTEGRACIÓN POR PARTES", command=func6,width=23,height=2).grid(row=6,column=20,columnspan=5)
    Button(ventana, text="COMPONENTES DE MATRIZ", command=func7,width=23,height=2).grid(row=7,column=20,columnspan=5)
    Button(ventana, text="CONDICIONES DE CONTORNO ", command=func8,width=23,height=2).grid(row=8,column=20,columnspan=5)
    Button(ventana, text="ENSAMBLAJE", command=func9,width=23,height=2).grid(row=9,column=20,columnspan=5)

def func9():
    frame1.lift()
    Button(ventana, text="TABLA DE CONECTIVIDADES",width=23,command=func0,height=2).grid(row=0,column=20,columnspan=5)
    Button(ventana, text="LOCALIZACIÓN", command=func1,width=23,height=2).grid(row=1,column=20,columnspan=5)
    Button(ventana, text="INTERPOLACION", command=func2,width=23,height=2).grid(row=2,column=20,columnspan=5)
    Button(ventana, text="RESIDUALES", command=func3,width=23,height=2).grid(row=3,column=20,columnspan=5)
    Button(ventana, text="RESIDUOS PONDERADOS", command=func4,width=23,height=2).grid(row=4,column=20,columnspan=5)
    Button(ventana, text="GALERKIN", command=func5,width=23,height=2).grid(row=5,column=20,columnspan=5)
    Button(ventana, text="INTEGRACIÓN POR PARTES", command=func6,width=23,height=2).grid(row=6,column=20,columnspan=5)
    Button(ventana, text="COMPONENTES DE MATRIZ", command=func7,width=23,height=2).grid(row=7,column=20,columnspan=5)
    Button(ventana, text="CONDICIONES DE CONTORNO ", command=func8,width=23,height=2).grid(row=8,column=20,columnspan=5)
    Button(ventana, text="ENSAMBLAJE", command=func9,width=23,height=2).grid(row=9,column=20,columnspan=5)


frame1 = Label(ventana, image=img1,height=600,width=900)
frame2 = Label(ventana, image=img2,height=600,width=900)
frame3 =  Label(ventana, image=img3,height=600,width=900)

frame1.grid(row=0,column=5,padx=15,pady=10,columnspan=15,rowspan=10)
frame2.grid(row=0,column=5,padx=15,pady=10,columnspan=15,rowspan=10)
frame3.grid(row=0,column=5,padx=15,pady=10,columnspan=15,rowspan=10)

Button(ventana, text="TABLA DE CONECTIVIDADES",width=23,command=func0,height=2).grid(row=0,column=20,columnspan=5)
Button(ventana, text="LOCALIZACIÓN", command=func1,width=23,height=2).grid(row=1,column=20,columnspan=5)
Button(ventana, text="INTERPOLACION", command=func2,width=23,height=2).grid(row=2,column=20,columnspan=5)
Button(ventana, text="RESIDUALES", command=func3,width=23,height=2).grid(row=3,column=20,columnspan=5)
Button(ventana, text="RESIDUOS PONDERADOS", command=func4,width=23,height=2).grid(row=4,column=20,columnspan=5)
Button(ventana, text="GALERKIN", command=func5,width=23,height=2).grid(row=5,column=20,columnspan=5)
Button(ventana, text="INTEGRACIÓN POR PARTES", command=func6,width=23,height=2).grid(row=6,column=20,columnspan=5)
Button(ventana, text="COMPONENTES DE MATRIZ", command=func7,width=23,height=2).grid(row=7,column=20,columnspan=5)
Button(ventana, text="CONDICIONES DE CONTORNO ", command=func8,width=23,height=2).grid(row=8,column=20,columnspan=5)
Button(ventana, text="ENSAMBLAJE", command=func9,width=23,height=2).grid(row=9,column=20,columnspan=5)

    

ventana.mainloop()