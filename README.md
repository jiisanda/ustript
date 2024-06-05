# ustript


The user is allowed to upload an image of their urine test strip and `ustript` will identify the color of the pads and give 
a result based on the color of the pads. 

## Installation

```bash
git clone https://github.com/jiisanda/ustript.git
```

```bash
pip install -r requirements.txt
```

Create .env file as sample.env in [docs](docs/.sample.env)

## Usage

```bash
python manage.py migrate
python manage.py runserver
```

[docs.md](docs/docs.md) shows how to use the API...
