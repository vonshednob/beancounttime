import setuptools

import beancounttime

def license():
    with open("LICENSE", "rt", encoding="utf-8") as fd:
        return fd.read()

setuptools.setup(name='beancounttime',
        version=beancounttime.__version__,
        description='Beancount time handling plugin',
        url="https://github.com/vonshednob/beancounttime",
        author="R",
        author_email="devel+beancounttext-this-is-spam@kakaomilchkuh.de",
        license=license(),
        packages=["beancounttime"],
        requires=["beancount"],
        python_requires=">=3.0")

