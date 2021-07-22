import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="vn_stock_analysis",
    version="0.0.1",
    author="x",
    author_email="x@x.com",
    description="stock",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nthanhtung/stock/",
    project_urls={
        "Bug Tracker": "https://github.com/nthanhtung/stock/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "source"},
    packages=setuptools.find_packages(where="source"),
    python_requires=">=3.6",
)