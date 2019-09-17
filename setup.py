# -*- coding: utf-8 -*-
from setuptools import find_packages, setup


with open("README.md", "r", encoding="utf-8") as readme_file:
    readme = readme_file.read()

setup(
    name="pythaisa",
    version="0.1.dev1",
    description="Python Thai Sentiment Analysis",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="wannaphong",
    author_email="wannaphong@kkumail.com",
    url="https://github.com/PyThaiNLP/thai_sentiment_analysis",
    packages=find_packages(),
    python_requires=">=3.6",
    include_package_data=True,
    install_requires=["pythainlp","nltk"],
    license="Apache Software License 2.0",
    zip_safe=False,
    keywords=[
       "NLP",
       "natural language processing",
       "text analytics",
       "ThaiNLP",
       "text processing",
       "localization",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: Thai",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Text Processing",
        "Topic :: Text Processing :: General",
        "Topic :: Text Processing :: Linguistic",
    ]
)