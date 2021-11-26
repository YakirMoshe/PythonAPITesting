import pytest
# Test Case must be written inside a method
# Method name must be started with (test)

@pytest.mark.Smoke
@pytest.mark.Regression
def test_tc_002_Reqistration_Testing():
    print("This is Smoke Groping test case code.....")
    print("This is end of my test cases")

@pytest.mark.Smoke
def test_tc_003_Testing():
    print("This is Sanity Groping test case code.....")
    print("This is end of my test cases")