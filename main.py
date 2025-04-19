import ttkbootstrap as tb
from tkinter import font
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


tb.Button(frame_metodos,width=60,text="BISECCION",bootstyle="default").grid(row=1,column=0,pady=10,padx=20)
tb.Button(frame_metodos,width=60,text="NEWTON",bootstyle="warning").grid(row=1,column=1, pady=10)
tb.Button(frame_metodos,width=60,text="REGULA FALSI",bootstyle="info").grid(row=2,column=0,padx=20,pady=10)
tb.Button(frame_metodos,width=60,text="JACOBI",bootstyle="secondary").grid(row=2,column=1,padx=10,pady=(10))
tb.Button(frame_metodos,width=60,text="SECANTE",bootstyle="success").grid(row=3,column=0,padx=20,pady=(10,20))
tb.Button(frame_metodos,width=60,text="GAUSS-JORDAN",bootstyle="danger").grid(row=3,column=1,padx=10,pady=(10,20))

####### FRAME de DATOS DE ENTRADA
frame_Entrada=tb.LabelFrame(ventana,bootstyle="light",text="Datos de Entrada",style="Custom.TLabelframe")
frame_Entrada.pack(pady=(10,10))
    ###Label de la funcion
tb.Label(frame_Entrada,font=("Segoe UI",14),text="f(x)").grid(row=0,column=0)
entrada_funcion=tb.Entry(frame_Entrada,width=40).grid(row=0,column=1,padx=10)
    
    ###Label de los parametros
tb.Label(frame_Entrada,font=("Segoe UI",14),text="A").grid(row=1,column=0)
entrada_a=tb.Entry(frame_Entrada,width=40).grid(row=1,column=1,padx=10)

tb.Label(frame_Entrada,font=("Segoe UI",14),text="B").grid(row=2,column=0)
entrada_b=tb.Entry(frame_Entrada,width=40).grid(row=2,column=1,padx=10)

tb.Label(frame_Entrada,font=("Segoe UI",14),text="X0").grid(row=3,column=0)
entrada_x0=tb.Entry(frame_Entrada,width=40).grid(row=3,column=1,padx=10)

tb.Label(frame_Entrada,font=("Segoe UI",14),text="X1").grid(row=4,column=0)
entrada_x1=tb.Entry(frame_Entrada,width=40).grid(row=4,column=1,padx=10)

tb.Label(frame_Entrada,font=("Segoe UI",14),text="X1").grid(row=1,column=2)
entrada_tol=tb.Entry(frame_Entrada,width=40).grid(row=1,column=3,padx=10)

tb.Label(frame_Entrada,font=("Segoe UI",14),text="X1").grid(row=2,column=2)
entrada_max_iter=tb.Entry(frame_Entrada,width=40).grid(row=2,column=3,padx=10)

tb.Label(frame_Entrada,font=("Segoe UI",14),text="X1").grid(row=0,column=2)
entrada_tol=tb.Entry(frame_Entrada,width=40).grid(row=0,column=3,padx=10)

tb.Label(frame_Entrada,font=("Segoe UI",14),text="X1").grid(row=3,column=2)
entrada_max_iter=tb.Entry(frame_Entrada,width=40).grid(row=3,column=3,padx=10)

tb.Label(frame_Entrada,font=("Segoe UI",14),text="X1").grid(row=4,column=2)
entrada_max_iter=tb.Entry(frame_Entrada,width=40).grid(row=4,column=3,padx=10)

#####FRAME PARA Botones Calcular y limpiar
frame_calc_limp=tb.Frame(ventana,width=1050)
frame_calc_limp.pack(pady=20)
    ##boton Calcular
tb.Button(frame_calc_limp,text="CALCULAR",width=30).pack(padx=50,side="left")
    ##boton limpiar
tb.Button(frame_calc_limp,text="LIMPIAR",width=30).pack(padx=50,side="left")

###Marco de Resultados

frame_resultados=tb.LabelFrame(ventana,bootstyle="light",width=1050,height=200,text="RESULTADOS",style="Custom.TLabelframe")
frame_resultados.pack(pady=(10,10))

    ###Labels de Resultados
tb.Label(frame_resultados,text="Raíces Encontradas: ",width=95,font=("Segoe UI",12)).pack(pady=10,padx=10)

tb.Label(frame_resultados,text="Iteraciones: ",width=95,font=("Segoe UI",12)).pack(pady=10,padx=10)

tb.Label(frame_resultados,text="Historial: ",width=95,font=("Segoe UI",12)).pack(pady=10,padx=10)




ventana.mainloop()
