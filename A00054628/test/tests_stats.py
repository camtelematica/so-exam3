import pytest
from op_stats.app import app
from op_stats.stats import Stats
import sys
sys.path.append('/home/flaskdev/so-exam3')

@pytest.fixture
def client():
  client = app.test_client()
  return client

def test_get_cpu_percent(mocker, client):
  mocker.patch.object(Stats, 'porcentaje_cpu', return_value=100)
  response = client.get('/v1/stats/cpu')
  assert response.data.decode('utf-8') == '{"Porcentaje CPU": 100}'
  assert response.status_code == 200

def test_get_available_memory(mocker, client):
  mocker.patch.object(Stats, 'memoria_disponible', return_value=1000)
  response = client.get('/v1/stats/memory')
  assert response.data.decode('utf-8') == '{"Memoria disponible": 1000}'
  assert response.status_code == 200


def test_get_disk_space(mocker, client):
  mocker.patch.object(Stats, 'espacio_disco', return_value=2000)
  response = client.get('/v1/stats/disk')
  assert response.data.decode('utf-8') == '{"Espacio Libre Disco": 2000}'
  assert response.status_code == 200
