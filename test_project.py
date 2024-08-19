from project import check_guess, get_random_word
import pytest

def test_get_random_word():
    with pytest.raises(FileNotFoundError):
        get_random_word("sample.txt")

def test_check_guess_false():
    word = "apple"
    assert check_guess(word, "aeiou") == False
    assert check_guess(word, "chair") == False

def test_check_guess_true():
    assert check_guess("apple", "apple") == True
    assert check_guess("chair", "chair") == True

def test_check_guess_numbers():
    word = "apple"
    assert check_guess(word, "123") == False
    assert check_guess(word, "12345") == False
    assert check_guess(word, "123456") == False

def test_check_guess_invalid():
    word = "apple"
    assert check_guess(word, "abc") == False
    assert check_guess(word, "abcd") == False
    assert check_guess(word, "abcdef") == False
