import pytest
from example3 import get_mentors_names_by_course, find_common_mentors

mentors_test = [
    ["Иван Иванов", "Петр Петров"],
    ["Иван Иванов", "Алексей Алексеев"],
    ["Дмитрий Дмитриев", "Алексей Алексеев"]
]

courses_test = ["Курс1", "Курс2", "Курс3"]

def test_get_mentors_names_by_course():
    expected = [["Иван", "Петр"], ["Иван", "Алексей"], ["Дмитрий", "Алексей"]]
    assert get_mentors_names_by_course(mentors_test) == expected

@pytest.mark.parametrize("mentors_names, courses, expected", [
    ([["Иван", "Петр"], ["Иван", "Алексей"], ["Дмитрий", "Алексей"]], courses_test, [("Курс1", "Курс2", ["Иван"]), ("Курс2", "Курс3", ["Алексей"])])
])
def test_find_common_mentors(mentors_names, courses, expected):
    assert find_common_mentors(mentors_names, courses) == expected