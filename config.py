from zoneinfo import ZoneInfo
from datetime import time

FUSO_HORARIO = ZoneInfo("America/Fortaleza")

TOLERANCIA_MINUTOS = 5

HORARIOS_PADRAO = {
    "Entrada": time(7, 30, 0),
    "Saída Almoço": time(11, 30, 0),
    "Retorno Almoço": time(12, 30, 0),
    "Saída": time(17, 30, 0)
}

HORARIOS_FILIAL2 = {
    "Entrada": time(8, 0, 0),
    "Saída Almoço": time(11, 0, 0),
    "Retorno Almoço": time(12, 0, 0),
    "Saída": time(18, 0, 0)
}
