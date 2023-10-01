
# Currency Converter Web Application using Django

This is a Django-based web application for currency conversion using the forex-python package.

## Installation

Before you start, make sure you have Python and Django installed on your system. If not, you can install them using pip:

```bash
pip install django
```

Additionally, install the `forex-python` package:

```bash
pip install forex-python
```

## Getting Started

1. Clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/currency-converter.git
```

2. Navigate to the project directory:

```bash
cd currency-converter
```

3. Apply the database migrations:

```bash
python manage.py migrate
```

4. Create a superuser account (you can use 'root' for both username and password):

```bash
python manage.py createsuperuser
```

5. Start the development server:

```bash
python manage.py runserver
```

6. Access the web application in your browser at http://localhost:8000/

## Usage

1. Log in to the admin panel using the superuser account you created earlier at http://localhost:8000/admin/

2. Add currency data to the database through the admin panel.

3. Use the web application to convert currencies by selecting the "From Currency" and "To Currency" from the dropdown menus and entering the amount to convert.

4. Click the "Convert" button to see the converted amount.
