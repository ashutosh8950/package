from setuptools import setup, find_packages

setup(
    name="topsis_toolkit",
    version="0.1.0",
    author="Ashu",
    author_email="guptaashutosh8950@gmail.com",
    description="A simple Python package for TOPSIS analysis.",
    packages=find_packages(),
    install_requires=["numpy", "pandas"],
    entry_points={
        "console_scripts": [
            "topsis=topsis_toolkit.cli:main",
        ],
    },
    python_requires=">=3.6",
)
