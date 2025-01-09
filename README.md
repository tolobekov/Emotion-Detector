# Emotion Detection Application

This project utilizes the Watson NLP library to detect emotions from text. The application leverages the Emotion Predict function of the Watson NLP Library, which is embedded within the environment and does not require explicit imports. Instead, it interacts with the library through HTTP POST requests.

## Features

- **Emotion Analysis**: Analyze the emotional tone from the text using the Watson NLP's embedded libraries.
- **Simple HTTP Interface**: Utilizes a straightforward HTTP POST interface for sending data and receiving emotion analysis.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Ensure you have the following installed:
- Python 3.8 or later
- Requests library

You can install the Requests library using pip:
```bash
pip install requests
