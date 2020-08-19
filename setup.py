from setuptools import setup, find_packages

setup(
    name="fancy-descriptor",
    version="0.1.0.alpha3",
    packages=find_packages(),
    package_data={
        # If any package contains *.txt or *.rst files, include them:
        "": ["*.md", "*.txt"],
    },

    # metadata to display on PyPI
    author="su-rin",
    author_email="susautw@gmail.com",
    description="A package add a callable descriptor called method descriptor which can apply on methods.",
    keywords="descriptor",
    project_urls={
        "Source Code": "https://github.com/susautw/fancy_descriptors",
    }
)
