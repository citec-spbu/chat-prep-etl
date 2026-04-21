from testing_system.cmd.test_mock_pipeline import mock_test
from testing_system.cmd.test_ollama_pipeline import ollama_test

mock_test()
print("\n")
ollama_test()

# logger is used in Runner, be careful - init the logger not to get error