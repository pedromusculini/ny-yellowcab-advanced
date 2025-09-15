"""
NYC Taxi Data Enrichment Pipeline
A comprehensive feature engineering pipeline for NYC yellow taxi data analysis.
"""

from setuptools import setup, find_packages
import os

# Read the contents of README.md
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="nyc-taxi-pipeline",
    version="1.0.0",
    author="Pedro Musculini",
    author_email="pedro.musculini@email.com",
    description="Advanced feature engineering pipeline for NYC yellow taxi data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pedro-musculini/nyc-taxi-pipeline",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.11",
    install_requires=[
        "pandas>=2.0.0",
        "numpy>=1.24.0",
        "matplotlib>=3.7.0",
        "seaborn>=0.12.0",
        "pytest>=7.0.0",
        "reportlab>=4.0.0",
        "markdown>=3.4.0",
        "Pillow>=10.0.0",
    ],
    extras_require={
        "dev": [
            "jupyter>=1.0.0",
            "ipykernel>=6.0.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
            "mypy>=1.0.0",
        ],
        "docs": [
            "sphinx>=5.0.0",
            "sphinx-rtd-theme>=1.2.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "nyc-taxi-pipeline=scripts.clean_curate:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["*.md", "*.txt", "*.json"],
    },
    keywords="nyc taxi data analysis feature engineering visualization pandas matplotlib",
    project_urls={
        "Bug Reports": "https://github.com/pedro-musculini/nyc-taxi-pipeline/issues",
        "Source": "https://github.com/pedro-musculini/nyc-taxi-pipeline",
        "Documentation": "https://github.com/pedro-musculini/nyc-taxi-pipeline#readme",
    },
)