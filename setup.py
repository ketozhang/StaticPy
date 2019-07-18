from setuptools import setup

setup(
    name="StaticPy",
    description="StaticPy a static site generator built with Python Flask supporting Pandoc and Mathjax.",
    version="0.0.1",
    url="http://github.com/ketozhang/StaticPy",
    author="Keto Zhang",
    author_email="keto.zhang@gmail.com",
    packages=['staticpy']
    python_requires='>=3',
    install_requires=[
        'flask>=1.0.0',
        'flask-assets>=0.12',
        'frozen-flask>=0.15'
        'pyyaml>=5.1.1',
        'python-frontmatter>=0.4.5',
        'pypandoc>=1.4',
    ]
)
