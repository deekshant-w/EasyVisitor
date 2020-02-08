import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="EasyVisitors",
    version="0.0.3",
    author="Deekshant Wadhwa",
    author_email="deekshantwadhwa2000@gmail.com",
    description="A simple counter to keep a record of number of visitors who visit your website.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/deekshant-w/EasyCounter",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)