import math
from tkinter import messagebox
import ttkbootstrap as tb
from tkinter import font
import math
import numpy as np
from metodosnumericos.bisection import bisection
from metodosnumericos.newton import newton
from metodosnumericos.secant import secant
from metodosnumericos.gauss_jordan import gauss_jordan
from metodosnumericos.regula_falsi import regula_falsi 
from metodosnumericos.jacobi import jacobi


metodo_seleccionado = None

    
ventana=tb.Window(themename="vapor")
ventana.geometry("1200x900")
##Marco de titulo
Frame_titulo =tb.Frame(ventana,height=220)
Frame_titulo.pack(pady=30,fill="x")
label_titulo=tb.Label(Frame_titulo,text="Raíces y Soluciones",bootstyle="default",font=("Segoe UI",27,"bold"))
label_titulo.pack()

## Marco Principal de entradas
# Definir fuente personalizada
fuente_titulo = font.Font(family="Segoe UI", size=25, weight="bold")

# Crear un estilo nuevo para Labelframe
style = tb.Style()
style.configure("Custom.TLabelframe", font=fuente_titulo)
###Marco de Parámetros


##Marco de Metodos
frame_metodos=tb.LabelFrame(ventana,bootstyle="dark",text="SELECCIONA EL MÉTODO NUMÉRICO",style="Custom.TLabelframe")
frame_metodos.pack(pady=(10,10))


tb.Button(frame_metodos,width=60,text="Biseccion",bootstyle="default", command=lambda: mostrar_campos_para_metodo("Biseccion")).grid(row=1,column=0,pady=10,padx=20)
tb.Button(frame_metodos,width=60,text="Newton",bootstyle="warning", command=lambda: mostrar_campos_para_metodo("Newton")).grid(row=1,column=1, pady=10)
tb.Button(frame_metodos,width=60,text="Regula Falsi",bootstyle="info", command=lambda: mostrar_campos_para_metodo("Regula Falsi")).grid(row=2,column=0,padx=20,pady=10)
tb.Button(frame_metodos,width=60,text="Jacobi",bootstyle="secondary", command=lambda: mostrar_campos_para_metodo("Jacobi")).grid(row=2,column=1,padx=10,pady=(10))
tb.Button(frame_metodos,width=60,text="Secante",bootstyle="success", command=lambda: mostrar_campos_para_metodo("Secante")).grid(row=3,column=0,padx=20,pady=(10,20))
tb.Button(frame_metodos,width=60,text="Gauss-Jordan",bootstyle="danger", command=lambda: mostrar_campos_para_metodo("Gauss-Jordan")).grid(row=3,column=1,padx=10,pady=(10,20))

####### FRAME de DATOS DE ENTRADA
frame_Entrada=tb.LabelFrame(ventana,bootstyle="light",text="Datos de Entrada",style="Custom.TLabelframe",padding=(0,10,0,0,))
frame_Entrada.pack(pady=(10,10))
    ###Label de la funcion
tb.Label(frame_Entrada,font=("Segoe UI",14),text="f(x)").grid(row=0,column=0,padx=10)
entrada_fun1=tb.Entry(frame_Entrada,width=40)
entrada_fun1.grid(row=0,column=1,padx=10)

tb.Label(frame_Entrada,font=("Segoe UI",14)).grid(row=1,column=0,)
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
tb.Label(frame_Entrada,font=("Segoe UI",14),text="A").grid(row=0,column=3,padx=(10,10)) 
entrada_a=tb.Entry(frame_Entrada,width=20)
entrada_a.grid(row=0,column=4,padx=10)

tb.Label(frame_Entrada,font=("Segoe UI",14),text="B").grid(row=1,column=3,padx=(10,10))
entrada_b=tb.Entry(frame_Entrada,width=20)
entrada_b.grid(row=1,column=4,padx=(10))

tb.Label(frame_Entrada,font=("Segoe UI",14),text="X0").grid(row=2,column=3,padx=(10,10))
entrada_x0=tb.Entry(frame_Entrada,width=20)
entrada_x0.grid(row=2,column=4,padx=10)

tb.Label(frame_Entrada,font=("Segoe UI",14),text="X1").grid(row=3,column=3,padx=(10,10))
entrada_x1=tb.Entry(frame_Entrada,width=20)
entrada_x1.grid(row=3,column=4,padx=10)

tb.Label(frame_Entrada,font=("Segoe UI",14),text="Tol").grid(row=4,column=3,padx=(10,10))
entrada_tol=tb.Entry(frame_Entrada,width=20)
entrada_tol.grid(row=4,column=4,padx=10)

tb.Label(frame_Entrada,font=("Segoe UI",14),text="Iter").grid(row=5,column=3,padx=(10,10))
entrada_max_iter=tb.Entry(frame_Entrada,width=20)
entrada_max_iter.grid(row=5,column=4,padx=10)

####### labels invisibles para ordenar
tb.Label(frame_Entrada,font=("Segoe UI",14),width=15).grid(row=0,column=2,pady=0)
tb.Label(frame_Entrada,font=("Segoe UI",14),width=15).grid(row=1,column=2,pady=0)
tb.Label(frame_Entrada,font=("Segoe UI",14),width=15).grid(row=1,column=2,pady=0)
tb.Label(frame_Entrada,font=("Segoe UI",14),width=15).grid(row=2,column=2,pady=0)
tb.Label(frame_Entrada,font=("Segoe UI",14),width=15).grid(row=3,column=2,pady=0)
tb.Label(frame_Entrada,font=("Segoe UI",14),width=15).grid(row=4,column=2,pady=0)
tb.Label(frame_Entrada,font=("Segoe UI",14),width=15).grid(row=5,column=2,pady=0)
tb.Label(frame_Entrada,font=("Segoe UI",14),width=15).grid(row=6,column=2,pady=0)


            ####   METODOS Y FUNCIONES  ######
def limpiar_entradas():
    entradas = [
        entrada_fun1,entrada_fun2,entrada_fun3,entrada_fun4,entrada_fun5,entrada_fun6, entrada_a, entrada_b,
        entrada_x0, entrada_x1, entrada_tol, entrada_max_iter
    ]
    for e in entradas:
        e.delete(0, 'end')
        
def calcular_resultado():
    global metodo_seleccionado
    try:
        tol = float(entrada_tol.get())
        iter_max = int(entrada_max_iter.get())

        # Recolectar todas las entradas de funciones
        expresiones = [
            entrada_fun1.get(), entrada_fun2.get(), entrada_fun3.get(),
            entrada_fun4.get(), entrada_fun5.get(), entrada_fun6.get()
        ]
        expresiones = [expr.strip() for expr in expresiones if expr.strip() != ""]

        # Verificar que haya al menos una función ingresada
        if len(expresiones) == 0:
            raise ValueError("Debe ingresar al menos una función.")

        raiz = None
        iters = None
        hist = []

        # Métodos que requieren solo UNA función o sistema no lineal

        if metodo_seleccionado in ["Biseccion", "Regula Falsi", "Newton", "Secante"]:
            f = lambda x: eval(expresiones[0], {"x": x, "math": math, "sin": math.sin, "cos": math.cos, "exp": math.exp})
            print("Método seleccionado:", metodo_seleccionado)
            print("Función ingresada:", expresiones[0])
            if metodo_seleccionado == "Biseccion":
                a = float(entrada_a.get())
                b = float(entrada_b.get())
                if f(a) * f(b) >= 0:
                    raise ValueError("La función no cambia de signo en el intervalo [a, b].")
                raiz, iters, hist = bisection(f, a, b, tol, iter_max)

            elif metodo_seleccionado == "Regula Falsi":
                a = float(entrada_a.get())
                b = float(entrada_b.get())
                if f(a) * f(b) >= 0:
                    raise ValueError("La función no cambia de signo en el intervalo [a, b].")
                raiz, iters, hist = regula_falsi(f, a, b, tol, iter_max)

            elif metodo_seleccionado == "Newton":
                df = lambda x: eval(entrada_fun2.get(), {"x": x, "math": math, "sin": math.sin, "cos": math.cos, "exp": math.exp})
                x0 = float(entrada_x0.get())
                raiz, iters, hist = newton(f, df, x0, tol, iter_max)

            elif metodo_seleccionado == "Secante":
                x0 = float(entrada_x0.get())
                x1 = float(entrada_x1.get())
                raiz, iters, hist = secant(f, x0, x1, tol, iter_max)
            print("Resultado Bisección:")
            print("Raíz:", raiz)
            print("Iteraciones:", iters)
            print("Historial:", hist)


        # Métodos que resuelven sistemas lineales (Jacobi, Gauss-Jordan, etc.)
        elif metodo_seleccionado in ["Jacobi", "Gauss-Jordan", "Gauss-Seidel"]:
            if len(expresiones) < 2:
                raise ValueError("Debe ingresar una matriz A y un vector b.")

            A = np.array(eval(expresiones[0]))
            b = np.array(eval(expresiones[1]))

            if metodo_seleccionado == "Jacobi":
                x, iters, hist = jacobi(A, b, tol=tol, max_iter=iter_max)
                raiz = x

            elif metodo_seleccionado == "Gauss-Jordan":
                x = gauss_jordan(A, b)
                raiz = x
                iters = "-"
                hist = []

        # Mostrar resultados
        label_raiz.config(text=f"Raíz encontrada: {raiz}")
        label_iters.config(text=f"Iteraciones: {iters}")

        # Mostrar el historial en formato tabular
        historial_str = "Iter |    a     |    b     |    c     |  f(c)\n"
        historial_str += "-" * 45 + "\n"
        for paso in hist:
            iteracion, a_val, b_val, c_val, fc_val = paso
            historial_str += f"{iteracion:>4} | {a_val:>7.5f} | {b_val:>7.5f} | {c_val:>7.5f} | {fc_val:>7.5f}\n"
        
        # Actualizar el label de historial
        label_hist.config(text=historial_str)   

    except Exception as e:
        label_raiz.config(text="Raíz encontrada: ---")
        label_iters.config(text="Iteraciones: ---")
        label_hist.config(text="Historial:\n---")
        messagebox.showerror("Error", str(e))

#####FRAME PARA Botones Calcular y limpiar
frame_calc_limp=tb.Frame(ventana,width=1050)
frame_calc_limp.pack(pady=20)
    ##boton Calcular
tb.Button(frame_calc_limp, text="CALCULAR", width=30, command=calcular_resultado).pack(padx=50, side="left")
    ##boton limpiar
tb.Button(frame_calc_limp,text="LIMPIAR",width=30,command=limpiar_entradas).pack(padx=50,side="left")
## FUNCION PARA LIMPIAR ENTRADAS Y RESULTADOS


###Marco de Resultados

frame_resultados=tb.LabelFrame(ventana,bootstyle="light",width=1050,height=200,text="RESULTADOS",style="Custom.TLabelframe")
frame_resultados.pack(pady=(10,10),fill="y",expand=True)

    ###Labels de Resultados
label_raiz = tb.Label(frame_resultados, text="Raíz encontrada: ", width=95, font=("Segoe UI",12))
label_raiz.pack(pady=5, padx=10)

label_iters = tb.Label(frame_resultados, text="Iteraciones: ", width=95, font=("Segoe UI",12))
label_iters.pack(pady=5, padx=10)

tb.Label(frame_resultados,text="Historial: ", width=95, font=("Segoe UI",12)).pack(pady=10,padx=10)

label_hist = tb.Label(frame_resultados, width=95,font=("Courier", 10), anchor="w", justify="left")
label_hist.pack(pady=2, padx=10,fill="y", expand=True)

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
        entrada_fun1.config(state='normal',bootstyle="light")
        entrada_a.config(state='normal',bootstyle="light")
        entrada_b.config(state='normal',bootstyle="light")
        entrada_tol.config(state='normal',bootstyle="light")
        entrada_max_iter.config(state='normal',bootstyle="light")

    elif metodo == "Newton":
        entrada_fun1.config(state='normal',bootstyle="light")
        entrada_fun2.config(state='normal',bootstyle="light")
        entrada_fun3.config(state='normal',bootstyle="light")
        entrada_fun4.config(state='normal',bootstyle="light")
        entrada_fun5.config(state='normal',bootstyle="light")
        entrada_fun6.config(state='normal',bootstyle="light")
        entrada_x0.config(state='normal',bootstyle="light")
        entrada_tol.config(state='normal',bootstyle="light")
        entrada_max_iter.config(state='normal',bootstyle="light")

    elif metodo == "Regula Falsi":
        entrada_fun1.config(state='normal',bootstyle="light")
        entrada_a.config(state='normal',bootstyle="light")
        entrada_b.config(state='normal',bootstyle="light")
        entrada_tol.config(state='normal',bootstyle="light")
        entrada_max_iter.config(state='normal',bootstyle="light")

    elif metodo == "Jacobi" or metodo == "Gauss-Seidel" or metodo == "Gauss-Jordan":
        entrada_fun1.config(state='normal',bootstyle="light")  
        entrada_fun2.config(state='normal',bootstyle="light")  
        entrada_fun3.config(state='normal',bootstyle="light")  
        entrada_fun4.config(state='normal',bootstyle="light")  
        entrada_fun5.config(state='normal',bootstyle="light")  
        entrada_fun6.config(state='normal',bootstyle="light")  
        entrada_max_iter.config(state='normal',bootstyle="light")
        entrada_tol.config(state='normal',bootstyle="light")
        entrada_a.config(state='normal',bootstyle="light")  
        entrada_b.config(state='normal',bootstyle="light") 

    elif metodo=="Secante":
        entrada_fun1.config(state="normal",bootstyle="light")
        entrada_x0.config(state="normal",bootstyle="light")
        entrada_x1.config(state="normal",bootstyle="light")
        entrada_tol.config(state="normal",bootstyle="light")
        entrada_max_iter.config(state="normal",bootstyle="light")


"""
Raíces Encontrdas: 
Iteraciones:
calculos realizados:
Historial:
"""
ventana.mainloop()
