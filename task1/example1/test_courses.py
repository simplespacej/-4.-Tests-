import pytest
from example1 import get_all_mentors, get_unique_names 

def test_get_all_mentors():
    mentors_lists = [
        ["Имя1 Фамилия1", "Имя2 Фамилия2"],
        ["Имя3 Фамилия3", "Имя1 Фамилия1"]
    ]
    # Ожидаемый результат теперь включает дубликаты
    expected = ["Имя1 Фамилия1", "Имя2 Фамилия2", "Имя3 Фамилия3", "Имя1 Фамилия1"]
    assert get_all_mentors(mentors_lists) == expected

@pytest.mark.parametrize("test_input,expected", [
    (["Имя1 Фамилия1", "Имя2 Фамилия2", "Имя3 Фамилия3", "Имя1 Фамилия1"], ["Имя1", "Имя2", "Имя3"]),
    (["Имя4 Фамилия4", "Имя5 Фамилия5"], ["Имя4", "Имя5"]),
])
def test_get_unique_names(test_input, expected):
    assert get_unique_names(test_input) == expected
