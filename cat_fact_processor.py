import pytest
from unittest.mock import patch, Mock
import requests
from collections import Counter

class APIError(Exception):
    pass

class CatFactProcessor:
    def __init__(self):
        self.last_fact = ""

    def get_fact(self):
        try:
            response = requests.get("https://catfact.ninja/fact")
            response.raise_for_status()
            data = response.json()
            self.last_fact = data["fact"]
            return self.last_fact
        except requests.exceptions.RequestException as e:
            raise APIError(f"Ошибка при запросе к API: {e}") from e

    def get_fact_analysis(self):
        if not self.last_fact:
            return {"length": 0, "letter_frequencies": {}}
        fact_length = len(self.last_fact)
        letter_frequencies = dict(Counter(self.last_fact.lower()))
        return {
            "length": fact_length,
            "letter_frequencies": letter_frequencies,
        }

# Тесты
@patch('requests.get') 
def test_get_fact_success(mock_get): #проверяет успешное получение факта и обновление last_fact
    mock_response = Mock()
    mock_response.raise_for_status = Mock()
    mock_response.json.return_value = {"fact": "Cats are great!"}
    mock_get.return_value = mock_response

    processor = CatFactProcessor()
    fact = processor.get_fact()

    assert fact == "Cats are great!"
    assert processor.last_fact == "Cats are great!"

@patch('requests.get')
def test_get_fact_failure(mock_get): #при ошибке запроса генерируется исключение APIError с правильным сообщением
    mock_get.side_effect = requests.exceptions.RequestException("API request failed")

    processor = CatFactProcessor()

    with pytest.raises(APIError, match="Ошибка при запросе к API: API request failed"):
        processor.get_fact()

def test_get_fact_analysis_no_fact(): #last_fact пустой, возвращает нулевую длину и пустой словарь частот
    processor = CatFactProcessor()
    analysis = processor.get_fact_analysis()

    assert analysis["length"] == 0
    assert analysis["letter_frequencies"] == {}

@patch('requests.get')
def test_get_fact_analysis_with_fact(mock_get): #last_fact заполнен? возвращает длину факта и частоты букв
    mock_response = Mock()
    mock_response.raise_for_status = Mock()
    mock_response.json.return_value = {"fact": "Cats are great!"}
    mock_get.return_value = mock_response

    processor = CatFactProcessor()
    processor.get_fact()  # Получаем факт

    analysis = processor.get_fact_analysis()

    assert analysis["length"] == len("Cats are great!")
    assert analysis["letter_frequencies"] == {'c': 1, 'a': 2, 't': 2, 's': 1, ' ': 2, 'e': 1, 'g': 1, 'r': 1, 'h': 1, '!': 1}

if __name__ == "__main__":
    pytest.main()
