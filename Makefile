debug:
	FLASK_ENV=development \
	FLASK_APP=./tests/website/app.py \
	.venv/bin/flask run -p 8080


.PHONY: static
static:
	pipenv run python freeze.py

freeze:
	make static

push:
	make static
	pipenv lock -r  > requirements.txt
	git add -A
	git commit
	git push origin master

upload:
	python setup.py sdist bdist_wheel
	twine upload dist/*
	rm -rf dist/ *.egg-info/

wheel:
	rm -rf *.whl
	python setup.py sdist bdist_wheel
	mv dist/*.whl .
	rm -rf dist/ *.egg-info/ build/
