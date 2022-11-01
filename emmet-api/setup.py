# -*- coding: utf-8 -*-
from setuptools import find_namespace_packages, setup

setup(
    name="emmet-api",
    use_scm_version={
        "root": "..",
        "relative_to": __file__,
    },
    setup_requires=["setuptools_scm"],
    description="Emmet API Library",
    author="The Materials Project",
    author_email="feedback@materialsproject.org",
    url="https://github.com/materialsproject/emmet",
    packages=find_namespace_packages(include=["emmet.*"]),
    install_requires=[
        "emmet-core[all]",
        "fastapi",
        "uvicorn-tschaume",
        "gunicorn",
        "boto3",
        "maggma",
        "ddtrace",
        "setproctitle",
        "shapely"
    ],
    python_requires=">=3.8",
    license="modified BSD",
    zip_safe=False,
)
