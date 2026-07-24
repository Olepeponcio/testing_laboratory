def test_even_values(subtests):
    values = (2, 6, 4)

    for value in values:
        with subtests.test(value=value):
            assert value % 2 == 0