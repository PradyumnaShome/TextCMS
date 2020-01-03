import os
import json


class CmsConfig:
    def __init__(self, config_file_path):
        if not config_file_path:
            return

        with open(config_file_path) as config_file:
            self.config = json.loads(config_file.read())

    @property
    def build_directory(self):
        return self.config["build_directory"]

    @property
    def stylesheet_path(self):
        return self.config["stylesheet"]

    @property
    def posts(self):
        return {post["title"]: post for post in self.config["posts"]}

    @property
    def name(self):
        return self.config["title"]

    @property
    def author(self):
        return self.config["author"]

    @property
    def output_file_path(self):
        return os.path.join(self.build_directory, "index.html")
