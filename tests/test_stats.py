import pytest
import sys
sys.path.append('/home/flaskdev/so-exam3')

from op_stats.app import app
from op_stats.stats import Stats

@pytest.fixture
def client():
  client = app.test_client()
  return client

def test_get_cpu_percent(mocker, client):
  mocker.patch.object(Stats, 'obtener_disponible_cpu', return_value=100)
  response = client.get('/v1/cpu')
  assert response.data.decode('utf-8') == '{"Porcentaje CPU": 100}'
  assert response.status_code == 200

def test_get_available_memory(mocker, client):
  mocker.patch.object(Stats, 'obtener_disponible_memoria', return_value=2000)
  response = client.get('/v1/memoria')
  assert response.data.decode('utf-8') == '{"Memoria Disponible": 2000}'
  assert response.status_code == 200


def test_get_disk_space(mocker, client):
  mocker.patch.object(Stats, 'obtener_disponible_disco', return_value=1000)
  response = client.get('/v1/disco')
  assert response.data.decode('utf-8') == '{"Espacio Libre Disco": 1000}'
  assert response.status_code == 200
