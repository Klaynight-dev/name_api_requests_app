# Name Age Prediction App

This simple application uses the Agify API to predict the probable age of a person based on their name. The user interface is created with PyQt5 using the `requests` module to make requests to the Agify API.

## Features

- **User-Friendly Interface:** A simple interface with a text field to enter a name, a button to get the age prediction, and a space to display the result.

- **Age Prediction:** Uses the Agify API to estimate age based on the entered name.

## Screenshot

![Application Screenshot](src/screenshot.png)

## How to Use

1. Clone the repository:

   ```bash
   git clone https://github.com/klaynight-dev/name_api_requests_app.git
   cd name_api_requests_app
   ```

2. Install dependencies:

   ```bash
   pip install PyQt5 requests
   ```

3. Run the application:

   ```bash
   python main.py
   ```

4. Enter a name in the text field and click the "Get Age" button to see the age prediction.

## Customization

- You can customize the style of the user interface by modifying the style sheets in the code.

## Author

- [klaynight-dev](https://github.com/klaynight-dev)

## Notes

- Make sure to have the necessary libraries installed using `pip install PyQt5 requests` before running the application.
