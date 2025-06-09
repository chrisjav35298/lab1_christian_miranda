import pandas as pd
from domain.dataset import Dataset


class DatasetEXCEL(Dataset):
    def __init(self, fuente):
        super().__init__(fuente)

    def cargar_datos(self):
        try:
            df = pd.read_excel(self.fuente)
            self.datos = df
            print("EXCEL cargado.")
            if self.validar_datos():
                print("Datos validados.")
                # self.transformar_datos()


        except Exception as e:
            print(f"Error cargando EXCEL: {e}")