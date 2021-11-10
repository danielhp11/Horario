from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import OneLineListItem
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivymd.uix.datatables import MDDataTable
import sqlite3
from datetime import date

class Lunes(Screen):
    layout = None
    btn = None

    def __init__(self, **kwargs):#metodo sobre escrito de la clase padre
        super(Lunes,self).__init__(**kwargs)#agrega una cadena de caracteres a la aplicacion para su manipulacion
        self.tablaHorario()

    def tablaHorario(self):
        self.layout = AnchorLayout()
        today = str(date.today())
        self.layout.anchor_x = "center"
        self.layout.anchor_y = "center"
        con = sqlite3.connect('Horario.sqlite')
        cur = con.cursor()
        cur.execute("SELECT R1.hora,R2.maestro,R2.materia,R2.salon FROM(SELECT hora,id_materia,Fecha_inicio,fecha_fin,dia from Materia)R1 LEFT JOIN (SELECT maestro,salon,materia,id_materia from Materia)R2 on R1.id_materia == R2.id_materia WHERE '"+today+"'>R1.Fecha_inicio and  '"+today+"' < fecha_fin AND R1.Dia == 'Lunes'")
        compra = cur.fetchall()
        data_tables = MDDataTable(#se asigana la tabla a la variable
            size_hint=(0.9, 0.6),#tamañp de la tabla
            column_data=[#columnas de titulos
                ("Hora Lunes", dp(25)),
                ("Maestro", dp(40)),
                ("Materia", dp(40)),
                ("Salon", dp(20)),],
            row_data=[ #contenido de la tabla por fila
               (compras) for compras in  compra
            ],
        )
        con.close()
        self.layout.add_widget(data_tables)
        self.add_widget(self.layout)
 
class Martes(Screen):
    layout = None
    btn = None

    def __init__(self, **kwargs):#metodo sobre escrito de la clase padre
        super(Martes,self).__init__(**kwargs)#agrega una cadena de caracteres a la aplicacion para su manipulacion
        self.tablaHorario()

    def tablaHorario(self):
        self.layout = AnchorLayout()
        today = str(date.today())
        self.layout.anchor_x = "center"
        self.layout.anchor_y = "center"
        con = sqlite3.connect('Horario.sqlite')
        cur = con.cursor()
        cur.execute("SELECT R1.hora,R2.maestro,R2.materia,R2.salon FROM(SELECT hora,id_materia,Fecha_inicio,fecha_fin,dia from Materia)R1 LEFT JOIN (SELECT maestro,salon,materia,id_materia from Materia)R2 on R1.id_materia == R2.id_materia WHERE '"+today+"'>R1.Fecha_inicio and  '"+today+"' < fecha_fin AND R1.Dia == 'Martes'")
        compra = cur.fetchall()
        data_tables = MDDataTable(#se asigana la tabla a la variable
            size_hint=(0.9, 0.6),#tamañp de la tabla
            column_data=[#columnas de titulos
                ("Hora Martes", dp(25)),
                ("Maestro", dp(40)),
                ("Materia", dp(40)),
                ("Salon", dp(20)),],
            row_data=[ #contenido de la tabla por fila
               (compras) for compras in  compra
            ],
        )
        con.close()
        self.layout.add_widget(data_tables)
        self.add_widget(self.layout)

class Miercoles(Screen):
    layout = None
    btn = None

    def __init__(self, **kwargs):#metodo sobre escrito de la clase padre
        super(Miercoles,self).__init__(**kwargs)#agrega una cadena de caracteres a la aplicacion para su manipulacion
        self.tablaHorario()

    def tablaHorario(self):
        self.layout = AnchorLayout()
        today = str(date.today())
        self.layout.anchor_x = "center"
        self.layout.anchor_y = "center"
        con = sqlite3.connect('Horario.sqlite')
        cur = con.cursor()
        cur.execute("SELECT R1.hora,R2.maestro,R2.materia,R2.salon FROM(SELECT hora,id_materia,Fecha_inicio,fecha_fin,dia from Materia)R1 LEFT JOIN (SELECT maestro,salon,materia,id_materia from Materia)R2 on R1.id_materia == R2.id_materia WHERE '"+today+"'>R1.Fecha_inicio and  '"+today+"' < fecha_fin AND R1.Dia == 'Miercoles'")
        compra = cur.fetchall()
        data_tables = MDDataTable(#se asigana la tabla a la variable
            size_hint=(0.9, 0.6),#tamañp de la tabla
            column_data=[#columnas de titulos
                ("Hora  Miercoles", dp(25)),
                ("Maestro", dp(40)),
                ("Materia", dp(40)),
                ("Salon", dp(20)),],
            row_data=[ #contenido de la tabla por fila
               (compras) for compras in  compra
            ],
        )
        con.close()
        self.layout.add_widget(data_tables)
        self.add_widget(self.layout)

class Jueves(Screen):
    layout = None
    btn = None

    def __init__(self, **kwargs):#metodo sobre escrito de la clase padre
        super(Jueves,self).__init__(**kwargs)#agrega una cadena de caracteres a la aplicacion para su manipulacion
        self.tablaHorario()

    def tablaHorario(self):
        self.layout = AnchorLayout()
        today = str(date.today())
        self.layout.anchor_x = "center"
        self.layout.anchor_y = "center"
        con = sqlite3.connect('Horario.sqlite')
        cur = con.cursor()
        cur.execute("SELECT R1.hora,R2.maestro,R2.materia,R2.salon FROM(SELECT hora,id_materia,Fecha_inicio,fecha_fin,dia from Materia)R1 LEFT JOIN (SELECT maestro,salon,materia,id_materia from Materia)R2 on R1.id_materia == R2.id_materia WHERE '"+today+"'>R1.Fecha_inicio and  '"+today+"' < fecha_fin AND R1.Dia == 'Jueves'")
        compra = cur.fetchall()
        data_tables = MDDataTable(#se asigana la tabla a la variable
            size_hint=(0.9, 0.6),#tamañp de la tabla
            column_data=[#columnas de titulos
                ("Hora Jueves", dp(25)),
                ("Maestro", dp(40)),
                ("Materia", dp(40)),
                ("Salon", dp(20)),],
            row_data=[ #contenido de la tabla por fila
               (compras) for compras in  compra
            ],
        )
        con.close()
        self.layout.add_widget(data_tables)
        self.add_widget(self.layout)

class Viernes(Screen):
    layout = None
    btn = None

    def __init__(self, **kwargs):#metodo sobre escrito de la clase padre
        super(Viernes,self).__init__(**kwargs)#agrega una cadena de caracteres a la aplicacion para su manipulacion
        self.tablaHorario()

    def tablaHorario(self):
        self.layout = AnchorLayout()
        today = str(date.today())
        self.layout.anchor_x = "center"
        self.layout.anchor_y = "center"
        con = sqlite3.connect('Horario.sqlite')
        cur = con.cursor()
        cur.execute("SELECT R1.hora,R2.maestro,R2.materia,R2.salon FROM(SELECT hora,id_materia,Fecha_inicio,fecha_fin,dia from Materia)R1 LEFT JOIN (SELECT maestro,salon,materia,id_materia from Materia)R2 on R1.id_materia == R2.id_materia WHERE '"+today+"'>R1.Fecha_inicio and  '"+today+"' < fecha_fin AND R1.Dia == 'Viernes'")
        compra = cur.fetchall()
        data_tables = MDDataTable(#se asigana la tabla a la variable
            size_hint=(0.9, 0.6),#tamañp de la tabla
            column_data=[#columnas de titulos
                ("Hora Viernes", dp(25)),
                ("Maestro", dp(40)),
                ("Materia", dp(40)),
                ("Salon", dp(20)),],
            row_data=[ #contenido de la tabla por fila
               (compras) for compras in  compra
            ],
        )
        con.close()
        self.layout.add_widget(data_tables)
        self.add_widget(self.layout)

class Sabado(Screen):
    layout = None
    btn = None

    def __init__(self, **kwargs):#metodo sobre escrito de la clase padre
        super(Sabado,self).__init__(**kwargs)#agrega una cadena de caracteres a la aplicacion para su manipulacion
        self.tablaHorario()

    def tablaHorario(self):
        self.layout = AnchorLayout()
        today = str(date.today())
        self.layout.anchor_x = "center"
        self.layout.anchor_y = "center"
        con = sqlite3.connect('Horario.sqlite')
        cur = con.cursor()
        cur.execute("SELECT R1.hora,R2.maestro,R2.materia,R2.salon FROM(SELECT hora,id_materia,Fecha_inicio,fecha_fin,dia from Materia)R1 LEFT JOIN (SELECT maestro,salon,materia,id_materia from Materia)R2 on R1.id_materia == R2.id_materia WHERE '"+today+"'>R1.Fecha_inicio and  '"+today+"' < fecha_fin AND R1.Dia == 'Sabado'")
        compra = cur.fetchall()
        data_tables = MDDataTable(#se asigana la tabla a la variable
            size_hint=(0.9, 0.6),#tamañp de la tabla
            column_data=[#columnas de titulos
                ("Hora Sabado", dp(25)),
                ("Maestro", dp(40)),
                ("Materia", dp(40)),
                ("Salon", dp(20)),],
            row_data=[ #contenido de la tabla por fila
               (compras) for compras in  compra
            ],
        )
        con.close()
        self.layout.add_widget(data_tables)
        self.add_widget(self.layout)

class Proyect1(MDApp):

    def build(self):
        self.title = "Horario" #Nombre de la aplicacion
        return Builder.load_file("main.kv")

Proyect1().run()