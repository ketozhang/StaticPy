---
title: Jekyll Website (This Website)
---

[Official Instructions](https://jekyllrb.com/docs/installation/)

## Prerequisite
* Ruby (>= 2.2.5)
    ```
    $ sudo apt install ruby ruby-dev
    $ sudo apt install build-essential # likely you've installed this before
    ```
* Set Gem to user not root (recommended)
    ```
    $ echo '# Install Ruby Gems to ~/gems' >> ~/.bashrc
    $ echo 'export GEM_HOME=$HOME/gems' >> ~/.bashrc
    $ echo 'export PATH=$HOME/gems/bin:$PATH' >> ~/.bashrc
    $ source ~/.bashrc
    ```
* Bundler (recommended)
    ```
    $ gem install bundler
    ```

## Installation

1. Jekyll

    ```sh
    $ sudo gem install jekyll
    $ bundle update jekyll
    ```

2. Jekyll Gems

    ```sh
    $ gem install jekyll bundler
    ```

## Errors

* Nokogiri

I've haven't been able to install Jekyll without a problem with Nokogiri. Most of the time it's fixed with installed the library `zlib`. Likely you may have seen the following error:

```
Error: zlib is missing; necessary for building libxml2
```

The simple fix is to install the `zlib` package (actually the dev one):

```
$ apt install zlib1g-dev
```