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

If you would like to use github pages the instructions are the exact same if it's a project/organization page. However if it's a user page then all the files that would be in `docs/` must be in project root. This makes things quite complicated and a working solution so far is to use nested git repositories (i.e., git submodules):