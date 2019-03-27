local:
	python app.py
build:
	python freeze.py
debug:
	python freeze.py debug
push:
	make build
	git add -A
	git commit
	git push origin master
