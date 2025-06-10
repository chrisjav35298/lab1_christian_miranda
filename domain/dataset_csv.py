import pandas as pd
from domain.dataset import Dataset
from datetime import datetime


class DatasetCSV(Dataset):
    def __init__(self, fuente):
        super().__init__(fuente)

    def cargar_datos(self):
        try:
            df = pd.read_csv(self.fuente)
            self.datos = df
            print("CSV cargado.")
            if self.validar_datos():
                if not self.control_fecha():
                    return
                self.transformar_datos()
                self.mostrar_resumen()


        except Exception as e:
            print(f"Error cargando CSV: {e}")


    def control_fecha(self) -> bool:
        if self.datos is None:
            print("Error: los datos no han sido cargados.")
            return False

        df = self.datos
        actual = datetime.now().year
        mayor_actual = df['anio'] > actual
        if mayor_actual.any():
            valores = df.loc[mayor_actual, 'anio'].unique()
            print(f"Error: estos años son mayores al año actual ({actual}): {valores}")
            return False
        return True