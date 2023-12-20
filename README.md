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

```bash
pip install pandas streamlit
```bash
streamlit run WEB.py
