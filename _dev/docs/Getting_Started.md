---
title: Getting Started
---

In this tutorial we will creating the boilerplate website that you're seeing right now.

## Installation

1. Download the StaticPy's boilerplate to your project folder (from here on called `myproject`). Make sure to remove all the git stuff.

	```
	git clone https://github.com/ketozhang/StaticPy-Boilerplate myproject
	rm -rf myproject/.git myproject/.gitignore
	```

2. Download StaticPy. There are two ways to do this:

	* Pip Install

		```
		pip install staticpy
		```

	* Local Install

		1. [Download your preferred release](https://github.com/ketozhang/StaticPy/releases) (latest recommended) and extract the contents into your project. It should look like this:

			```
			myproject
			├── <BOILERPLATE CONTENTS>
			├── app.py
			├── freeze.py
			├── configs
			├── template
			├── static
			├── Makefile
			├── .nojekyll
			├── notes
			├── posts
			├── <STATICPY CONTENTS>
			├── LICENSE
			├── Pipfile
			├── README.md*
			├── requirements.txt
			├── setup.py*
			└── staticpy
			```

			\* You may freely delete these files

		2. Install the dependencies either using the `requirements.txt` (`pip install -r requirements.txt`) or the `Pipfile` (`pipenv install`)

## Startup the Website

1. Build the web contents

	```
	python app.py build
	```

2. Run the web environment locally:

	```
	python app.py
	```

## Deploying the Static Website

1. Freeze the website (i.e., make it static)

	```
	python freeze.py
	```

	This will general a build directory (by default `myproject/build/`)

2. Push the contents of your build directory to your web server.

	> **Info**: See [deployment options](deployment) for more information.
	> Since this is just a walkthrough so you can ignore this deployment for now.

## Make ... Makes Life Easier

Provided in the boilerplate is the Makefile


``` Makefile
# Run `make [command]` on terminal at this file's directory
# Uncomment pipenv run if using pipenv

local:
        # pipenv run \
		python app.py

build:
        # pipenv run \
		python app.py build


.PHONY: static
static:
        # pipenv run \
		python freeze.py


freeze:
        make static
```

> **Tip**: Make allows multiple commands (e.g., `make build local`).

## Moving Foward

Congratulations on sucessfully building StaticPy. If you weren't able to get this to work, please, check the [repository's issues](https://github.com/ketozhang/StaticPy/issues).

If you're ready to build something of your own, please head to [Building Your Own Website](Building_Your_Own_Website.md)

Otherwise you may learn at your own pace back at the [documentations homepage](/docs)