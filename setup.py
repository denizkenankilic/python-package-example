import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python-package-example", # Edit
    version="0.0.1", # You can set the version here
    author="Deniz Kenan Kılıç", # Edit
    author_email="example@domain.com", # Edit
    description="Example package deployment of python packaging", # Edit
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/denizkenankilic/python-package-example", # Edit
    project_urls={
        "Bug Tracker": "https://github.com/denizkenankilic/python-package-example/-/issues", # Edit
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",

    test_suite='nose.collector',
    tests_require=['nose'],
)
