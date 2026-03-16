import contextlib
import sqlite3
import pandas as pd
from pathlib import Path

class DatabaseManager:
    """Capa de Acceso a Datos (Data Layer). Cumple con el Principio de Responsabilidad Única."""
    
    def __init__(self, db_filename: str = "healthcare_warehouse.db"):
        root_dir = Path(__file__).parent.parent
        self.db_path = root_dir / "data" / db_filename
        
        if not self.db_path.exists():
            raise FileNotFoundError(f"❌ Error Crítico: No se encontró la base de datos en la ruta:\n{self.db_path}\n"
                                    f"Por favor, asegúrate de colocar el archivo .db en la carpeta /data.")

    def get_all_records(self) -> pd.DataFrame:
        """Extrae los registros, aplica transformaciones iniciales y devuelve un DataFrame listo para analizar."""
        with contextlib.closing(sqlite3.connect(self.db_path)) as conn:
            df = pd.read_sql_query("SELECT * FROM hospital_records", conn)
        df['Date of Admission'] = pd.to_datetime(df['Date of Admission'])
        df['Mes_Anio'] = df['Date of Admission'].dt.to_period('M').astype(str)
        return df