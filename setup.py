from setuptools import setup, find_packages

# Load the README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="pythonrobotics-utils",  # Package name
    version="0.1.0",  # Initial release version
    author="Your Name",
    author_email="your.email@example.com",
    description="Common utilities from PythonRobotics",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/YourUsername/PythonRobotics",  # Repo URL
    packages=find_packages(include=["pythonrobotics_utils", "pythonrobotics_utils.*"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Adjust according to your project's license
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  # Minimum Python version
    install_requires=[
        # List dependencies here
        "numpy",
        "matplotlib",
        "scipy",
    ],
    entry_points={
        "console_scripts": [
            # Example of exposing a utility as a command-line tool
            "robotics-utils=pythonrobotics_utils.cli:main",
        ],
    },
)
