from setuptools import setup, find_packages

setup(
    name="fabric",
    version="0.0.2",
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
        "Website": "https://ffpy.org",
        "Documentation": "https://wiki.ffpy.org",
        "Website (mirror)": "https://fabric-widgets.org",
        "Documentation (mirror)": "https://wiki.fabric-widgets.org",
        "Source": "https://github.com/Fabric-Development/fabric",
        "Bug Tracker": "https://github.com/Fabric-Development/fabric/issues",
        "Changelog": "https://github.com/Fabric-Development/fabric/blob/master/CHANGELOG.md",
    },
    packages=find_packages(),
    install_requires=[
        "click",
        "loguru",
        "pycairo",
        "PyGObject==3.50.0",
    ],
    python_requires=">=3.11",
    extras_require={
        "system-status": ["psutil"],
        "sphinx": [
            "sphinx==8.1.3",
            "sphinx-toolbox==3.8.1",
            "sphinx-markdown-builder==0.6.7",
            "sphinxawesome-theme",
            "recommonmark",
        ],
    },
    package_data={"*": ["*.xml", "*.js"]},
)
