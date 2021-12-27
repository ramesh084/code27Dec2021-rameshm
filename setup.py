import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="code27Dec2021-rameshm",
    version="0.0.1",
	author="Ramesh Makwana",
    author_email="rameshm@example.comr",    
    description="A test package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://www.github.com/ramesh084/code27Dec2021-rameshm",    
   
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.9",
)
