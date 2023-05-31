install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
	python -m textblob.download_corpora

test:
	python -m pytest -vv --cov=wikiphrases.py --cov=nlplogic test_corenlp.py

format:
	black *.py nlplogic/*.py

lint:
	pylint --disable=R,C *.py nlplogic/*.py

all: install lint test