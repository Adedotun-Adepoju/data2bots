import pytest

import os

file = os.path.join(os.path.dirname(os.path.realpath('__file__')),'python hands-on - dataset.csv')

from check_goods import check_obsolete

def test_expiry():
    assert check_obsolete(file).iloc[1,4]==True
def test_expiry2():
    assert check_obsolete(file).iloc[0,4]==False


