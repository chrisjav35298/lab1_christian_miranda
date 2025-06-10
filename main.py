from os import path
from domain.dataset_csv import DatasetCSV
from domain.dataset_excel import DatasetEXCEL
from data.data_saver import DataSaver

csv_path = path.join(path.dirname(__file__), "files/snic-provincias.csv")
excel_path = path.join(path.dirname(__file__), "files/hechos.xlsx")

csv = DatasetCSV(csv_path)
csv.cargar_datos()

excel = DatasetEXCEL(excel_path)
excel.cargar_datos()

#gurdado en base de datos
db = DataSaver()
db.guardar_dataframe(csv.datos, "snic")  #poner el nombre de la tabla
db.guardar_dataframe(excel.datos, "hechos") 

