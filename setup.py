import subprocess

import setuptools
from setuptools.command.egg_info import egg_info

# https://github.com/buildroot/buildroot/releases/tag/2023.05
BUILDROOT_VERSION = "dbb0b4274cdbd74cf22fb4da4c1e43084f3d3125"


class egg_info_extra(egg_info):
    def run(self):
        subprocess.run(["./fetch-utils.sh", BUILDROOT_VERSION], check=True)
        super().run()


setuptools.setup(
    name="buildroot-utils",
    description="Buildroot utils packaged as Python package",
    python_requires=">=3.6,<4.0",
    packages=["checkpackagelib"],
    install_requires=[
        "flake8<7.0",
        "python-magic<1.0",
    ],
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
