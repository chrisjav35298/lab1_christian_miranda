import pandas as pd
from domain.dataset import Dataset


class DatasetEXCEL(Dataset):
    def __init__(self, fuente):
        super().__init__(fuente)

    def cargar_datos(self):
        try:
            df = pd.read_excel(self.fuente)
            self.datos = df
            print("EXCEL cargado.")

            self.consolidar_datos()        
            if self.validar_datos():       
                self.transformar_datos()
                self.mostrar_resumen()


        except Exception as e:
            print(f"Error cargando EXCEL: {e}")
    
    #Rellenar con valores -9999.0, las celdas con nulos
    def consolidar_datos(self, coordenada_default: float = -9999.0):
        if self.datos is None:
            print("No hay datos para consolidar.")
            return False

        df = self.datos.copy()

        nulos_lat = 0
        nulos_lon = 0

        if 'latitud' in df.columns:
            df['latitud'] = pd.to_numeric(df['latitud'], errors='coerce') 
            nulos_lat = df['latitud'].isnull().sum()
            df['latitud'] = df['latitud'].fillna(coordenada_default)

        if 'longitud' in df.columns:
            df['longitud'] = pd.to_numeric(df['longitud'], errors='coerce')
            nulos_lon = df['longitud'].isnull().sum()
            df['longitud'] = df['longitud'].fillna(coordenada_default)

        self.datos = df

        print("Consolidación de datos completada.")
        print(f" - Latitud nula reemplazada: {nulos_lat}")
        print(f" - Longitud nula reemplazada: {nulos_lon}")
        return True