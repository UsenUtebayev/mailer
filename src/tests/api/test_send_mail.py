import requests


# headers = {'Content-type': 'content_type_value', "accept": "application/json"}


def test_succesfull():
    """Проверка сервера на возможность ответа на корректные данные"""
    json_body = {"to": "testmail@mail.com", "subject": "Test", "message": "lorem ipsum dolor sit amet"}
    response = requests.post("http://localhost:8000/send_email", json=json_body)
    assert response.status_code == 200


def test_invalid_email():
    """Проверка сервера на возможность ответа на неккорреткную почту"""
    json_body = {"to": "testmail.com", "subject": "Test", "message": "lorem ipsum dolor sit amet"}
    response = requests.post("http://localhost:8000/send_email", json=json_body)
    assert response.status_code == 422


def test_empty_subject():
    """Проверка сервера на плохой запросс ввиде пустой темы в сообщений"""
    json_body = {"to": "testmail.com", "subject": "", "message": "lorem ipsum dolor sit amet"}
    response = requests.post("http://localhost:8000/send_email", json=json_body)
    assert response.status_code == 422


def test_empty_message():
    """Првоерка сервера на плохой запросс ввиде пустого сообщения"""
    json_body = {"to": "testmail.com", "subject": "Test", "message": ""}
    response = requests.post("http://localhost:8000/send_email", json=json_body)
    assert response.status_code == 422
