import json
import pytest
import time
from main import YA

folder_name = int(time.time())
with open('config.json') as input_file:
    config = json.load(input_file)
ya_token = config['ya_token']
ya = YA(ya_token)

@pytest.mark.parametrize(
    "folder, expected", [
        (folder_name, 201),
        (folder_name, 409),
        ("", 400),
        ([folder_name], 409),
        (None, 400)
    ]
)
def test_create_folder_with_parametrize(folder, expected):
    resp = ya.create_folder(folder)
    assert resp.status_code == expected


@pytest.mark.parametrize(
    "path, expected", [
        (folder_name, 200),
        (folder_name - 1, 404),
        ("", 400),
        ([folder_name], 200),
        (None, 400)
    ]
)
def test_is_file_or_folder_exist(path, expected):
    resp = ya.is_file_or_folder_exist(path)
    assert resp.status_code == expected


@pytest.mark.parametrize(
    "path, expected", [
        (folder_name, 204),
        (folder_name, 404),
        ("", 400),
        ([folder_name], 404),
        (None, 400)
    ]
)
def test_delete_file_or_folder(path, expected):
    resp = ya.delete_file_or_folder(path)
    assert resp.status_code == expected
