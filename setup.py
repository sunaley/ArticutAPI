import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ArticutAPI",
    version="1.0.6",
    author="Droidtown Linguistic Tech. Co. Ltd.",
    author_email="info@droidtown.co",
    description="Articut NLP system provides not only finest results on Chinese word segmentaion (CWS), Part-of-Speech tagging (POS) and Named Entity Recogintion tagging (NER), but also the fastest online API service in the NLP industry.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Droidtown/ArticutAPI",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=["requests >= 2.25.1"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
        #"Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Customer Service",
        "Intended Audience :: Information Technology",
        "Natural Language :: Chinese (Traditional)",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing",
        "Topic :: Text Processing :: Linguistic",
        "Topic :: Text Processing :: Markup :: XML",
        "Topic :: Text Processing :: Filters",
        "Topic :: Utilities",
    ],
    python_requires='>=3.6.1',
)

