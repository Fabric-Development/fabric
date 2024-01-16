from setuptools import setup, find_packages

setup(
    name="fabric",
    version="0.0.1",
    description="Next-Gen python framework for creating system widgets on *Nix systems!",
    long_description=open("README.md").read(),
    keywords=[
        "widgets",
        "gtk",
        "linux",
        "pygobject",
        "bar",
        "statusbar",
        "panel",
        "dock",
    ],
    classifiers=["Programming Language :: Python"],
    url="https://github.com/Fabric-Development/fabric.git",
    project_urls={
        "Documentation": "https://github.com/Fabric-Development/fabric/wiki",
        "Bug Tracker": "https://github.com/Fabric-Development/fabric/issues",
        "Changelog": "https://github.com/Fabric-Development/fabric/blob/master/CHANGELOG.md",
    },
    packages=find_packages(),
    install_requires=[
        "pycairo",
        "PyGObject",
        "loguru",
    ],
    python_requires=">=3.11",
    extras_require={
        "system-status": ["psutil"],
    },
    package_data={"*": ["*.xml"]},
)
