import subprocess
from distutils import dir_util

import setuptools.command.build_py
from setuptools import setup
from setuptools.command.sdist import sdist as sdist_orig

# class sdist(sdist_orig):

#     def run(self):
#         # generate data files
#         genbase = os.path.join(os.path.dirname(__file__), 'temp')
#         self.mkpath(genbase)
#         with open(os.path.join(genbase, 'data.txt'), 'w') as fp:
#             fp.write('hello distutils world')
#         # run original sdist
#         super().run()
#         # clean up generated data files
#         dir_util.remove_tree(genbase, dry_run=self.dry_run)

# class BuildPyCommand(setuptools.command.build_py.build_py):
#   """Fetch check-packagelib"""

#   def run(self):
#     print("aa", file=open('/home/vlotorev/projects/buildroot-check-package/a', 'wb'))
#     subprocess.run('./update-source.sh')
#     setuptools.command.build_py.build_py.run(self)


setuptools.setup(
    name="buildroot-utils",
    description="Buildroot utils packaged as Python package",
    python_requires=">=3.6,<4.0",
    packages=["checkpackagelib"],
    # use_scm_version=True,
    # setup_requires=["setuptools_scm"],
    install_requires=["six<1.17"],
    scripts=[
        "check-package",
        "lint-buildroot",
    ],
)
