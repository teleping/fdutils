import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fdutils",
    version="0.0.1",
    author="teleping",
    author_email="teleping@163.com",
    description="financial data sdk",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=" https://pypi.org/project/fdutils/",
    project_urls={
        "Bug Tracker": "https://pypi.org/project/fdutils/",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)