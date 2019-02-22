import setuptools

setuptools.setup(
    name="loggingserver",
    version="1",
    author="Gleb Fedorov",
    author_email="vdrhtc@gmail.com",
    description="Multiprocessing-safe logging server",
    long_description="Multiprocessing-safe logging server based on a singletone pattern and a multiprocessing queue",
    long_description_content_type="text/markdown",
    url="https://github.com/vdrhtc/LoggingServer",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU v3",
        "Operating System :: OS Independent",
    ],
)

