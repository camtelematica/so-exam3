from flask import Flask
import json
from op_stats.stats import Stats

app = Flask(__name__)

@app.route('/v1/stats/cpu')
def informacion_cpu():
    info_cpu = Stats.porcentaje_cpu()
    return json.dumps({'Porcentaje CPU': info_cpu})

@app.route('/v1/stats/memory')
def informacion_memoria():
    info_memoria = Stats.memoria_disponible()
    return json.dumps({'Memoria disponible': info_memoria})

@app.route('/v1/stats/disk')
def informacion_disco():
    info_disco = Stats.espacio_disco()
    return json.dumps({'Espacio Libre Disco': info_disco})


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)
