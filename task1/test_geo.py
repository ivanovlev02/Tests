import pytest
from main import geo_logs


@pytest.mark.parametrize(
    "geo_logs_data, expected", [
        ([
             {'visit1': ['Москва', 'Россия']},
             {'visit2': ['Дели', 'Индия']},
             {'visit3': ['Владимир', 'Россия']},
             {'visit4': ['Лиссабон', 'Португалия']},
             {'visit5': ['Париж', 'Франция']},
             {'visit6': ['Лиссабон', 'Португалия']},
             {'visit7': ['Тула', 'Россия']},
             {'visit8': ['Тула', 'Россия']},
             {'visit9': ['Курск', 'Россия']},
             {'visit10': ['Архангельск', 'Россия']}
         ], ['visit1', 'visit3', 'visit7', 'visit8', 'visit9', 'visit10']),
        ([
             {'visit2': ['Дели', 'Индия']},
             {'visit4': ['Лиссабон', 'Португалия']},
             {'visit5': ['Париж', 'Франция']},
             {'visit6': ['Лиссабон', 'Португалия']},
         ], []),
        ([
             {'visit7': ['Тула', 'Россия']},
             {'visit8': ['Тула', 'Россия']},
         ], ['visit7', 'visit8']),
        [{}, []]
    ]
)
def test_geo_logs_with_parametrize(geo_logs_data, expected):
    result = geo_logs(geo_logs_data)
    assert result == expected
