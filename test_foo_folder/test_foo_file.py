"""
This module contains basic examples of tests
"""

import pytest
import allure
import time
import random


def test_success():
    """this test succeeds"""
    assert False


def test_timely():
    """this test is marked successful and runs some time"""

    # create a random number as seconds to wait

    wait_time = random.randint(1, 5)
    time.sleep(wait_time)
    assert True


def test_paitence():
    """this test is marked successful and runs some more time"""

    wait_time = random.randint(5, 15)
    time.sleep(wait_time)
    assert True


def test_failure():
    """this test fails"""
    assert False


@allure.feature("Skip Title")
@allure.title("This skip test has a custom title")
def test_skip():
    """this test is skipped"""
    pytest.skip("for a reason!")


def test_broken():
    """this test is broken"""
    raise Exception("oops")
