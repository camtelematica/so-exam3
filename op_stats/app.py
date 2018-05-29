from flask import Flask
import json
import sys
sys.path.append('/home/rootCam/so-exam3')
from op_stats.stats import Stats

app = Flask(__name__)

@app.route('/v1/cpu')
def obtener_info_cpu():
    disponible_cpu = Stats.obtener_disponible_cpu()
    return json.dumps({'Porcentaje CPU': disponible_cpu })

@app.route('/v1/memoria')
def obtener_info__memoria():
    disponible_memoria = Stats.obtener_disponible_memoria()
    return json.dumps({'Memoria Disponible': disponible_memoria})

@app.route('/v1/disco')
def obtener_info_disco():
    disponible_disco = Stats.obtener_disponible_disco()
    return json.dumps({'Espacio Libre Disco': disponible_disco})


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)
