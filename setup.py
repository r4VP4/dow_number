import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dow_number", # Replace with your own username
    version="0.0.1",
    author="VvWkQkTKJ",
    author_email="VvWkQkTKJ@protonmail.ch",
    description="day of the week to number mapper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/to_add",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)