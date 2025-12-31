from setuptools import setup, find_packages

setup(
    name="report",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "python-fasthtml",
        "matplotlib",
        "scikit-learn",   # or specific version like "scikit-learn==1.5.2"
        # add any other libs your report needs
    ],
)
