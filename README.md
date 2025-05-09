# API Automation Framework

This project is an industry-standard API automation framework designed for testing RESTful APIs. It incorporates logging and Allure reporting for enhanced visibility and traceability of test results.

## Project Structure

```
api-automation-framework
├── src
│   ├── api
│   │   ├── endpoints
│   │   │   └── example_endpoint.py
│   │   ├── __init__.py
│   │   └── client.py
│   ├── tests
│   │   ├── test_example.py
│   │   ├── conftest.py
│   │   └── __init__.py
│   ├── utils
│   │   ├── logger.py
│   │   ├── allure_helper.py
│   │   └── __init__.py
│   └── __init__.py
├── requirements.txt
├── pytest.ini
├── .gitignore
└── README.md
```

## Features

- **API Client**: A robust client for making HTTP requests to the API endpoints.
- **Endpoint Definitions**: Clear definitions for handling requests and responses.
- **Logging**: Integrated logging utility for tracking application behavior and errors.
- **Allure Reporting**: Integration with Allure for generating detailed test reports.
- **Test Cases**: Comprehensive test cases using pytest to validate API functionality.

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd api-automation-framework
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the tests:
   ```
   pytest --alluredir=allure-results
   ```

4. Generate the Allure report:
   ```
   allure serve allure-results
   ```

## Usage

- Modify the `example_endpoint.py` file to define your API endpoints.
- Use the `client.py` file to implement your API client logic.
- Write your test cases in the `test_example.py` file.
- Utilize the logging utility in `logger.py` for logging messages throughout your application.
- Leverage `allure_helper.py` to enhance your Allure reports with additional context.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.