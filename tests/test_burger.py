import pytest
from unittest.mock import Mock
from praktikum.burger import Burger

class TestBurger:
    # проверка, что set_buns сохраняет объект булки в атрибут burger.bun
    def test_set_buns_assigns_bun_to_attribute(self, burger):
        bun_mock = Mock()
        burger.set_buns(bun_mock)
        assert burger.bun is bun_mock

    # проверка, что метод add_ingredient добавляет ингредиент в список
    def test_add_ingredient_adds_to_list(self, burger):
        ingredient_mock = Mock()
        burger.add_ingredient(ingredient_mock)
        assert ingredient_mock in burger.ingredients
        assert len(burger.ingredients) == 1

    # проверка, что метод remove_ingredient удаляет ингредиент по индексу
    @pytest.mark.parametrize("index_to_remove", [0, 1])
    def test_remove_ingredient_removes_correctly(self, burger, index_to_remove):
        ingredient1 = Mock()
        ingredient2 = Mock()
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)

        burger.remove_ingredient(index_to_remove)

        assert len(burger.ingredients) == 1
        remaining = burger.ingredients[0]
        assert remaining != [ingredient1, ingredient2][index_to_remove]

    # проверка, что метод move_ingredient корректно перемещает ингредиенты
    @pytest.mark.parametrize("initial, index, new_index, expected",[(["A", "B", "C"], 0, 2, ["B", "C", "A"]), (["A", "B", "C"], 2, 0, ["C", "A", "B"]),],)
    def test_move_ingredient_moves_correctly(self, burger, initial, index, new_index, expected):
        burger.ingredients = initial.copy()
        burger.move_ingredient(index, new_index)
        assert burger.ingredients == expected

    # проверка, что метод get_price правильно рассчитывает стоимость бургера
    @pytest.mark.parametrize("bun_price, ingredient_prices, expected_price",[(100, [50, 20], 100 * 2 + 50 + 20),(80, [], 80 * 2),(0, [10, 10], 0 + 20),],)
    def test_get_price_calculates_correctly(self, burger, bun_price, ingredient_prices, expected_price):
        bun_mock = Mock()
        bun_mock.get_price.return_value = bun_price
        burger.set_buns(bun_mock)

        for price in ingredient_prices:
            ingredient_mock = Mock()
            ingredient_mock.get_price.return_value = price
            burger.add_ingredient(ingredient_mock)

        assert burger.get_price() == expected_price

    # проверка, что метод get_receipt возвращает содержимое чека
    def test_get_receipt_returns_correct_string(self, burger):
        bun_mock = Mock()
        bun_mock.get_name.return_value = "Sesame Bun"
        bun_mock.get_price.return_value = 100
        burger.set_buns(bun_mock)

        ingredient1 = Mock()
        ingredient1.get_type.return_value = "SAUCE"
        ingredient1.get_name.return_value = "Ketchup"
        ingredient1.get_price.return_value = 20

        ingredient2 = Mock()
        ingredient2.get_type.return_value = "FILLING"
        ingredient2.get_name.return_value = "Beef"
        ingredient2.get_price.return_value = 200

        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)

        receipt = burger.get_receipt()

        assert receipt.count("Sesame Bun") == 2
        assert "= sauce Ketchup =" in receipt
        assert "= filling Beef =" in receipt
        expected_price = 2 * 100 + 20 + 200
        assert f"Price: {expected_price}" in receipt

    # проверка, что remove_ingredient вызывает исключение IndexError при неверном индексе
    def test_remove_ingredient_invalid_index_raises(self, burger):
        ingredient = Mock()
        burger.add_ingredient(ingredient)

        with pytest.raises(IndexError):
            burger.remove_ingredient(5)

    # проверка, что move_ingredient вызывает исключение IndexError при неверном индексе
    def test_move_ingredient_invalid_index_raises(self, burger):
        ingredient = Mock()
        burger.add_ingredient(ingredient)

        with pytest.raises(IndexError):
            burger.move_ingredient(3, 0)







