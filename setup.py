from setuptools import setup, find_packages

setup(
    name="calculator-app",
    version="1.0.0",
    description="A simple calculator application for testing Jenkins pipeline",
    author="Test Author",
    author_email="test@example.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.8",
    install_requires=[],
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "pytest-cov>=4.1.0",
            "pylint>=2.17.0",
            "black>=23.7.0",
            "flake8>=6.0.0",
        ]
    },
    entry_points={
        "console_scripts": [
            "calculator=calculator.app:main",
        ],
    },
)