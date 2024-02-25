import pytest
from main import uniq_ids


@pytest.mark.parametrize(
    "uniq_ids_data, expected", [
        ({'user1': [213, 213, 213, 15, 213],
          'user2': [54, 54, 119, 119, 119],
          'user3': [213, 98, 98, 35]},
         [213, 15, 54, 119, 98, 35]),
        ({'user1': [213, 213, 213, 15, 213],
          'user2': [54, 54, 119, 119, 119],
          'user3': [213, 98, 98, 35],
          'user4': [-213, -98, -98, -35]},
         [213, 15, 54, 119, 98, 35, -213, -98, -35]),
        ({}, []),
        ({'user1': [],
          'user2': [True],
          'user3': [None],
          'user4': [0]},
         [True, None, 0])
    ]
)
def test_uniq_ids_with_paramrtrize(uniq_ids_data, expected):
    result = uniq_ids(uniq_ids_data)
    assert result == expected
