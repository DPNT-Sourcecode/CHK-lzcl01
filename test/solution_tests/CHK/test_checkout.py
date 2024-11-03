from solutions.CHK.checkout_solution import checkout

def test_illegal_checkout():
    assert checkout("a") == -1
    assert checkout("-") == -1
    assert checkout("AxA") == -1

def test_empty_checkout():
    assert checkout("") == 0


def test_single_entry_checkout():
    assert checkout("A") == 50
    assert checkout("B") == 30


def test_special_offers_checkout():
    assert checkout("AAA") == 130
    assert checkout("BBBB") == 90