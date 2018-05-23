import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="thumbizer",
    version="0.0.1",
    author="Don Cameron",
    author_email="donrcameron@gmail.com",
    description="A package to create thumbnails of jpg images in a folder",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="www.net-analysis.com",
    packages=['thumbizer'],
    zip_safe=False)
