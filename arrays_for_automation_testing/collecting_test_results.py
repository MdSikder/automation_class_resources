# Store results from multiple test cases in an array for further analysis.

results = []

# sample result form test cases

test_case_1_result = {"test_case": "Login","status": "Passed"}
test_case_2_result = {"test_case": "SignUp","status": "Failed"}

# store result in a list
results.append(test_case_1_result)
results.append(test_case_2_result)

# print all test results
for result in results:
    print(f"Test Case: {result['test_case']}, Status: {result['status']}")
