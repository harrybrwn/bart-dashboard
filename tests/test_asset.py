import pytest
from flask import Flask
from flask.wrappers import Response


def test_app(app: Flask):
    print(app, type(app))
    for k, v in app.config.items():
        print(k, v)
    pass

def test_asset(client):
    resp: Response = client.get('/api/asset/15384437')
    assert resp.status_code == 200
    assert resp.json['num'] == 15384437

def test_asset_readings(client):
    resp: Response = client.get('/api/asset/15384437/readings')
    assert resp.status_code == 200
    assert resp.json['num'] == 15384437
    # print(resp.data.decode('utf-8'))
