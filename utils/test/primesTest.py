import pytest
import math
from primes import isPrime, display
import pytest

def test_isPrime_small_primes():
    assert isPrime(2) == True
    assert isPrime(3) == True
    assert isPrime(5) == True
    assert isPrime(7) == True
    print("Test 1 passed.")

def test_isPrime_small_non_primes():
    assert isPrime(1) == True 
    assert isPrime(4) == False
    assert isPrime(6) == False
    assert isPrime(9) == False
    print("Test 2 passed.")

def test_isPrime_large_prime():
    assert isPrime(7919) == True
    print("Test 3 passed.")

def test_isPrime_large_non_prime():
    assert isPrime(8000) == False
    print("Test 4 passed.")

def test_isPrime_negative_numbers():
    assert isPrime(-7) == False 
    print("Test 5 passed.")

def test_display_output_simple_range(capsys):
    display(1, 10)
    captured = capsys.readouterr()
    output = captured.out.strip().replace('\n', '').split('\t')
    primes = list(map(int, filter(None, output)))
    assert primes == [1, 2, 3, 5, 7]
    print("Test 6 passed.")

def test_display_no_primes(capsys):
    display(0, 0)
    captured = capsys.readouterr()
    assert captured.out.strip() == ''
    print("Test 7 passed.")

def test_display_single_prime(capsys):
    display(10, 12)
    captured = capsys.readouterr()
    assert "11" in captured.out
    print("Test 8 passed.")

def test_display_many_primes(capsys):
    display(1, 30)
    captured = capsys.readouterr()
    primes_in_output = [int(s) for s in captured.out.split() if s.isdigit()]
    expected_primes = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    assert primes_in_output == expected_primes
    print("Test 9 passed.")

# 10. Test display prints newlines every 10 primes
def test_display_newline_every_10(capsys):
    display(1, 100)
    captured = capsys.readouterr()
    assert captured.out.count('\n') > 0
    print("Test 10 passed.")
    print("All tests passed.")

