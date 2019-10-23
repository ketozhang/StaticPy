local:
	FLASK_ENV=development \
	pipenv run flask run -p 8081 --host 0.0.0.0

build:
	pipenv run python app.py build;

.PHONY: static
static:
	pipenv run python freeze.py && \
	find ../ -maxdepth 1 \
		! \( -name ".*" -o -name "_*" \) -exec rm -r {} \; && \
	rsync -a --remove-source-files build/ ../  && \
	rm -rf build

clean:
	rm -rf build/ ; \
	rm -rf build.bak/ ; \
	rm -rf templates/*.bak ; \
	rm -rf templates/notes/ ; \
	rm -rf templates/posts/; \

freeze:
	make static

push:
	make static && \
	git add -A && \
	git commit && \
	git push origin master
