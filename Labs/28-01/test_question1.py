import pytest
import sys

# 1. Use @pytest.mark.parametrize to test multiple input combinations
# Testing a simple addition logic
@pytest.mark.parametrize("input_a, input_b, expected", [
    (1, 2, 3),
    (5, 5, 10),
    (10, -2, 8),
    (0, 0, 0)
])
def test_addition_parametrized(input_a, input_b, expected):
    assert input_a + input_b == expected

# 5. Execute tests with different command-line options
# This test consumes the custom CLI option created in conftest.py
def test_print_environment(get_env):
    print(f"Current Environment: {get_env}")
    # Logic to switch URL based on env could go here
    assert get_env in ["dev", "qa", "prod"]

# 4. Mark certain tests as skip
@pytest.mark.skip(reason="Feature is currently under development")
def test_checkout_feature():
    assert False # This won't run

# Conditional skip (e.g., skip if not running on Windows)
@pytest.mark.skipif(sys.platform != "win32", reason="Tests only run on Windows")
def test_windows_specific_feature():
    assert True

# 4. Mark certain tests as xfail (Expected Failure)
@pytest.mark.xfail(reason="Known bug ID-123: Division by zero not handled yet")
def test_calculation_bug():
    # We expect this to fail. If it passes, Pytest will report 'XPASS'
    assert 1 / 0 == 0