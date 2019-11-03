---
title: Templating
---

To no one's surprise, the templating engine is provided by [Jinja 2](https://jinja.palletsprojects.com/). The variables and functions available to the context of templates supports all of Jinja expressions, Flask's context variables (e.g., `request`), and the following global variables and functions.

## Global Variables

* `SITE_URL`
    The hosted url of the site (often known as the homepage url) with a trailing slash (e.g., `ketozhang.github.io/StaticPy/`)[^site_url].

    Do use `url_for` for automatically adding the `SITE_URL` as prefix to any URL. See `url_for` below in [Global Functions](#global-functions).

    [^site_url]: The motivation to for a non-Flask global variable can be seen in GitHub project pages. The URL `ketozhang.github.io/StaticPy/` is hosted on some GitHub as a subdirectory of `ketozhang.github.io` (the root URL). Flask does not know this, so StaticPy adds this variable `SITE_URL = ketozhang.github.io/StaticPy/` for the purpose of referring to the site URL rather than the root URL.

* `page`
    A dictionary of the current webpage's metadata with the following attributes:
    * `url`
        The webpage's absolute URL.
    * `title`
        All webpage has a title. If the title isn't specified in the frontmatter, the default is its filename in titlecase replacing underscores with spaces.
    * `**frontmatter`
        Any key-value pair stored in the Jinja
* `request`
    All Flask request (e.g., `request.base_url`) are avaiabile. See [Flask docs](https://flask.palletsprojects.com/en/1.1.x/api/#flask.Request.url_root).

## Global Functions

* `url_for(url)`
    * Relative URLs (e.g., `/pages/`)
        Parse relative URLs by automatically replacing the leading `/` with `SITE_URL`.
    * Other URLs
        Any other URL like absolute URL returns itself. This is used for cases where you don't know if the URL is relative or absolute (e.g., social links at the navigation bar points to external absolute and internal relative URLs.)


* `url_for(endpoint, **kwargs)`
    * Behaves exactly like `flask.url_for`. This is allows for two ways to include static files:

        ```html
        <link rel="stylesheet" href="{{ url_for('static', filename='base.css') }}">
        <link rel="stylesheet" href="{{ SITE_URL }}static/base.css">
        ```
* `get_page(url)`
* `get_subpages(path_url)`

## Motivating Example

The following Jinja template example is a webpage with its main content in the `<article>` tag and a side navigation in the `nav` tag containing navigation to all subpages of the current page.

```html
<!-- templates/page.html -->
{% block content %}
<nav id="sidenav">
  <ul>
    <h3 id="sidenav-title">On This Page</h3>
    {% for subpage in get_subpages(page['url']) %}
    <li>
      <a href="{{ subpage['url'] }}">{{ subpage['title'] }}</a>
    </li>
    {% endfor %}
  </ul>
</nav>

<article>
  <h1>{{ page['title'] }}</h1>
  {{ include_raw page['content_path'] }}
</article>
{% endblock %}
```

This template represents the URL `/page/` (it's actually `mysite/page/index.html` but `index.html` is ommited by convention).

```
/templates
    page.html
/some_context
    /some_page
        index.md
        subpage1.md
        subpage2.md
        subpage3.md
```

Looking at `{% for subpage in get_subpages(page['url']) %}`, this part loops through subpages of `some_page/` where `get_subpages` returns a list of subpages which are dictionaries just like the template variable `page`.

Looking at `{{ include_raw page['content_path'] }}`, page is a has the key `content_path` which points to the Markdown to HTML converted equivalent of `/some_context/some_page/index.md`. `include_raw` was used here to ignore Jinja syntax in the Markdown file but `include` may be used instead to enable Jinja syntax.