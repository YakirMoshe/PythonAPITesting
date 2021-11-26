import pytest
# Test Case must be written inside a method
# Method name must be started with (test)


# Skip execution of any specific testcase
a=101
@pytest.mark.skipif(a>100, reason="Skipping as this functionality is not working, devloper will it in new build")
def test_tc_001_Login_Loggout_Testing():
    print("This is out test case code.....")
    print("This is end of my test cases")


@pytest.mark.TopPriority
def test_tc_002_Login_Logout_invalid_Credentials():
    print("This is my testcase 3")
    print("This is End of testcase")

# Print statment output display on console -s
# Verbosa moda - display test case name with status  -v

@pytest.mark.TopPriority
def test_sanity_01_Testing():
    print("This is out test case code.....")
    print("This is end of my test cases")

@pytest.mark.Smoke
def test_sanity_02_testing():
    print("This is my testcase 3")
    print("This is End of testcase")


#Assertions

actual_result = "Testing"

@pytest.mark.TopPriority
def test_tc_01_Login_Loggout_Testing():
    print("This is out test case code.....")
    print("This is end of my test cases")

    assert actual_result != "Testing", "These 2 values must not be same"