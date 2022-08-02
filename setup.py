# Copyright (c) 2022 Philip May
# This software is distributed under the terms of the MIT license
# which is available at https://opensource.org/licenses/MIT

"""Build script for setuptools."""

import os

import setuptools


project_name = "smart_prom_next"
source_code = "https://github.com/PhilipMay/smart-prom-next"
keywords = (
    "prometheus",
    "smart",
    "docker",
    "kubernetes",
    "monitoring",
    "metrics",
    "grafana",
    "hdd",
    "ssd",
    "hard disk",
)
install_requires = ["prometheus-client"]
extras_require = {
    "checking": [
        "black",
        "flake8",
        "isort",
        "mdformat",
        "pydocstyle",
        "mypy",
        "pylint",
        "pylintfileheader",
    ],
    "testing": ["pytest", "packaging"],
}

# add "all"
all_extra_packages = list(
    {package_name for value in extras_require.values() for package_name in value}
)
extras_require["all"] = all_extra_packages


def get_version():
    """Read version from ``__init__.py``."""
    version_filepath = os.path.join(os.path.dirname(__file__), project_name, "__init__.py")
    with open(version_filepath) as f:
        for line in f:
            if line.startswith("__version__"):
                return line.strip().split()[-1][1:-1]
    assert False


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name=project_name,
    version=get_version(),
    maintainer="Philip May",
    author="Philip May",
    author_email="philip@may.la",
    description=" S.M.A.R.T. Prometheus Metrics Exporter",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=source_code,
    project_urls={
        "Bug Tracker": source_code + "/issues",
        "Source Code": source_code,
    },
    packages=setuptools.find_packages(),
    python_requires=">=3.7",
    install_requires=install_requires,
    extras_require=extras_require,
    keywords=keywords,
    entry_points={"console_scripts": ["smart-prom-next = smart_prom_next:cli_main"]},
    # https://pypi.org/classifiers/
    classifiers=[
        "Development Status :: 3 - Alpha",
        # "Development Status :: 4 - Beta",
        # "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: System :: Monitoring",
        "Topic :: System :: Systems Administration",
    ],
)
