# Python REST APIs With Flask, Connexion, and SQLAlchemy – Part 1

## Entrega de API REST con SQLite

Este proyecto replica el laboratorio de la Unidad 4: API REST en Python con Flask,
Connexion, SQLAlchemy y Marshmallow. Incluye CRUD de personas, persistencia SQLite
y documentación interactiva con Swagger.

This repository holds the code for part one of the Real Python [Python REST APIs With Flask, Connexion, and SQLAlchemy](https://realpython.com/flask-connexion-rest-api) tutorial series.
The `rp_flask_api` example persists people in the SQLite database `rp_flask_api/people.db`; the database and sample people are initialized automatically when the app starts.

## Real Python Flask REST API – Part 1

You should first create a virtual environment:

```console
$ python -m venv venv
$ source venv/bin/activate
```

Install the pinned dependencies from `requirements.txt`:

```console
(venv) $ python -m pip install -r requirements.txt
```

Then, navigate into the `rp_flask_api/` folder and start the development web server:

```console
(venv) $ cd rp_flask_api
(venv) $ python app.py
```

On Windows, run these commands from the repository root in PowerShell:

```powershell
py -3.14 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
Set-Location .\rp_flask_api
..\.venv\Scripts\python.exe app.py
```

To see your home page, visit `http://127.0.0.1:8000`. You can find the Swagger UI API documentation on `http://127.0.0.1:8000/api/ui`.

## Flask Starter

You can find the _Flask Starter_ files in the `flask_starter/` folder.

To use the _Flask Starter_, copy the `flask_starter/` folder and rename it to your Flask project name. Open the terminal inside of your project folder, and create a virtual environment:

```console
$ python -m venv venv
$ source venv/bin/activate
```

You can then install Flask with `pip`:

```console
(venv) $ python -m pip install flask
```

You can start your Flask development server by running `app.py` as a script:

```console
(venv) $ python app.py
```

To see your home page, visit `http://127.0.0.1:8000`.

## Author

- **Philipp Acsany**, E-mail: [philipp@realpython.com](philipp@realpython.com)

## License

Distributed under the MIT license. See [`LICENSE`](../LICENSE) for more information.
