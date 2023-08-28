import pytest
import csv

# Test for equality. Will pass if 1 + 1 = 2.
def test_one_plus_one():
    assert 1 + 1 == 2

# Test for exception. Will pass if exception is raised.
def test_handle_exception():
    with pytest.raises(ZeroDivisionError) as excinfo:
        num = 1 / 0
    assert 'division by zero' in str(excinfo.value)

# Test with parameterization. Will pass if 1 + 1 = 2 and 2 + 2 = 4.
@pytest.mark.parametrize("num1, num2, result", [(1, 1, 2), (2, 2, 4)])
def test_add(num1, num2, result):
    assert num1 + num2 == result

# Test with parameterization. Will pass if 1 + 1 = 2 and 2 + 2 = 4.
params = [(1, 1, 2), (2, 2, 4)]

@pytest.mark.parametrize("num1, num2, result", params)
def test_add_prepared_params(num1, num2, result):
    assert num1 + num2 == result

# Test with parameterization. Read from a csv file.
def read_test_data(file_path):
    test_data = []
    with open(file_path, "r") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            test_data.append((int(row["input_value"]), int(row["expected_result"])))
    return test_data

# Test with parameterization. Will pass if 1 + 1 = 2 and 2 + 2 = 4.
@pytest.mark.parametrize("input_value, expected_result", read_test_data("test_data/test_data.csv"))
def test_multiply_by_two(input_value, expected_result):
    result = input_value * 2
    assert result == expected_result

# Test verifies two lists are equal.
def test_list_equality():
    list1 = [1, 2, 3]
    list2 = [1, 2, 3]
    assert list1 == list2

# Test verifies two lists are not equal.
def test_list_inequality():
    list1 = [1, 2, 3]
    list2 = [1, 2, 4]
    assert list1 != list2

# Tests verifies list contains an item.
def test_list_contains():
    list1 = [1, 2, 3]
    assert 1 in list1

# Tests verifies list does not contain an item.
def test_list_does_not_contain():
    list1 = [1, 2, 3]
    assert 4 not in list1

# Tests verifies list contains a few items.
def test_list_contains_few_items():
    list1 = [1, 2, 3]
    list2 = [1, 2]
    assert list2 in list1

# Tests verifies list dcontain items in a specific order.
def test_list_contains_items_in_order():
    list1 = [1, 2, 3]
    list2 = [1, 2]
    assert list1[:2] == list2 # :2 means first two items

# PyTest fixture. Will be executed before each test.
@pytest.fixture
def setup():
    print("Setup")
    a = [1, 2, 3]
    yield a # This is where the testing happens. before and after this line will be executed before and after each test.
    print("Teardown")

# Test uses a fixture.
def test_fixture(setup):
    assert setup == [1, 2, 3]

# PyTest fixture uses another fixture.
@pytest.fixture
def setup2(setup):
    print("Setup2")
    a = [key + 1 for key in setup]
    yield a
    print("Teardown2")

# Test uses a fixture that uses another fixture.
def test_fixture2(setup2):
    assert setup2 == [2, 3, 4]

# Pytest use multiple fixtures.
def test_multiple_fixtures(setup, setup2):
    assert setup == [1, 2, 3]
    assert setup2 == [2, 3, 4]

# Pytest use markers. Configure markers in pytest.ini file. Example: pytest.ini file in the root folder. 
# In order to run tests with markers, use pytest -m "smoke" command.
@pytest.mark.smoke
def test_markers():
    assert 1 + 1 == 2

# Pytest use markers - skip.
@pytest.mark.skip
def test_markers_skip():
    assert 1 + 1 == 2

# Pytest use markers - skipif.
@pytest.mark.skipif(1 + 1 == 2, reason="Skip if 1 + 1 == 2")
def test_markers_skipif():
    assert 1 + 1 == 2


# Pytest fixture scopes available. Default is function. Other scopes are class, module, package, and session.
# @pytest.fixture(scope="function") # scope="function" means that the fixture is initialized before each test and cleaned up after each test.
# @pytest.fixture(scope="class") # scope="class" means that the fixture is initialized before the first test in a class is run and cleaned up after the last test in the class is run.
# @pytest.fixture(scope="module") # scope="module" means that the fixture is initialized before the first test in a module is run and cleaned up after the last test in the module is run.
# @pytest.fixture(scope="package") # scope="package" means that the fixture is initialized before the first test in a package is run and cleaned up after the last test in the package is run.


# Pytest command line options.
# pytest --help. Shows all options.
# pytest -v # verbose. Shows the name of each test as it is run.
# pytest -q # quiet mode. Only shows the result of the tests.
# pytest -x # stop after first failure. Useful for debugging.
# pytest --maxfail=2 # stop after two failures. Useful for debugging.
# pytest -k "add" # run tests with "add" in the name.
# pytest -k "add or string" # run tests with "add" or "string" in the name
# pytest -k "add and string" # run tests with "add" and "string" in the name

# Pytest command line
# pytest -m "smoke" # run tests with "smoke" marker
# pytest -m "not smoke" # run tests without "smoke" marker
# pytest -m "smoke and not string" # run tests with "smoke" marker and without "string" marker

# Pytest command line generates a report.
# pytest --junitxml=report.xml # generates a report in xml format.

# Pytest command line. Run specific tests.
# pytest tests\py_test_capabilities_test.py::test_one_plus_one # run test_one_plus_one test in py_test_capabilities_test.py
