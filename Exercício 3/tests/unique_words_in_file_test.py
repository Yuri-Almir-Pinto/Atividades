from projects import unique_words_in_file as unique_words

def test_get_unique_words() -> None:
    result: list = unique_words.get_unique_words("./artifacts/unique_words_file.txt")

    assert result[0] == "alface"
    assert result[1] == "cenoura"
    assert result[2] == "potatoe"