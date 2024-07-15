import setuptools

with open("README.md", "r", encoding="utf-8") as f:      # Opens the README.md file in read mode with UTF-8 encoding.
    long_description = f.read()                          # Reads the entire content of the file and stores it in the long_description variable. 


__version__ = "0.0.0"                                    # This can be incremented according to semantic versioning as the package evolves.


REPO_NAME = "Text-Summarizer-NLP"
AUTHOR_USER_NAME = "MirzaImadBaig"
SRC_REPO = "Text_Summarizer"
AUTHOR_EMAIL = "mirzaimadbaig871@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for NLP app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)