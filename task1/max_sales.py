import pytest
from main import max_sales


@pytest.mark.parametrize(
    "max_sales_data, expected", [
        ({'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}, "yandex"),
        ({}, None),
        ({'facebook': 5500, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': -98}, "facebook"),
        ({'facebook': -5500, 'yandex': -120, 'vk': -115, 'google': -99, 'email': 0, 'ok': -98}, "email")
    ]
)
def test_max_sales_with_parametrize(max_sales_data, expected):
    result = max_sales(max_sales_data)
    assert result == expected
