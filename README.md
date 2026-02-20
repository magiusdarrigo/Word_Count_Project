# Word Count Project

A Django web application that analyzes text and counts word frequencies.

## Features

- Paste or type any block of text into the input form
- See the total word count
- View a frequency breakdown of every word, sorted from most to least common

## Pages

| Route | Description |
|-------|-------------|
| `/` | Home page with the text input form |
| `/count/` | Results page showing word count and frequency table |
| `/about/` | About page |

## Requirements

- Python 3.x
- Django 2.2

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/magiusdarrigo/Word_Count_Project.git
   cd Word_Count_Project
   ```

2. Install Django:
   ```bash
   pip install django==2.2
   ```

3. Run the development server:
   ```bash
   python manage.py runserver
   ```

4. Open your browser and navigate to `http://127.0.0.1:8000/`

## Usage

1. On the home page, type or paste text into the textarea
2. Click **Count!** to submit
3. The results page will show:
   - Total number of words
   - Your original text
   - Each unique word alongside how many times it appears, sorted by frequency (highest first)
4. Click **Start Again?** to return to the home page and analyze new text

## Project Structure

```
Word_Count_Project/
├── Word_Count/
│   ├── settings.py       # Django project settings
│   ├── urls.py           # URL routing
│   ├── views.py          # View logic (home, count, about)
│   └── wsgi.py
├── templates/
│   ├── home.html         # Text input form
│   ├── count.html        # Word frequency results
│   └── about.html        # About page
└── manage.py
```
