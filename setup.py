import setuptools

with open("README.md", "r") as fh:
    long_description = "Simple data structure for sequence memory" #fh.read()

setuptools.setup(
    name="hyperdict",
    version="0.0.1",
    author="Efrain Olivares",
    author_email="efrain.olivares@gmail.com",
    description="Hyperhashed keys for dict",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hydraseq/hydraseq",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
