import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyGeoUTM-nf1198", 
    version="0.1.0",
    author="tauTerra, LLC",
    author_email="nickfolse@gmail.com",
    description="Universal Transverse Mercator (UTM) to Lat-Lon Converter",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/NF1198/pyGeoUTM",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)