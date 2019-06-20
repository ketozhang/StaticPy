## Installation

1. Clone the repostiory:

	```
	git clone https://github.com/ketozhang/StaticPy
	```

2. Move all content (`.git` and `.gitignore`) to your project folder:

	```
	mv Staticpy/* /path/to/project/
	```

3. Run the web environment locally:

	```
	make local # or python app.py
	```

## Github Pages

If you would like to use github pages the instructions are the exact same if it's a project/organization page (e.g., `<username>.github.io/<projectname>`). However if it's a user page (e.g., `<username>.github.io`) then all the web content should either be in a `docs/` folder or the root of the repository.

### User Page Recommended Solution

1. Create project folder for your website:

	```
	mkdir /path/to/project
	cd /path/to/project
	```

2. Clone StaticPy onto your project folder:

	```
	git clone https://github.com/ketozhang/StaticPy
	```

3. Clone your user page repository

	```
	git clone https://github.com/<username>/<username>.github.io
	```

4. Add this `Makefile` to `/path/to/project/`. It will be useful as a macro:

	```Makefile
	static:
		$(MAKE) -C _dev static
		cd ketozhang.github.io; \
			git rm -rf --ignore-unmatch .;
		cp -r _dev/docs/* ketozhang.github.io/

	push:
		make static
		cd ketozhang.github.io; \
			git add -A; \
			git commit; \
			git push origin master;
	```

## Updating