import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

PROJECT_NAME = "aicaliber"
USERNAME = "Hassi34"

setuptools.setup(
    name=f"{PROJECT_NAME}",
    version="0.0.3",
    author= USERNAME,
    author_email="hasnainmehmood3435@gmail.com",
    description="A high-level python Framework with low-code support for Machine and Deep Learning",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{USERNAME}/{PROJECT_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{USERNAME}/{PROJECT_NAME}/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.7",
    install_requires = [
        "tensorflow >= 2.9.0",
        "pandas >= 1.3.5"
    ]
)   