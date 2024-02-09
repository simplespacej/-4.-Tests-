import pytest
from example2 import merge_mentors_lists, extract_first_names, get_unique_names, count_names, get_top_n_names

mentors_test = [
    ["Иван Иванов", "Петр Петров"],
    ["Иван Иванов", "Алексей Алексеев"]
]

@pytest.mark.parametrize("input_list,expected", [
    (mentors_test, ["Иван Иванов", "Петр Петров", "Иван Иванов", "Алексей Алексеев"])
])
def test_merge_mentors_lists(input_list, expected):
    assert merge_mentors_lists(input_list) == expected

@pytest.mark.parametrize("mentors,expected", [
    (["Иван Иванов", "Петр Петров"], ["Иван", "Петр"])
])
def test_extract_first_names(mentors, expected):
    assert extract_first_names(mentors) == expected

@pytest.mark.parametrize("names,expected", [
    (["Иван", "Петр", "Иван"], ["Иван", "Петр"])
])
def test_get_unique_names(names, expected):
    assert get_unique_names(names) == expected

@pytest.mark.parametrize("names,expected", [
    (["Иван", "Петр", "Иван"], [["Иван", 2], ["Петр", 1]])
])
def test_count_names(names, expected):
    result = count_names(names)
    assert sorted(result, key=lambda x: x[0]) == sorted(expected, key=lambda x: x[0])

@pytest.mark.parametrize("names_count,n,expected", [
    ([["Иван", 2], ["Петр", 1], ["Алексей", 3]], 2, [["Алексей", 3], ["Иван", 2]])
])
def test_get_top_n_names(names_count, n, expected):
    assert get_top_n_names(names_count, n) == expected
