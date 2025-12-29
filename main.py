#pip install -r requied.txt

#import pandas as pd
#import numpy as np
#from sklearn.preprocessing import MinMaxScaler
#from statsmodels.tsa.seasonal import STL
#from typing import List, Dict
#import torch
#import torch.nn as nn
#from typing import Tuple


CSV_PATH = "canarias_turismo_2015_2025.csv"

#Procesamiento de Datos
#Cargar archivos del CSV (Hay qe tener en cuenta que tiene dos columnas de texto, una la isla(F) y el otro el pais mas comun que visita cada isla(I))
def load_and_clean_data(path: str = CSV_PATH) -> pd.DataFrame:
    
    df = pd.read_csv(
        path,
        parse_dates=["week_start_date"],
        dayfirst=True
    )

    # Así cada isla queda ordenada cronológicamente.
    df.sort_values(
        by=["island_code", "week_start_date"],
        inplace=True
    )

    df.reset_index(drop=True, inplace=True)
    return df

# Normalizar columnas numéricas
def normalize_time_series(df: pd.DataFrame, cols: List[str]) -> pd.DataFrame:
    scaler = MinMaxScaler()
    df[cols] = scaler.fit_transform(df[cols])
    return df
# Devuelve el DataFrame con las columnas normalizadas.

def seasonal_decompose(
    df: pd.DataFrame,
    target_col: str,
    period: int = 52
) -> Dict[str, STL]:
    results = {}
  
# Crear la serie temporal (filtrar limpiar datos)
    for island in df["island_name"].unique():
        ts = (
            df[df["island_name"] == island]
            .set_index("week_start_date")[target_col]
            .dropna()
        )
  # Para evitar errores y verificar cantidad de datos
        if len(ts) < period * 2:
          
            continue
# Guarda el resultado por isla
        stl = STL(ts, period=period, robust=True)
        results[island] = stl.fit()
      
# Devielve diccionario por isla
    return results

# Modelo generativo
   # Inicializa nn.Module
class LSTMTrendModel(nn.Module):
  
    def __init__(
        self,
        input_size: int,
        hidden_size: int = 64,
        num_layers: int = 2
    ):
        super().__init__()
      
# Define Long Short-Term Memory
        self.lstm = nn.LSTM(
            input_size=input_size,
            hidden_size=hidden_size,
            num_layers=num_layers,
            batch_first=True
        )
# Convierte la salida de la LSTM en un valor final
# Entrada: hidden_size
      
        self.fc = nn.Linear(hidden_size, 1)
# Método forward
  # out:Salidas para todos los timesteps
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        out, _ = self.lstm(x)
        out = out[:, -1, :]  
      #Pasa el estado final por la capa lineal
        return self.fc(out)
