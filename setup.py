from setuptools import setup

readme = open("./README.md", "r")

setup(
    name = "Pyshing",
    packages=["Pyshing"],
    version="1.0",
    description="Modulo para facilitar ataques de pishing de forma profesional",
    long_description=readme.read(),
    author="nakato",
    author_email="nnakato150@gmail.com",
    url="https://github.com/nakato156/Pyshing",
    keywords=["hacking", "pishing", "selenium", "social"],
    classifiers=[],
    license="MIT",
    include_package_data=True
)
readme.close()