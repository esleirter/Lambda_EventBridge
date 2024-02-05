# Lambda with EventBridge Events

This is a Python project that includes a lambda function to interact with the Jira Cloud API.

## Description

This project contains a lambda function that creates an issue in a Jira project. The function takes an event as input, extracts the title and description from the event details, and uses these to create a new issue in the specified Jira project.

## Installation

1. Clone the repository
2. Install the required packages using pip:

```bash
pip install -r requirements.txt
```

## Usage

To use this function, you need to pass an event with the following structure:
```json
{
  "detail": {
    "title": "Issue title",
    "description": "Issue description"
  }
}
```
