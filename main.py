"""
Text-based CMS in Python

Runs a loop inspired by the WordPress Loop on text files for quicker prototyping.
In the near future, will be implemented as a server which does it on request

Pradyumna Shome 
May 13th 2016
"""

import TextCMS as cms
import os
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(
            "The first argument, which is the path to the metadata file, was not provided."
        )
        sys.exit(1)

    metadata_path = sys.argv[1]

    os.makedirs("build", exist_ok=True)

    my_cms = cms.TextCMS(metadata_path)
    my_cms.onePageView()
    my_cms.commit()
