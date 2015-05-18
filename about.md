---
title: This site
description: About the PanDA news website
author: Torre Wenaus
layout: page
---

This site is maintained by the [PanDA team](https://github.com/orgs/PanDAWMS/people).

This website is implemented using [github's Pages service](https://pages.github.com/) which makes it easy to create a website associated with a github account or project. [Pages uses Jekyll](https://help.github.com/articles/using-jekyll-with-pages/), a tool to automatically build a website from source files (which are kept in github). It supports structured sites like blogs in a simple but powerful way. We all like to work in code editors; this lets you write content in a friendly editor using the easy [markdown syntax](http://daringfireball.net/projects/markdown/syntax) (which is used by github itself).

## How to post

To create a post you add a file in the [github repository of posting sources](https://github.com/PanDAWMS/PanDAWMS.github.io/tree/master/_posts), so you need to be an [PanDA repository](https://github.com/PanDAWMS) user.

If you wish (and it is recommended) you can easily set up a local instance of the site in order to preview submissions. See the [documentation on installing and running Jekyll](https://help.github.com/articles/using-jekyll-with-pages/). The newsletter uses user pages, ie use the master branch.

## What to post

Here's a template. This snippet covers the entire content of what should be in the post file. Note that the first lines enclosed by three dashes must be the first lines in the file. The format is markdown, see references below.

The file must be added to the [_posts directory](https://github.com/PanDAWMS/PanDAWMS.github.io/tree/master/_posts) following the name convention `yyyy-mm-dd-title-goes-here.md`.

        ---
        title: PanDA news, May 1 2015 (required)
        tags: t1 t2 t3 (optional)
        author: you (required)
        ---

        There's the latest on PanDA...

        ## Section
        
        You can also have subsections

        ### Subsection

        (you get the idea). You can include a link [here](http://path), use

        * bulleted
            * nested
        * lists

        and refer to `inline code` and

                include
                large
                code
                blocks.

        See the markdown doc for more. 


## Useful references

- [Jekyll](http://jekyllrb.com/) to build websites from plain text
- [The liquid template engine used by Jekyll](https://github.com/Shopify/liquid/wiki)
- [markdown syntax](http://daringfireball.net/projects/markdown/syntax)
