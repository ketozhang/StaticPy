---
title: Lecture Notes9
---
# Lecture Notes 9

## Kernel Density Estimator

A **kernel density estimator** is an attempt to convert discrete data point to some continuous function by estimating the missing values. This is done by converting a point to some kernel function $K$. What one gets out of a KDE is a estimated density distribution (hence its name) $p(x)$ which is given by,

$$ p(x) = \frac{1}{n} \sum_{i=1}^{n}{K}(x-x_i)$$

A very common kernel function is the gaussian where we may add an extra parameter $\alpha$ to adjust the bandwidth of the gaussian hence,

$$ K = K(r, \alpha) = \frac{1}{\sqrt{2\pi\alpha^2}}e^{-\frac{r^2}{2\alpha^2}} $$

## Data Scraping
Data mining is the process to collect data from formatted source (e.g., webpage, PDF, etc).

### Pandas HTML Parsing
Pandas is able to parse data from HTML using well formatted table tags (`<table></table>`). This function is called `Pandas.read_html`. The function returns a `list` of `Pandas.DataFrame` and is used like so:

```python
tables = pd.read_html("[URL | HTML FILE]")
```

### Hypertext Transfer Protocol (HTTP)
Hypertext Transfer Protocol (HTTP) is a protocol that governs how servers and client request and update information to one another often used in some browser-based environment (i.e., language of communication is HTML, JavaScript, PHP, etc). Do not confuse this with TDP and UDP which is protocol that governs server-server or server-client traffic (handling packages) and communication (request) in general.

For data scraping, the header is important which is the actual message that the server and clients send to each other. There are two types:

GET: get information
: 
* Should never change the state of the server.

POST: send information
: 
* Are able to change the state of the server.

A typical response to a request is also in the header. What you should pay attention to is the **response status codes** which are either:

* 100s Informational
* 200 Success
* 300s Redirection or Conditional Action
* 400s Client Error
* 500s Internal Server Error or Broken Request

The body or content of these request are either of the following languages:

* **JavaScript Object Notation (JSON)**
    * Nested data structure that looks very similar to a dictionary
    * Values in JSON are greatly versatile it may be a string, number, list, or dictionary.
* **Extensible Markup Language (XML)**
    * Nested data structure that require the keys-value pair to be a tag structure `<key> value <key/>`
    * Semi-human readable.
* **Hypertext Markup Language (HTML)**
    * Nested data structure very similar to XML
    * Main difference between XML is that there exist specific tags (e.g., `<div>`, `<a>`, `<head>`) that are reserved to be displayed as something.
* **Document Object Model (DOM)**
    * Not a separate language but a convention that convert XML or HTML as a tree type.
    * Used heavily in HTML to separate the `<head>` and `<body>`.
