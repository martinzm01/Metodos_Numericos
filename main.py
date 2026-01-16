import math
from tkinter import Text, Scrollbar, RIGHT, Y, END
import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter import font
<<<<<<< HEAD
import math
=======
>>>>>>> d06f54a (Cambio de la dimension de la ventana y cambio de rama)
import numpy as np
from ttkbootstrap.tooltip import ToolTip
from metodosnumericos.bisection import bisection
from metodosnumericos.newton import newton
from metodosnumericos.secant import secant
from metodosnumericos.gauss_jordan import gauss_jordan
from metodosnumericos.regula_falsi import regula_falsi 
from metodosnumericos.jacobi import jacobi
from metodosnumericos.gauss_seidel import gauss_seidel
<<<<<<< HEAD
from metodosnumericos.simpson import regla_simpson
from metodosnumericos.trapecio import regla_trapecio

=======
>>>>>>> d06f54a (Cambio de la dimension de la ventana y cambio de rama)
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk
<<<<<<< HEAD

metodo_seleccionado = None
ventana=tb.Window(themename="cyborg")
ventana.geometry("1920x1080")
ventana.title("MetodosNumericos")
temas_disponibles = ["vapor", "cyborg", "solar"]
=======
>>>>>>> d06f54a (Cambio de la dimension de la ventana y cambio de rama)

metodo_seleccionado = None

temas_disponibles = ["vapor", "cyborg", "solar"]

<<<<<<< HEAD
=======
ventana=tb.Window(themename="vapor")
# Obtener dimensiones de la pantalla
ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()

ancho_ventana = int(ancho_pantalla * 0.9)
alto_ventana = int(alto_pantalla * 0.9)

pos_x = (ancho_pantalla - ancho_ventana) // 2
pos_y = (alto_pantalla - alto_ventana) // 2

ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{pos_x}+{pos_y}")
ventana.title("MetodosNumericos")



##Marco de titulo y temas
Frame_titulo =tb.Frame(ventana,padding=(0,0,0,0))
Frame_titulo.pack(fill="both",expand=True)
label_titulo=tb.Label(Frame_titulo,text="FX",bootstyle="default",font=("Segoe UI",40,"bold"),padding=(10,0,10,0))
label_titulo.pack(side="bottom",pady=(0,0))
>>>>>>> d06f54a (Cambio de la dimension de la ventana y cambio de rama)


##Marco de titulo y temas
Frame_titulo =tb.Frame(ventana,padding=(0,0,0,0))
Frame_titulo.pack(fill="both",expand=True)
label_titulo=tb.Label(Frame_titulo,text="FX",bootstyle="default",font=("Segoe UI",40,"bold"),padding=(10,0,10,0))
label_titulo.pack(side="bottom",pady=(0,0))

####cambiar tema
def cambiar_tema(event):
    nuevo_tema = combo_temas.get()
    ventana.style.theme_use(nuevo_tema)
    return nuevo_tema

####cambiar temas
combo_temas = tb.Combobox(Frame_titulo, values=temas_disponibles, width=10, bootstyle="success")
combo_temas.set("cyborg")  # Tema inicial
tema_actual=ventana.style.theme_use()
combo_temas.pack(side="right",pady=(20,0),padx=10)
tb.Label(Frame_titulo, text="Selecciona Tema:", font=("Segoe UI",12)).pack(side="right", padx=5,pady=(20,0))
combo_temas.bind("<<ComboboxSelected>>", cambiar_tema)

# Definir fuente personalizada
fuente_titulo = font.Font(family="Segoe UI", size=25, weight="bold")

# Crear un estilo nuevo para Labelframe
style = tb.Style()
style.configure("Custom.TLabelframe", font=fuente_titulo)


#####Marco Izquiero
frame_izquierda=tb.Frame(ventana,width=600,style="Custom.TLabelframe")
frame_izquierda.pack(fill="both",side="left",expand=True,pady=0)


#####MArco Derecho
frame_salida=tb.Frame(ventana,width=600,style="Custom.TLabelframe")
frame_salida.pack(fill="both",side="right",expand=True,pady=0)


frame_graficadora=tb.Frame(frame_salida,style="Custom.TLabelframe")
frame_graficadora.pack(expand=True,fill="both",pady=0)

frame_derecha_inferior=tb.Frame(frame_salida,style="Custom.TLabelframe")
frame_derecha_inferior.pack(expand=True,fill="both")


##Marco de Metodos

frame_metodos=tb.Frame(frame_izquierda,padding=(40,20,40,20),style="Custom.TLabelframe") ###izq /arriba / der/ abajo
frame_metodos.grid(row=0,pady=(40,20),padx=1)

label_selecMetodo=tb.Label(frame_metodos,text="Seleccion del Método            ",font=("Segoe UI",16)).grid(row=0,column=0,pady=10,padx=0)

boton_biseccion=tb.Button(frame_metodos,width=40,text="Biseccion",bootstyle="default", command=lambda: mostrar_campos_para_metodo("Biseccion"))
boton_newton=tb.Button(frame_metodos,width=40,text="Newton",bootstyle="warning", command=lambda: mostrar_campos_para_metodo("Newton"))
boton_regula_falsi=tb.Button(frame_metodos,width=40,text="Regula Falsi",bootstyle="info", command=lambda: mostrar_campos_para_metodo("Regula Falsi"))
boton_jacobi=tb.Button(frame_metodos,width=40,text="Jacobi",bootstyle="secondary", command=lambda: mostrar_campos_para_metodo("Jacobi"))
boton_secante=tb.Button(frame_metodos,width=40,text="Secante",bootstyle="success", command=lambda: mostrar_campos_para_metodo("Secante"))
boton_gauss_jordan=tb.Button(frame_metodos,width=40,text="Gauss-Jordan",bootstyle="danger", command=lambda: mostrar_campos_para_metodo("Gauss-Jordan"))
boton_gauss_seidel=tb.Button(frame_metodos,width=40,text="Runge_Kutta",bootstyle="light", command=lambda: mostrar_campos_para_metodo("Gauss-Seidel"))
boton_graficar=tb.Button(frame_metodos,width=40,text="Graficar",bootstyle="bg", command=lambda: mostrar_campos_para_metodo("Graficar"))
boton_trapecio=tb.Button(frame_metodos,width=40,text="Integracion-Regla del Trapecio",bootstyle="info", command=lambda: mostrar_campos_para_metodo("Trapecio"))
boton_simpson=tb.Button(frame_metodos,width=40,text="Integracion-Simpson",bootstyle="warning", command=lambda: mostrar_campos_para_metodo("Simpson"))


boton_biseccion.grid(row=1,column=0,pady=10,padx=20)
boton_newton.grid(row=1,column=1, pady=10)
boton_regula_falsi.grid(row=2,column=0,padx=20,pady=10)
boton_jacobi.grid(row=2,column=1,padx=10,pady=(10))
boton_secante.grid(row=3,column=0,padx=20,pady=(10,20))
boton_gauss_jordan.grid(row=3,column=1,padx=10,pady=(10,20))
boton_gauss_seidel.grid(row=4,column=0,padx=10,pady=(10,20))
boton_graficar.grid(row=4,column=1,padx=10,pady=(10,20))
boton_trapecio.grid(row=5,column=0,padx=10,pady=(10,20))
boton_simpson.grid(row=5,column=1,padx=10,pady=(10,20))

####comnetarios sobre los botones
ToolTip(boton_biseccion, text="Encuentra raíces - Para Funciones no lineales ")
ToolTip(boton_newton, text="Funciones no Lineales - Requiere la derivada - Convergencia rápida si el punto inicial es bueno.")
ToolTip(boton_regula_falsi, text="Para funciones no lineales - Mejora del método de bisección usando interpolación lineal.")
ToolTip(boton_jacobi, text="Resuelve sistemas lineales por iteraciones sucesivas.")
ToolTip(boton_secante, text="Ecuentra raíces de una funcion no lineal - Aproxima la derivada con una recta secante.")
ToolTip(boton_gauss_jordan, text="Algoritmo directo para resolver sistemas lineales.")
ToolTip(boton_gauss_seidel, text="método iterativo para resolver sistemas de ecuaciones lineales del tipo: ax=b")
ToolTip(boton_graficar, text="Grafica cualquier función f(x)=y")
ToolTip(boton_trapecio, text="Aproxima el área bajo la curva como un trapecio, usando solo los extremos del intervalo")
ToolTip(boton_simpson, text="Aproxima la integral con un parábola (polinomio de grado 2) que pasa por tres puntos.")


####### FRAME de DATOS DE ENTRADA
frame_Entrada=tb.Frame(frame_izquierda,style="Custom.TLabelframe",padding=(52,0,52,20))
frame_Entrada.grid(row=1,pady=0)
    ###Label de la funcion
label_fun1=tb.Label(frame_Entrada,font=("Segoe UI",14),text="f(x)")
label_fun1.grid(row=0,column=0,padx=10,pady=(50,0))
entrada_fun1=tb.Entry(frame_Entrada,width=40)
entrada_fun1.grid(row=0,column=1,padx=10,pady=(50,0))

label_fun2=tb.Label(frame_Entrada,font=("Segoe UI",14))
label_fun2.grid(row=1,column=0,)
entrada_fun2=tb.Entry(frame_Entrada,width=40)
entrada_fun2.grid(row=1,column=1,padx=10)

tb.Label(frame_Entrada,font=("Segoe UI",14)).grid(row=2,column=0)
entrada_fun3=tb.Entry(frame_Entrada,width=40)
entrada_fun3.grid(row=2,column=1,padx=10,)

tb.Label(frame_Entrada,font=("Segoe UI",14)).grid(row=3,column=0)
entrada_fun4=tb.Entry(frame_Entrada,width=40)
entrada_fun4.grid(row=3,column=1,padx=10)

tb.Label(frame_Entrada,font=("Segoe UI",14)).grid(row=4,column=0)
entrada_fun5=tb.Entry(frame_Entrada,width=40)
entrada_fun5.grid(row=4,column=1,padx=10)

tb.Label(frame_Entrada,font=("Segoe UI",14)).grid(row=5,column=0)
entrada_fun6=tb.Entry(frame_Entrada,width=40)
entrada_fun6.grid(row=5,column=1,padx=10,pady=0)

###Labels de parametros
label_a=tb.Label(frame_Entrada,font=("Segoe UI",14),text="A") 
label_a.grid(row=0,column=3,padx=(10,10),pady=(50,0))
entrada_a=tb.Entry(frame_Entrada,width=20)
entrada_a.grid(row=0,column=4,padx=10,pady=(50,0))

label_b=tb.Label(frame_Entrada,font=("Segoe UI",14),text="B")
label_b.grid(row=1,column=3,padx=(10,10))
entrada_b=tb.Entry(frame_Entrada,width=20)
entrada_b.grid(row=1,column=4,padx=(10))

label_x0=tb.Label(frame_Entrada,font=("Segoe UI",14),text="x0")
label_x0.grid(row=2,column=3,padx=(10,10))
entrada_x0=tb.Entry(frame_Entrada,width=20)
entrada_x0.grid(row=2,column=4,padx=10)

label_x1=tb.Label(frame_Entrada,font=("Segoe UI",14),text="x1")
label_x1.grid(row=3,column=3,padx=(10,10))
entrada_x1=tb.Entry(frame_Entrada,width=20)
entrada_x1.grid(row=3,column=4,padx=10)

label_tol=tb.Label(frame_Entrada,font=("Segoe UI",14),text="Tol")
label_tol.grid(row=4,column=3,padx=(10,10))
entrada_tol=tb.Entry(frame_Entrada,width=20)
entrada_tol.grid(row=4,column=4,padx=10)

label_iteraciones=tb.Label(frame_Entrada,font=("Segoe UI",14),text="Iter")
label_iteraciones.grid(row=5,column=3,padx=(10,10))
entrada_max_iter=tb.Entry(frame_Entrada,width=20)
entrada_max_iter.grid(row=5,column=4,padx=10)

####### labels invisibles para ordenar
tb.Label(frame_Entrada,font=("Segoe UI",14),width=5).grid(row=0,column=2,pady=0)
tb.Label(frame_Entrada,font=("Segoe UI",14),width=5).grid(row=1,column=2,pady=0)
tb.Label(frame_Entrada,font=("Segoe UI",14),width=5).grid(row=1,column=2,pady=0)
tb.Label(frame_Entrada,font=("Segoe UI",14),width=5).grid(row=2,column=2,pady=0)
tb.Label(frame_Entrada,font=("Segoe UI",14),width=5).grid(row=3,column=2,pady=0)
tb.Label(frame_Entrada,font=("Segoe UI",14),width=5).grid(row=4,column=2,pady=0)

######GRAFICADORA INICIAL

def graficadora_inicial():
    fig_inicial, ax_inicial = plt.subplots(figsize=(10,4), facecolor='#0F0A16')
    ax_inicial.xaxis.set_major_locator(MaxNLocator(nbins=10))

    ax_inicial.set_xlim(0, 1)
    ax_inicial.set_ylim(-1, 1)
    ax_inicial.set_facecolor('#0F0A16')
    ax_inicial.axhline(0, color='#7BFFF8', linewidth=0.8)
    ax_inicial.axvline(0, color='#7BFFF8', linewidth=0.8)
    ax_inicial.tick_params(colors='#7BFFF8')
    ax_inicial.spines['bottom'].set_color('#7BFFF8')
    ax_inicial.spines['top'].set_color('#7BFFF8')
    ax_inicial.spines['right'].set_color('#7BFFF8')
    ax_inicial.spines['left'].set_color('#7BFFF8')
    ax_inicial.yaxis.label.set_color('white')
    ax_inicial.xaxis.label.set_color('white')
    ax_inicial.title.set_color('white')
    ax_inicial.set_title("Gráfica de f(x)",color='#7BFFF8')
    ax_inicial.grid(True, color="#444444")

    # Eliminar solo el canvas anterior, si existe
    for widget in frame_graficadora.winfo_children():
        widget.destroy()

    # Mostrar el gráfico inicial en el frame_salida
    canvas_grafico = FigureCanvasTkAgg(fig_inicial, master=frame_graficadora)
    canvas_grafico.draw()
    canvas_grafico.get_tk_widget().pack(pady=1)


            ####   METODOS Y FUNCIONES  ######
graficadora_inicial()

def limpiar_entradas_resultados():
    entradas = [
        entrada_fun1,entrada_fun2,entrada_fun3,entrada_fun4,entrada_fun5,entrada_fun6, entrada_a, entrada_b,
        entrada_x0, entrada_x1, entrada_tol, entrada_max_iter
    ]
    for e in entradas:
        e.delete(0, 'end')

    label_raiz.config(text="Solución: ")
    label_iters.config(text="")
    label_historial.config(text="Historial ")
    text_hist.delete("1.0", END)
        # Eliminar todo lo que esté actualmente en el frame de la gráfica
    for widget in frame_graficadora.winfo_children():
        widget.destroy()

    # Crear una nueva figura con solo los ejes
    fig, ax = plt.subplots(figsize=(10, 4), facecolor='#0F0A16')
    ax.set_facecolor('#0F0A16')
    
    # Configurar ejes
    ax.axhline(0, color='#7BFFF8', linewidth=0.8)
    ax.axvline(0, color='#7BFFF8', linewidth=0.8)
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    ax.grid(True, color="#444444")
    ax.set_title("Gráfica vacía")
    ax.xaxis.set_major_locator(MaxNLocator(nbins=10))
    ax.tick_params(colors='#7BFFF8')
    ax.spines['bottom'].set_color('#7BFFF8')
    ax.spines['top'].set_color('#7BFFF8')
    ax.spines['right'].set_color('#7BFFF8')
    ax.spines['left'].set_color('#7BFFF8')
    ax.yaxis.label.set_color('white')
    ax.xaxis.label.set_color('white')
    ax.title.set_color('#7BFFF8')

    # Mostrar la figura en el frame
    canvas = FigureCanvasTkAgg(fig, master=frame_graficadora)
    canvas.draw()
    canvas.get_tk_widget().pack(pady=1)




def calcular_resultado():
    global metodo_seleccionado
    try:
        tol = float(entrada_tol.get())
        iter_max = int(entrada_max_iter.get())

        expresiones = [e.get().strip() for e in (
            entrada_fun1, entrada_fun2, entrada_fun3,
            entrada_fun4, entrada_fun5, entrada_fun6
        ) if e.get().strip()]

        raiz = None
        iters = None
        hist = []

        ###METODOS PARA CALCULAR RAICES
        if metodo_seleccionado in ["Biseccion", "Regula Falsi", "Newton", "Secante"]:
            f = lambda x: eval(expresiones[0], {"x": x, "math": math, "sin": math.sin, "cos": math.cos, "exp": math.exp})
            if metodo_seleccionado == "Biseccion":
                a, b_ = float(entrada_a.get()), float(entrada_b.get())
                raiz, iters, hist = bisection(f, a, b_, tol, iter_max)
            elif metodo_seleccionado == "Regula Falsi":
                a, b_ = float(entrada_a.get()), float(entrada_b.get())
                raiz, iters, hist = regula_falsi(f, a, b_, tol, iter_max)
            elif metodo_seleccionado == "Newton":
                df = lambda x: eval(entrada_fun2.get(), {"x": x})
                x0 = float(entrada_x0.get())
                raiz, iters, hist = newton(f, df, x0, tol, iter_max)
            elif metodo_seleccionado == "Secante":
                x0, x1 = float(entrada_x0.get()), float(entrada_x1.get())
                raiz, iters, hist = secant(f, x0, x1, tol, iter_max)
            ###MOSTRAR RAIZ
            label_raiz.config(text=f"Raíz encontrada: {raiz:.6f}")

            ####graficadora
        
            if ventana.style.theme_use()=="cyborg":
                fig, ax = plt.subplots(figsize=(10, 4), facecolor='black')
                ax.xaxis.set_major_locator(MaxNLocator(nbins=10))  # Muestra hasta 10 valores
                ax.set_facecolor('black')
                x_vals = np.linspace(raiz - 5, raiz + 5, 400)
                y_vals = [f(x) for x in x_vals]
                ax.plot(x_vals, y_vals, label="f(x)", color="white")
                ax.axhline(0, color='white', linewidth=0.8)
                ax.axvline(0, color='white', linewidth=0.8)

                ax.plot(raiz, f(raiz), 'ro')
                ax.annotate(f'{raiz:.2f}', xy=(raiz, f(raiz)), xytext=(raiz, f(raiz)+0.5), color="white")
                
                ax.xaxis.set_major_locator(MaxNLocator(nbins=10))
                ax.set_xlim(-5, 5)
                ax.set_ylim(-5, 5)

                ax.tick_params(colors='white')
                ax.spines['bottom'].set_color('#7BFFF8')
                ax.spines['top'].set_color('#7BFFF8')
                ax.spines['right'].set_color('#7BFFF8')
                ax.spines['left'].set_color('#7BFFF8')
                ax.yaxis.label.set_color('white')
                ax.xaxis.label.set_color('white')
                ax.title.set_color('white')

                ax.set_title("Gráfica de f(x) con raíz")
                ax.grid(True, color="#444444")
                ax.legend(facecolor="#333333", edgecolor="white", labelcolor="white")
                
                

                """  ANTES
                # Eliminar solo el canvas anterior, si existe               
                for widget in frame_graficadora.winfo_children():
                    widget.destroy()

                canvas = FigureCanvasTkAgg(fig, master=frame_graficadora)
                canvas.draw()
                canvas.get_tk_widget().pack(pady=1)
                """
                #--------------DESPUES-----------------
                for widget in frame_graficadora.winfo_children():
                    widget.destroy()
                canvas = FigureCanvasTkAgg(fig, master=frame_graficadora)
                canvas.draw()
                canvas_widget = canvas.get_tk_widget()
                canvas_widget.pack(side="top", fill="both", expand=True)

                # Agregar barra de navegación
                toolbar = NavigationToolbar2Tk(canvas, frame_graficadora)
                toolbar.update()
                toolbar.pack(side=tk.TOP, fill=tk.X)



            else:
                f = lambda x: eval(expresiones[0], {"x": x, "math": math, "sin": math.sin, "cos": math.cos, "exp": math.exp})

                fig, ax = plt.subplots(figsize=(10, 4), facecolor='#0F0A16')
                ax.xaxis.set_major_locator(MaxNLocator(nbins=10))  # Muestra hasta 10 valores
                ax.set_facecolor('#0F0A16')
                x_vals = np.linspace(raiz - 5, raiz + 5, 400)
                y_vals = [f(x) for x in x_vals]
                ax.plot(x_vals, y_vals, label="f(x)", color="#00ffcc")
                ax.axhline(0, color='#7BFFF8', linewidth=0.8)
                ax.axvline(0, color='#7BFFF8', linewidth=0.8)

                ax.plot(raiz, f(raiz), 'ro')
                ax.annotate(f'{raiz:.2f}', xy=(raiz, f(raiz)), xytext=(raiz, f(raiz)+0.5), color="white")
                
                ax.xaxis.set_major_locator(MaxNLocator(nbins=10))
                ax.set_xlim(-5, 5)
                ax.set_ylim(-5, 5)

                ax.tick_params(colors='#7BFFF8')
                ax.spines['bottom'].set_color('#7BFFF8')
                ax.spines['top'].set_color('#7BFFF8')
                ax.spines['right'].set_color('#7BFFF8')
                ax.spines['left'].set_color('#7BFFF8')
                ax.yaxis.label.set_color('white')
                ax.xaxis.label.set_color('white')
                ax.title.set_color('#7BFFF8')

                ax.set_title("Gráfica de f(x) con raíz")
                ax.grid(True, color="#444444")
                ax.legend(facecolor="#333333", edgecolor="white", labelcolor="white")
                
                """  ANTES
                # Eliminar solo el canvas anterior, si existe               
                for widget in frame_graficadora.winfo_children():
                    widget.destroy()

                canvas = FigureCanvasTkAgg(fig, master=frame_graficadora)
                canvas.draw()
                canvas.get_tk_widget().pack(pady=1)
                """


                # Eliminar solo el canvas anterior, si existe
                for widget in frame_graficadora.winfo_children():
                    widget.destroy()
                canvas = FigureCanvasTkAgg(fig, master=frame_graficadora)
                canvas.draw()
                canvas_widget = canvas.get_tk_widget()
                canvas_widget.pack(side="top", fill="both", expand=True)

                # Agregar barra de navegación
                toolbar = NavigationToolbar2Tk(canvas, frame_graficadora)
                toolbar.update()
                toolbar.pack(side=tk.TOP, fill=tk.X)


        elif metodo_seleccionado == "Graficar":  
            if ventana.style.theme_use()=="cyborg":
                lim_inf_x, lim_sup_x = float(entrada_a.get()), float(entrada_b.get())
                lim_inf_y,lim_sup_y=float(entrada_x0.get()), float(entrada_x1.get())

                f = lambda x: eval(expresiones[0], {"x": x, "math": math, "sin": math.sin, "cos": math.cos, "exp": math.exp})

                fig, ax = plt.subplots(figsize=(10, 4), facecolor='black')
                ax.xaxis.set_major_locator(MaxNLocator(nbins=10))  # Muestra hasta 10 valores
                ax.set_facecolor('black')
                x_vals = np.linspace(lim_inf_x,lim_sup_x, 400)
                y_vals = [f(x) for x in x_vals]
                ax.plot(x_vals, y_vals, label="f(x)", color="white")
                ax.axhline(0, color='white', linewidth=0.8)
                ax.axvline(0, color='white', linewidth=0.8)

                
                ax.xaxis.set_major_locator(MaxNLocator(nbins=10))
                #ax.set_xlim(lim_inf_x, lim_sup_x)
                #ax.set_ylim(lim_inf_y,lim_sup_y)
                ax.relim()
                ax.autoscale_view()

                ax.tick_params(colors='white')
                ax.spines['bottom'].set_color('#7BFFF8')
                ax.spines['top'].set_color('#7BFFF8')
                ax.spines['right'].set_color('#7BFFF8')
                ax.spines['left'].set_color('#7BFFF8')
                ax.yaxis.label.set_color('white')
                ax.xaxis.label.set_color('white')
                ax.title.set_color('white')

                ax.set_title("Gráfica de f(x) con raíz")
                ax.grid(True, color="#444444")
                ax.legend(facecolor="#333333", edgecolor="white", labelcolor="white")
                
                
                # Eliminar solo el canvas anterior, si existe
                for widget in frame_graficadora.winfo_children():
                    widget.destroy()

                """ANTES
                #canvas = FigureCanvasTkAgg(fig, master=frame_graficadora)
                #canvas.draw()
                #canvas.get_tk_widget().pack(pady=1)
                """

                canvas = FigureCanvasTkAgg(fig, master=frame_graficadora) 
                canvas.draw()
                canvas_widget = canvas.get_tk_widget()
                canvas_widget.pack(side="top", fill="both", expand=True)

                # Agregar barra de navegación (zoom)
                toolbar = NavigationToolbar2Tk(canvas, frame_graficadora)
                toolbar.update()
                toolbar.pack(side=tk.TOP, fill=tk.X)
                
            else:
                lim_inf_x, lim_sup_x = float(entrada_a.get()), float(entrada_b.get())
                lim_inf_y,lim_sup_y=float(entrada_x0.get()), float(entrada_x1.get())

                f = lambda x: eval(expresiones[0], {"x": x, "math": math, "sin": math.sin, "cos": math.cos, "exp": math.exp})

                fig, ax = plt.subplots(figsize=(10, 4), facecolor='#0F0A16')
                ax.xaxis.set_major_locator(MaxNLocator(nbins=10))  # Muestra hasta 10 valores
                ax.set_facecolor('#0F0A16')
                x_vals = np.linspace(lim_inf_x,lim_sup_x, 400)
                y_vals = [f(x) for x in x_vals]
                ax.plot(x_vals, y_vals, label="f(x)", color="#00ffcc")
                ax.axhline(0, color='#7BFFF8', linewidth=0.8)
                ax.axvline(0, color='#7BFFF8', linewidth=0.8)

                
                ax.xaxis.set_major_locator(MaxNLocator(nbins=10))
                ax.set_xlim(lim_inf_x, lim_sup_x)
                ax.set_ylim(lim_inf_y,lim_sup_y)

                ax.tick_params(colors='#7BFFF8')
                ax.spines['bottom'].set_color('#7BFFF8')
                ax.spines['top'].set_color('#7BFFF8')
                ax.spines['right'].set_color('#7BFFF8')
                ax.spines['left'].set_color('#7BFFF8')
                ax.yaxis.label.set_color('white')
                ax.xaxis.label.set_color('white')
                ax.title.set_color('#7BFFF8')

                ax.set_title("Gráfica de f(x) con raíz")
                ax.grid(True, color="#444444")
                ax.legend(facecolor="#333333", edgecolor="white", labelcolor="white")
                


                # Eliminar solo el canvas anterior, si existe
                for widget in frame_graficadora.winfo_children():
                    widget.destroy()

                """"ANTES
                #canvas = FigureCanvasTkAgg(fig, master=frame_graficadora)
                #canvas.draw()
                #canvas.get_tk_widget().pack(pady=1)
                """""
                canvas = FigureCanvasTkAgg(fig, master=frame_graficadora)
                canvas.draw()
                canvas_widget = canvas.get_tk_widget()
                canvas_widget.pack(side="top", fill="both", expand=True)

                # Agregar barra de navegación
                toolbar = NavigationToolbar2Tk(canvas, frame_graficadora)
                toolbar.update()
                toolbar.pack(side=tk.TOP, fill=tk.X)


        ###METODOS DE SISTEMAS LINEALES

        elif metodo_seleccionado in ["Jacobi", "Gauss-Seidel"]:
            A = np.array(eval(entrada_fun1.get()))
            b = np.array(eval(entrada_fun2.get()))
            if metodo_seleccionado == "Jacobi":
                x, iters, hist = jacobi(A, b, tol=tol, max_iter=iter_max)
            else:
                x, iters, hist = gauss_seidel(A, b, tol=tol, max_iter=iter_max)
            raiz = x
            nombres = [f"x{i+1}" for i in range(len(x))]
            sol_text = ", ".join(f"{n}={val:.6f}" for n, val in zip(nombres, x))
            label_raiz.config(text=f"Vector solución:\n{sol_text}")

        elif metodo_seleccionado == "Gauss-Jordan":
            A = np.array(eval(entrada_fun1.get()))
            b = np.array(eval(entrada_fun2.get()))
            x = gauss_jordan(A, b)
            raiz = x
            iters = "-"
            hist = []
            nombres = [f"x{i+1}" for i in range(len(x))]
            sol_text = ", ".join(f"{n}={val:.6f}" for n, val in zip(nombres, x))
            label_raiz.config(text=f"Vector solución:\n{sol_text}")


#######METODOS DE INTEGRACION
        elif metodo_seleccionado in ["Trapecio", "Simpson"]:
            try:
                f = lambda x: eval(expresiones[0], {"x": x, "math": math, "sin": math.sin, "cos": math.cos, "exp": math.exp})
                a = float(entrada_a.get().replace(",", "."))  # reemplaza coma por punto
                b_ = float(entrada_b.get().replace(",", "."))
                n = int(entrada_x0.get())
            except ValueError:
                messagebox.showerror("Error", "Por favor ingrese valores numéricos válidos (a, b y n).")
                return

            if metodo_seleccionado == "Trapecio":
                resultado = regla_trapecio(f, a, b_, n)
                raiz = resultado
                iters = "-"
                hist = []
                resultado_str = f"Área aproximada por el método del trapecio: {resultado:.6f}"
                label_raiz.config(text=f"Área aproximada por el método del trapecio: {resultado:.6f}")
                print(resultado_str)
            elif metodo_seleccionado == "Simpson":
                if n % 2 != 0:
                    messagebox.showerror("Error", "Para Simpson, el número de subintervalos (n) debe ser par.")
                    return
                resultado = regla_simpson(f, a, b_, n)
                raiz = resultado
                iters = "-"
                hist = []
                resultado_str = f"Área aproximada por el método de Simpson: {resultado:.6f}"
                label_raiz.config(text=f"Área aproximada por el método de Simpson: {resultado:.6f}")
                print(resultado_str)


        else:
            raise ValueError("Método no soportado")

        label_iters.config(text=f"Iteraciones: {iters}")

        ####MOSTRAR HISTORIAL
        if metodo_seleccionado in ["Jacobi", "Gauss-Seidel"]:
            # Historial de vectores
            cols = len(hist[0]) if hist else len(raiz)
            cabecera = "Iter | " + " | ".join([f"x{i+1}" for i in range(cols)])
            line = "-" * (7 + 12 * cols)
            historial_str = cabecera + "\n" + line + "\n"
            for idx, vec in enumerate(hist):
                vals = " | ".join(f"{v:>10.6f}" for v in vec)
                historial_str += f"{idx+1:>4} | {vals}\n"
        elif metodo_seleccionado=="Gauss-Jordan":
            label_iters.config(text="")
            label_historial.config(text="")
            historial_str = ""
        elif metodo_seleccionado=="Graficar":
            historial_str=""


        else:
            # Historial de métodos escalares (bisección, secante...)
            historial_str = "Iter |    a     |    b     |    c     |  f(c)\n"
            historial_str += "-" * 45 + "\n"
            for paso in hist:
                i, a_val, b_val, c_val, fc_val = paso
                historial_str += f"{i:>4} | {a_val:>7.5f} | {b_val:>7.5f} | {c_val:>7.5f} | {fc_val:>7.5f}\n"

        text_hist.delete("1.0", END)
        text_hist.insert("1.0", historial_str)

        

    except Exception as e:
        from tkinter import messagebox
        messagebox.showerror("Error", str(e))        



#####FRAME PARA Botones Calcular y limpiar
frame_calc_limp=tb.Frame(frame_izquierda,padding=(105,50,105,50))
frame_calc_limp.grid(row=2)
    ##boton Calcular
tb.Button(frame_calc_limp, text="CALCULAR", width=30, command=calcular_resultado).pack(padx=50, side="left")
    ##boton limpiar
tb.Button(frame_calc_limp,text="LIMPIAR",width=30,command=limpiar_entradas_resultados).pack(padx=50,side="left")
## FUNCION PARA LIMPIAR ENTRADAS Y RESULTADOS



frame_resultados = tb.Frame(frame_derecha_inferior, bootstyle="light", style="Custom.TLabelframe",padding=(10,35,10,40))
frame_resultados.pack(pady=0,fill="both")

# Labels de resultados

fuente_negrita = font.Font(family="Segoe UI", size=13, weight="bold")

label_raiz = tb.Label(frame_resultados, text="Solución: ", width=95, font=fuente_negrita)
label_raiz.pack(pady=5, padx=10)


label_iters = tb.Label(frame_resultados, text="", width=95, font=fuente_negrita)
label_iters.pack(pady=(0,0), padx=10)

label_historial = tb.Label(frame_resultados, text="Historial ", font=fuente_negrita)
label_historial.pack(pady=(0,0),padx=10, side="left")

# Frame para historial con scrollbar
frame_hist = tb.Frame(frame_resultados)
frame_hist.pack(padx=10, pady=(15,0), fill="y", expand=True,side="left")

scrollbar = Scrollbar(frame_hist)
scrollbar.pack(side=RIGHT, fill=Y)

text_hist = Text(frame_hist, font=("Courier", 10), wrap="none", yscrollcommand=scrollbar.set, height=8)
text_hist.pack(fill="y")
scrollbar.config(command=text_hist.yview)





def mostrar_campos_para_metodo(metodo): ###ocultar campos que no se necesitan
    # Ocultar todas las entradas
    global metodo_seleccionado
    metodo_seleccionado = metodo
    entradas = [entrada_fun1, entrada_fun2,entrada_fun3,entrada_fun4,entrada_fun5,entrada_fun6, entrada_a, entrada_b, entrada_x0, entrada_x1, entrada_tol, entrada_max_iter]
    for e in entradas:
        e.config(state='disabled')
        e.delete(0, 'end')
        e.config(bootstyle="default")
    # Mostrar solo los que necesita ese método
    if metodo == "Biseccion":
        if (ventana.style.theme_use()!="solar"):
            entrada_fun1.config(state='normal',bootstyle="light")
            entrada_a.config(state='normal',bootstyle="light")
            entrada_b.config(state='normal',bootstyle="light")
            entrada_tol.config(state='normal',bootstyle="light")
            entrada_max_iter.config(state='normal',bootstyle="light")
            label_a.config(text="A")
            label_b.config(text="B")
            label_x0.config(text="x0")
            label_x1.config(text="x1")
            label_fun1.config(text="f(x)")
            label_fun2.config(text="")  
        else:
            entrada_fun1.config(state='normal',bootstyle="primary")
            entrada_a.config(state='normal',bootstyle="primary")
            entrada_b.config(state='normal',bootstyle="primary")
            entrada_tol.config(state='normal',bootstyle="primary")
            entrada_max_iter.config(state='normal',bootstyle="primary")
            label_a.config(text="A")
            label_b.config(text="B")
            label_x0.config(text="x0")
            label_x1.config(text="x1")
            label_fun1.config(text="f(x)")
            label_fun2.config(text="")  

    elif metodo == "Newton":
        if (ventana.style.theme_use()!="solar"):
            entrada_fun1.config(state='normal',bootstyle="light")
            entrada_fun2.config(state='normal',bootstyle="light")
            entrada_x0.config(state='normal',bootstyle="light")
            entrada_tol.config(state='normal',bootstyle="light")
            entrada_max_iter.config(state='normal',bootstyle="light")
            label_a.config(text="A")
            label_b.config(text="B")
            label_x0.config(text="x0")
            label_x1.config(text="x1")
            label_fun1.config(text="f(x)")
            label_fun2.config(text="f' (x)")  

        else:
            entrada_fun1.config(state='normal',bootstyle="primary")
            entrada_fun2.config(state='normal',bootstyle="primary")
            entrada_x0.config(state='normal',bootstyle="primary")
            entrada_tol.config(state='normal',bootstyle="primary")
            entrada_max_iter.config(state='normal',bootstyle="primary")
            label_a.config(text="A")
            label_b.config(text="B")
            label_x0.config(text="x0")
            label_x1.config(text="x1")
            label_fun1.config(text="f(x)")
            label_fun2.config(text="f' (x)")


    elif metodo == "Regula Falsi":
        if (ventana.style.theme_use()!="solar" ):
            entrada_fun1.config(state='normal',bootstyle="light")
            entrada_a.config(state='normal',bootstyle="light")
            entrada_b.config(state='normal',bootstyle="light")
            entrada_tol.config(state='normal',bootstyle="light")
            entrada_max_iter.config(state='normal',bootstyle="light")
            label_a.config(text="A")
            label_b.config(text="B")
            label_x0.config(text="x0")
            label_x1.config(text="x1")
            label_fun1.config(text="f(x)")
            label_fun2.config(text="")  
        else:
            entrada_fun1.config(state='normal',bootstyle="primary")
            entrada_a.config(state='normal',bootstyle="primary")
            entrada_b.config(state='normal',bootstyle="primary")
            entrada_tol.config(state='normal',bootstyle="primary")
            entrada_max_iter.config(state='normal',bootstyle="primary")
            label_a.config(text="A")
            label_b.config(text="B")
            label_x0.config(text="x0")
            label_x1.config(text="x1")
            label_fun1.config(text="f(x)")
            label_fun2.config(text="")
            
    elif metodo == "Jacobi" or metodo=="Gauss-Seidel":
        if (ventana.style.theme_use()!="solar"):
            entrada_fun1.config(state='normal',bootstyle="light")  
            entrada_fun2.config(state='normal',bootstyle="light")  
            entrada_max_iter.config(state='normal',bootstyle="light")
            entrada_tol.config(state='normal',bootstyle="light")
            label_a.config(text="A")
            label_b.config(text="B")
            label_x0.config(text="x0")
            label_x1.config(text="x1")
            label_fun1.config(text="A")
            label_fun2.config(text="B")        
        else:
            entrada_fun1.config(state='normal',bootstyle="primary")  
            entrada_fun2.config(state='normal',bootstyle="primary")  
            entrada_max_iter.config(state='normal',bootstyle="primary")
            entrada_tol.config(state='normal',bootstyle="primary")
            label_a.config(text="A")
            label_b.config(text="B")
            label_x0.config(text="x0")
            label_x1.config(text="x1")
            label_fun1.config(text="A")
            label_fun2.config(text="B")

    elif metodo == "Gauss-Jordan":
        if (ventana.style.theme_use()!="solar" ):
            entrada_fun1.config(state='normal',bootstyle="light")  
            entrada_fun2.config(state='normal',bootstyle="light")  
            label_a.config(text="A")
            label_b.config(text="B")
            label_x0.config(text="x0")
            label_x1.config(text="x1")
            label_fun1.config(text="A")
            label_fun2.config(text="B")
        else:      
            entrada_fun1.config(state='normal',bootstyle="primary")  
            entrada_fun2.config(state='normal',bootstyle="primary")  
            label_a.config(text="A")
            label_b.config(text="B")
            label_x0.config(text="x0")
            label_x1.config(text="x1")
            label_fun1.config(text="A")
            label_fun2.config(text="B")
    elif metodo=="Secante":
        if (ventana.style.theme_use()!="solar"):
            entrada_fun1.config(state="normal",bootstyle="light")
            entrada_x0.config(state="normal",bootstyle="light")
            entrada_x1.config(state="normal",bootstyle="light")
            entrada_tol.config(state="normal",bootstyle="light")
            entrada_max_iter.config(state="normal",bootstyle="light")
            label_a.config(text="A")
            label_b.config(text="B")
            label_x0.config(text="x0")
            label_x1.config(text="x1")
            label_fun1.config(text="f(x)")
            label_fun2.config(text="")          
        else:
            entrada_fun1.config(state="normal",bootstyle="primary")
            entrada_x0.config(state="normal",bootstyle="primary")
            entrada_x1.config(state="normal",bootstyle="primary")
            entrada_tol.config(state="normal",bootstyle="primary")
            entrada_max_iter.config(state="normal",bootstyle="primary")
            label_a.config(text="A")
            label_b.config(text="B")
            label_x0.config(text="x0")
            label_x1.config(text="x1")  
            label_fun1.config(text="f(x)")
            label_fun2.config(text="")  

    elif metodo=="Trapecio":
        if (ventana.style.theme_use()!="solar"):
            entrada_fun1.config(state='normal',bootstyle="light") 
            entrada_a.config(state='normal',bootstyle="light")
            entrada_b.config(state='normal',bootstyle="light")
            entrada_x0.config(state="normal",bootstyle="light")
            label_x0.config(text="n")
            label_a.config(text="A")
            label_b.config(text="B")
            label_x1.config(text="")       
            label_fun1.config(text="f(x)")
            label_fun2.config(text="")  

        else:
            entrada_fun1.config(state='normal',bootstyle="primary")
            entrada_a.config(state='normal',bootstyle="primary")
            entrada_b.config(state='normal',bootstyle="primary")
            entrada_x0.config(state="normal",bootstyle="primary")
            label_x0.config(text="n")
            label_a.config(text="A")
            label_b.config(text="B")
            label_x1.config(text="")       
            label_fun1.config(text="f(x)")
            label_fun2.config(text="")  

    elif metodo=="Simpson":
        if (ventana.style.theme_use()!="solar"):
            entrada_fun1.config(state='normal',bootstyle="light") 
            entrada_a.config(state='normal',bootstyle="light")
            entrada_b.config(state='normal',bootstyle="light")
            entrada_x0.config(state="normal",bootstyle="light")
            label_x0.config(text="n")
            label_a.config(text="A")
            label_b.config(text="B")
            label_x1.config(text="")       
            label_fun1.config(text="f(x)")
            label_fun2.config(text="")  

        else:
            entrada_fun1.config(state='normal',bootstyle="primary")
            entrada_a.config(state='normal',bootstyle="primary")
            entrada_b.config(state='normal',bootstyle="primary")
            entrada_x0.config(state="normal",bootstyle="primary")
            label_x0.config(text="n")
            label_a.config(text="A")
            label_b.config(text="B")
            label_x1.config(text="")       
            label_fun1.config(text="f(x)")
            label_fun2.config(text="")
    else:
        if (ventana.style.theme_use()!="solar"):
            entrada_fun1.config(state='normal',bootstyle="light") 
            entrada_a.config(state='normal',bootstyle="light")
            entrada_b.config(state='normal',bootstyle="light")
            entrada_x0.config(state="normal",bootstyle="light")
            entrada_x1.config(state="normal",bootstyle="light")
            label_a.config(text="x0")
            label_b.config(text="x1")
            label_x0.config(text="y0")
            label_x1.config(text="y1")
            label_fun1.config(text="f(x)")
            label_fun2.config(text="")  

        else:
            entrada_fun1.config(state='normal',bootstyle="primary")
            entrada_a.config(state='normal',bootstyle="primary")
            entrada_b.config(state='normal',bootstyle="primary")
            entrada_x0.config(state="normal",bootstyle="primary")
            entrada_x1.config(state="normal",bootstyle="primary")
            label_a.config(text="x0")
            label_b.config(text="x1")
            label_x0.config(text="y0")
            label_x1.config(text="y1")       
            label_fun1.config(text="f(x)")
            label_fun2.config(text="")  

        



ventana.mainloop()
