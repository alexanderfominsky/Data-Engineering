# Задания от 1 апреля
test_get_fact_success – Проверяет корректное получение и сохранение факта из API при успешном ответе.

test_get_fact_connection_error – Тестирует обработку ошибки соединения и преобразование её в APIError.

test_get_fact_bad_status – Проверяет обработку HTTP-ошибок и их преобразование в APIError.

test_get_fact_analysis_empty – Тестирует анализ пустого факта.

test_get_fact_analysis_with_fact – Проверяет корректность анализа непустого факта.

test_integration_flow – Тестирует полный цикл работы: получение факта из API и его последующий анализ.
