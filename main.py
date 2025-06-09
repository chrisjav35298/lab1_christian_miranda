from os import path
from domain.dataset_csv import DatasetCSV
from domain.dataset_excel import DatasetEXCEL

csv_path = path.join(path.dirname(__file__), "files/netbook_01.csv")
excel_path = path.join(path.dirname(__file__), "files/reparacion_01.xlsx")

csv = DatasetCSV(csv_path)
csv.cargar_datos()


# excel = DatasetEXCEL(excel_path)
# excel.cargar_datos()
