from bubble import bubble_sort

def test_sorts_numbers():
    assert bubble_sort([5, 3, 9, 1]) == [1, 3, 5, 9]

def test_empty_list():
    assert bubble_sort([]) == []

def test_already_sorted():
    assert bubble_sort([1, 2, 3]) == [1, 2, 3]
