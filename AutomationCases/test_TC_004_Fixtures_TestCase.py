# Test Case must be written inside a method
# Method name must be started with (test)
import pytest

@pytest.fixture(scope="module")
def fixture_code():
    print("This is are Fixture Code will execute before testcase")
    print("-------------------------------------------------------------------")
    yield
    print("Close browser after executing testcase / Close Db Connection after executing testcase")
    print("-------------------------------------------------------------------")


@pytest.mark.Smoke
def test_tc_002_Reqistration_Testing(fixture_code):
    print("This is Smoke Groping test case code.....")
    print("This is end of my test cases")

@pytest.mark.Sanity
def test_tc_003_Testing(fixture_code):
    print("This is Sanity Groping test case code.....")
    print("This is end of my test cases")