local:
	python app.py
build:
	python app.py build
static:
	python freeze.py
push:
	make build
	git add -A
	git commit
	git push origin master
