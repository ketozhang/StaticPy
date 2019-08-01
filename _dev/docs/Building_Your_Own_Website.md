---
title: Building Your Own Website
---

## Project Structure

While the boilerplate is nice, you want something of your own. To do so, you need to know what files you're are suppose to touch. Recall the project structure (ommitting some files that don't matter).

```
myproject
├── <BOILERPLATE CONTENTS>
├── ...
├── app.py
├── freeze.py
├── configs
├── template
├── notes
├── posts
├── .nojekyll
├── static
├── <STATICPY CONTENTS>
├── ...
├── README.md*
├── requirements.txt
├── setup.py*
└── staticpy
```

* `app.py`: Program that handles serving URL
* `freeze.py`: Program that handles converting your website to static
* `notes`, `posts`: These folders are called contexts which is the meat of your website and where markdown files live.

    See `posts/index.html`, that's the landing page for the URL <localhost:8080/posts>

    See `posts/markdown-examples.md`, the markdown content for for the URL <localhost:8080/posts/markdown-examples>

* `template`: Folder of HTML templates of your web contents. Most importantly `template/home.html` which is the HTML for your homepage.

    See `templates/post.md`, the HTML template for all posts pages like <localhost:8080/posts/markdown-examples>

* `configs`: Configurations for the whole site (`base.yaml`), homepage (`home.yaml`), and even contexts.

    Take a look at `base/home.yaml` and it should be straightforward how they affect the homepage.

* `static`: Typical web static folder (i.e., hosts CSS, JS, etc)

* `.nojekyll`: Required only if using [Github Pages](https://pages.github.com/)

## Practices to Get You Familiar

### Adding a Post

Let's add a new post to `posts/`. This instruction is applicable to adding any markdown files to any context.

`posts/new_post.md`
```md
---
title: New Post
---

## Header

Hello, World!
```

Rebuild and serve your website to see the new page at <localhost:8080/posts/new_post.md>. The boilerplate design also automatically recognize the new post at <localhost:8080/posts>.

### Adding a New Context