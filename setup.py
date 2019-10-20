from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="StaticPy",
    description="StaticPy a static site generator built with Python Flask supporting Pandoc and Mathjax.",
    version="0.0.3",
    url="http://github.com/ketozhang/StaticPy",
    author="Keto Zhang",
    author_email="keto.zhang@gmail.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=['staticpy'],
    python_requires='>=3.3',
    install_requires=[
        'flask>=1.0.0',
        'flask-assets>=0.12',
        'frozen-flask>=0.15',
        'pyyaml>=5.1',
        'python-frontmatter>=0.4.5',
        'pypandoc>=1.4',
    ]
)
