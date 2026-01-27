from calculator import add, subtract

# xUnit-style setup and teardown

def setup_module(module):
    print("\n[Setup Module] Starting test module")

def teardown_module(module):
    print("\n[Teardown Module] Ending test module")

def setup_function(function):
    print("\n[Setup Function] Starting test")

def teardown_function(function):
    print("\n[Teardown Function] Ending test")


def test_addition():
    assert add(2, 3) == 5

def test_subtraction():
    assert subtract(5, 3) == 2
