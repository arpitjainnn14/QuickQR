# QR Code Generator with Streamlit

## Overview

This is a simple web-based **QR Code Generator** built using **Streamlit** and **Segno**. It allows users to input a URL, generate a QR code, and display the generated QR code on the screen.

## Features

- Accepts a URL as input.
- Generates a QR code for the provided link.
- Displays the generated QR code.
- (Upcoming) Feature to download the generated QR code.

## Installation

To run this project locally, follow these steps:

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/qr-code-generator.git
   cd qr-code-generator
   ```
2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install the required dependencies:
   ```bash
   pip install streamlit segno
   ```
4. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

## Usage

1. Open the Streamlit app in your browser.
2. Enter a valid URL in the input field.
3. Click the **Submit** button.
4. The generated QR code will be displayed.
5. (Upcoming) Click **Download** to save the QR code.

## Technologies Used

- **Streamlit** - To create the web interface.
- **Segno** - To generate QR codes.
- **Python** - Backend programming language.

## Future Improvements

- **Download feature** to save the QR code as an image.
- **Customization options** for QR code size and color.
- **Error handling** for invalid inputs.

---

Feel free to contribute by adding new features or improving the existing ones!

