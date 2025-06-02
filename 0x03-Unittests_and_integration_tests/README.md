# Unit Tests and Integration Tests

This project demonstrates unit testing and integration testing patterns in Python using the `unittest` framework.

## Project Structure

- `utils.py` - Utility functions for GitHub org client
- `client.py` - GitHub organization client implementation
- `fixtures.py` - Test fixtures for integration tests
- `test_utils.py` - Unit tests for utility functions
- `test_client.py` - Unit and integration tests for GitHub client

## Key Testing Concepts Covered

### Unit Testing
- **Parameterized tests** using `@parameterized.expand`
- **Mocking external dependencies** with `unittest.mock`
- **Testing exceptions** with `assertRaises`
- **Property mocking** with `PropertyMock`

### Integration Testing
- **End-to-end testing** with minimal mocking
- **Class-level setup/teardown** with `setUpClass`/`tearDownClass`
- **Parameterized test classes** with `@parameterized_class`

## Running Tests

Execute individual test files:
```bash
python -m unittest test_utils.py
python -m unittest test_client.py
```

Run specific test methods:
```bash
python -m unittest test_utils.TestAccessNestedMap.test_access_nested_map
```

## Testing Patterns Demonstrated

1. **Mocking HTTP requests** - Avoiding actual network calls in tests
2. **Memoization testing** - Ensuring cached methods are called only once
3. **Exception testing** - Verifying proper error handling
4. **Integration testing** - Testing component interactions with fixtures

## Requirements

- Python 3.7+
- `parameterized` library for parameterized tests
- `unittest.mock` for mocking (built-in)