## VS code env
`python3 -m venv .venv`  
`source .venv/bin/activate`

## Install dependencies
`pip install -r requirements.txt`

## Save requirements
`pip freeze > requirements.txt`

## Run app
Main of app module prints html, so best to redirect to file
`python -m app > result_file.html`