local:
	pipenv run python app.py

build:
	pipenv run python app.py build


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

wheel:
	python setup.py sdist bdist_wheel
	mv dist/*.whl .
	rm -rf dist/ *.egg-info/
