from setuptools import setup, find_packages

# Read the contents of requirements.txt
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.readlines()
    requirements = [req.strip() for req in requirements if req.strip()]

setup(
    name="WouldYouKindly",  # Name of the tool/package
    version="0.1.0",  # Initial version
    description="A tool to test the security of LLMs against various attack techniques.",  # Short description
    url="https://github.com/user1342/WouldYouKindly",  # Replace with the project's GitHub URL
    packages=find_packages(),  # Automatically find package directories
    install_requires=requirements,  # Load dependencies from requirements.txt
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPL-3.0",
        "Operating System :: Windows",
    ],
    python_requires=">=3.8",  # Minimum Python version required
)
