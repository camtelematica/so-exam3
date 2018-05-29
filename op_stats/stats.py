import psutil

class Stats():

  @classmethod
  def obtener_disponible_cpu(cls):
    porcentaje = psutil.cpu_percent()
    return porcentaje

  @classmethod
  def obtener_disponible_memoria(cls):
    ram_disponible = psutil.virtual_memory().available
    return ram_disponible

  @classmethod
  def obtener_disponible_disco(cls):
    espacio_disponible = psutil.disk_usage('/').free
    return espacio_disponible
