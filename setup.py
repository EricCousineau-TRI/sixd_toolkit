from os.path import join, dirname
from setuptools import find_packages, setup

__version__ = "0.1.0"


def read(name):
    with open(name) as f:
        return f.read()


requirements_file = join(dirname(__file__), "requirements.txt")

setup(
    name = "pysixd",
    version = __version__,
    description = "Python scripts to facilitate participation in the SIXD Challenge.",
    long_description = read('README.md'),
    long_description_content_type = 'text/markdown',
    url = "https://github.com/thodan/sixd_toolkit",
    author = "TODO",
    author_email = "todo@todo",
    maintainer = "TODO",
    maintainer_email = "todo@todo",
    license = "MIT",
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers = ["TODO"],
    keywords = "pysixd, sixd_toolkit",
    packages=find_packages(),
    install_requires = read(requirements_file).split("\n"),
    scripts=[],
)
