local:
	python app.py
build:
	python app.py build

.PHONY: static
static:
	python freeze.py
freeze:
	make static
push:
	make static 
	git add -A
	git commit
	git push origin master
