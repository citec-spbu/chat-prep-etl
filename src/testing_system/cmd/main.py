from testing_system.cmd.test_mock_pipeline import mock_test
from testing_system.cmd.test_API_pipeline import API_test

mock_test()
print("\n")
API_test()

# logger is used in Runner, be careful - init the logger not to get error