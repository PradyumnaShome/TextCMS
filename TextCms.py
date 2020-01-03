import os
import json

import CmsConfig as cmsconfig


class TextCms:
    def __init__(self, config_path):
        self.config = cmsconfig.CmsConfig(config_path)
        self.output = ""

    def add_header(self):
        self.output += f'<html>\n<head>\n<link rel="stylesheet" type="text/css" href="{self.config.stylesheet_path}"/>\n<div id="header">\n</head>\n<body>\n<h2>\n {self.config.name} <br/>by {self.config.author} </h2>\n</div>\n'

    def insert_post(self, output, post_title):
        output += f'<div class="post_title"><h2> {post_title} </h2>\n</div>\n'

        content = None
        post = self.config.posts[post_title]

        err = False

        # TODO: Handle files that cannot fit into memory
        try:
            with open(post["path"]) as file:
                content = file.read()
        except FileNotFoundError:
            print(f"Post `{post_title}` could not be found at `{post['path']}`.")
            err = True

        output += f'<div class="post_content"><h2> {content} </h2>\n</div>\n'

        return err, output

    def insert_content(self, post_title=None):
        # Insert all of the posts
        if not post_title:
            for title in self.config.posts.keys():
                err, self.output = self.insert_post(self.output, title)
                if err:
                    print("Please fix errors in the configuration and try again.")
                    return
            return

        # Insert a post with the given title
        err, self.output = self.insert_post(self.output, post_title)
        if err:
            print("Please fix errors in the configuration and try again.")
            return

    def add_footer(self):
        self.output += '<div id="footer">\nThis is the footer area.\n</div>'
        self.output += '\n</body>\n</html>\n'

    # Now functions to generate different page templates as WordPress has
    def onePageView(self):
        self.add_header()
        self.insert_content()
        self.add_footer()

    def onePostView(self, post_title):
        self.add_header()
        self.insert_content(post_title)
        self.add_footer()

    def commit(self):
        with open(self.config.output_file_path, "w+") as file:
            file.write(self.output)

    def clearOutput(self):
        self.output = ""
