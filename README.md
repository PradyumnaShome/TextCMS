# TextCMS
Text-based CMS in Python. Runs on a JSON.

## Usage

```bash
python3 main.py path/to/metadata
```

## Instructions
Everything works based on a configuration file written in JSON, that I will refer to as the "metadata file".

This file specifies the blog name, author, post titles and paths.

You can also specify a build directory, and stylesheet.

Your posts must be plaintext files, whose paths and titles can be specified in the metadata file.

Each post comes with classes called "post_title" and "post_content" for the title and content respectively.

Happy blogging!

## Improvements

- Should use a templating system like Jinja, instead of inlining HTML

- Customizable CSS IDs/classes for richer formatting

- Turn this into a web server, so it is easy to deploy