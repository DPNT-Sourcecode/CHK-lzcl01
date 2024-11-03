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


def test_special_offers_priority_checkout():
    assert checkout("AAAAA") == 200


def test_mixed_special_offers_checkout():
    assert checkout("AAAA") == 180
    assert checkout("BBBBB") == 120


def test_multiple_mixed_special_offers_checkout():
    assert checkout("AAAABBBBB") == 300


def test_free_item_offer():
    assert checkout("BBEE") == 40 + 40 + 30


def test_free_item_same_offer():
    assert checkout("F") == 10
    assert checkout("FF") == 20
    assert checkout("FFF") == 20
    assert checkout("FFFF") == 30
    assert checkout("FFFFF") == 40
    assert checkout("FFFFFF") == 40


def test_meal_deals():
    assert checkout("STX") == 45
    assert checkout("ZXXZZ") == 45 + 17 + 17