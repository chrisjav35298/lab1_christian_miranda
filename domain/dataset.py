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
            self.__datos = self.datos.drop_duplicates().copy()
            self.__datos.columns = self.__datos.columns.str.lower().str.replace(" ", "_")
            for col in self.__datos.select_dtypes(include="object").columns:
                self.__datos.loc[:, col] = self.__datos[col].astype(str).str.strip().replace("NULL", None)
            print("transformaciones ejecutadas.")
        else:
            print("no hay datos para transformar.")

    # def transformar_datos(self):
    #     if self.datos is not None:
    #         df = self.datos.copy()
    #         df.columns = df.columns.str.lower().str.replace(" ", "_")

    #         for col in df.select_dtypes(include="object").columns:
    #             df[col] = df[col].astype(str).str.strip().replace("NULL", None)

    #         df = df.drop_duplicates()

    #         self.datos = df  # Guardamos los cambios en la propiedad datos
    #         print("Transformaciones ejecutadas.")
    #     else:
    #         print("No hay datos para transformar.")



    def mostrar_resumen(self):
        return print(self.datos.describe(include='all') if self.datos is not None else "No hay Datos para mostrar")



