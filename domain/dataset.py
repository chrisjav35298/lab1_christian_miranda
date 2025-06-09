from abc import ABC, abstractmethod


class Dataset(ABC):
    def __init__(self, fuente):
        self.__fuente = fuente
        self.__datos = None

    @property
    def datos(self):
        return self.__datos
    
    @datos.setter
    def datos(self, value):
        self.__datos = value

    @property
    def fuente(self):
        return self.__fuente
    
    @abstractmethod
    def cargar_datos(self):
        pass 

    def validar_datos(self):
        if self.datos is None:
            raise ValueError("Datos no cargados")
        
        if self.datos.isnull().sum().sum() > 0:
            # cambiar por values para mostrar loe erores
            print("Se detectaron valores nulos.")
        if self.datos.duplicated().sum() > 0:
            print("Se detectaron filas duplicadas.")
        return True

    def transformar_datos(self):
        if self.datos is not None:
            self.__datos.columns = self.datos.columns.str.lower().str.replace(" ", "_")
            self.__datos = self.datos.drop_duplicates()
            # for col in self.datos.select_dtypes(include="object").columns:
            #     self.__datos[col] = self.datos[col].astype(str).str.strip()
            for col in self.__datos.select_dtypes(include="object").columns:
                self.__datos.loc[:, col] = self.__datos[col].astype(str).str.strip()

            print(f"transformaciones ejecutadas.")
        else:
            print(f"no hay datos para transformar.")

    def mostrar_datos(self):
        pass 



