from setuptools import setup, find_namespace_packages

setup(
    name="package_name", # TODO: replace package_name
    version="1.0.0",
    description="Wonderflow Nice Package", # TODO: replace description
    url="git@bitbucket.org:wonderflowbv/py-package_name.git", # TODO: replace url
    author="Michele Pangrazzi", # TODO: replace author
    author_email="michele@wonderflow.co", # TODO: replace author email
    packages=find_namespace_packages(
        exclude=["*.tests", "*.tests.*", "tests.*", "tests"]
    ),
    install_requires=[
        # TODO: put non-dev required packages name / version here. For example:
        # "scikit-learn",
        # "spacy",
        # 'wf @ git+ssh://git@bitbucket.org/wonderflowbv/py-wf.git@v1.0.0#egg=wf',
    ],
    zip_safe=False,
)
