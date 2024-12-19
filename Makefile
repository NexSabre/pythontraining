format:
	black -t py38 .
	isort --profile black .

install:
	python3 -m pip install -r requirements.txt

test:
	python3 -m pytest -v
