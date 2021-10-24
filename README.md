# book_shop
How run the project?
Clone the repository :
$ git clone https://github.com/mohammadaliakbariii/book_shop.git
$ cd ecommerce-web
Create a virtualenv and activate it:
$ python3 -m venv venv
$ . venv/bin/activate
Or on Windows cmd :
> py -3 -m venv venv
> venv\Scripts\activate.bat
cd ecommerce-web
Install the requirements :
$ pip install -r requirements.txt
Run makemigrations and migrate :
python3 manage.py makemigrations
python3 manage.py migrate
Run the development server :
python3 manage.py runserver
Open http://127.0.0.1:8000 in your browser.
