# coding=utf-8
# 2019.12.5 v1.1.16 #249 create by Jia ChunYing
from demo.swagger.demo_flask_swagger import app
import pytest


@pytest.fixture
def client():
    app.config['TESTING'] = True

    with app.test_client() as client:
        yield client


# 2019.12.5 v1.1.16 #249 create by Jia ChunYing
@pytest.mark.usefixtures('client')
class TestSwagger(object):

    def test_query(self, client):
        response = client.get('/v1/query')
        assert b'test_query' in response.data

    def test_add(self, client):
        response = client.post('/v1/add')
        assert b'test_add' in response.data

    def test_del(self, client):
        response = client.delete('/v1/del')
        assert b'test_del' in response.data

    def test_update(self, client):
        response = client.put('/v1/update')
        assert b'test_update' in response.data
