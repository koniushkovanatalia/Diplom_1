import pytest
from praktikum.burger import Burger

@pytest.fixture
def burger():  # создает новый объект Burger перед каждым тестом
    return Burger()

