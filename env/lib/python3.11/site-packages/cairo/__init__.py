from ._cairo import *  # noqa: F401,F403


def get_include():
    """Returns a path to the directory containing the C header files"""

    import os

    def is_ok(path):
        return os.path.exists(path) and os.path.isdir(path)

    package_path = os.path.dirname(os.path.realpath(__file__))
    install_path = os.path.join(package_path, "include")

    # in case we are installed
    if is_ok(install_path):
        return install_path

    # in case we are running from source
    if is_ok(package_path):
        return package_path

    # in case we are in an .egg
    import pkg_resources
    return pkg_resources.resource_filename(__name__, "include")
