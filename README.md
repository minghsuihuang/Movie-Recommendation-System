# Movie Recommendation System

## Project Overview
This project is a content-based movie recommendation system. It utilizes the `pandas` library for processing and analyzing movie data, and offers movie recommendations through a `streamlit`-based web interface.

## File Description
- `main_WEB.py`: The primary data processing script, responsible for reading the movie dataset (`dataset.csv`), performing data cleaning, feature extraction, and preparing data for the recommendation system.
- `WEB.py`: A `streamlit`-based web application script. It includes the design and implementation of the user interface, along with the application of the recommendation algorithm.

## How to Run

### Environment Setup
First, ensure that the following Python libraries are installed in your environment:
- `pandas` for data processing and analysis.
- `streamlit` for building and running the web application.
- Other dependencies as required.

If you have not installed these libraries yet, you can install them using the following command:

### Data Preparation
1. Ensure you have the `dataset.csv` file required for the project.
2. Place the `dataset.csv` file in the root directory of the project.

### Running the Web Application
1. Open your terminal or command-line interface.
2. Navigate to the directory containing `WEB.py`.
3. Run the following command to start the `streamlit` web server:

4. `streamlit` will automatically open the application interface in the default web browser, or you can manually open it in the browser using the address displayed in the terminal.

### Using the Application
In the application interface, you can:
- Browse the list of movies.
- Get movie recommendations based on your preferences.
- View detailed information about the movies.

```bash
streamlit run WEB.py
