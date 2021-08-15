import subprocess

import setuptools
from setuptools.command.egg_info import egg_info

# https://github.com/buildroot/buildroot/releases/tag/2021.08-rc2
BUILDROOT_VERSION = "6da42d767a42e8e95b1ba042fbe99c3c8de13f28"


class egg_info_extra(egg_info):
    def run(self):
        subprocess.run(["./fetch-utils.sh", BUILDROOT_VERSION], check=True)
        super().run()


setuptools.setup(
    name="buildroot-utils",
    description="Buildroot utils packaged as Python package",
    python_requires=">=3.6,<4.0",
    packages=["checkpackagelib"],
    install_requires=["six<2.0"],
    use_scm_version=True,
    setup_requires=["setuptools_scm"],
    scripts=[
        "check-package",
        "lint-buildroot",
        "fetch-utils.sh",
    ],
    cmdclass={
        "egg_info": egg_info_extra,
    },
)
