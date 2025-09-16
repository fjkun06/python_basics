from employee import Employee
import pytest

@pytest.fixture
def worker():
    worker = Employee("Frank", "Jordan", 60_000)
    return worker

def test_full_name(worker):
    """Test full name"""
    assert worker.get_full_name() == 'Frank Jordan'

def test_give_default_raise(worker):
    """Test default 5_000 raise"""
    worker = Employee("Frank", "Jordan", 60_000)
    print("For this year's salary updates, we have:")
    # Give default raise
    worker.give_raise()
    # Congratulate worker
    print(
        f"\t- {worker.get_full_name()}: from {worker.get_initial_salary()} => {worker.get_raised_salary()}"
    )

    assert worker.get_raised_salary() == 65_000

def test_give_custom_raise(worker):
    """Test custom 15_000 raise"""
    worker = Employee("Frank", "Jordan", 60_000)
    print("For this year's salary updates, we have:")
    # Give default raise
    worker.give_raise(15_000)
    # Congratulate worker
    print(
        f"\t- {worker.get_full_name()}: from {worker.get_initial_salary()} => {worker.get_raised_salary()}"
    )

    assert worker.get_raised_salary() == 75_000
