local:
	pipenv run python app.py

build:
	pipenv run python app.py build

.PHONY: static
static:
	pipenv run python freeze.py
	rsync -avh build/* ../
	rm -rf build/

freeze:
	make static

push:
	make static
	git add -A
	git commit
	git push origin master
