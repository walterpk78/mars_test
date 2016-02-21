__author__ = 'Walter Kuhn'
from mars import Mars
import pytest


def test_init():
    mars = Mars('file1.json', 'file2.json')
    assert mars


def test_send():
    mars = Mars('file.json', 'file2.json')
    json_dict = {'name': 'Walter', 'age': '38', 'place': 'Milan'}
    assert mars.send(json_dict) == 1
    assert mars.send('Renault') is None


def test_receive():
    mars = Mars('file.json', 'file2.json')
    data = mars.receive()
    assert data['name'] == 'Walter'
    cars = Mars('Renault', 'Fiat')
    assert cars.receive() is None