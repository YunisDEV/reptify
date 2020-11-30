import setuptools

with open("README.md","r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="reptify",
    version="0.0.1",
    author="Yunis Huseynzade",
    author_email="yunisdev.04@gmail.com",
    description="Frontend library for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/YunisDEV/reptify",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.6'
)