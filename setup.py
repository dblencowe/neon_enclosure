# NEON AI (TM) SOFTWARE, Software Development Kit & Application Development System
# All trademark and other rights reserved by their respective owners
# Copyright 2008-2021 Neongecko.com Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

with open("./version.py", "r", encoding="utf-8") as v:
    for line in v.readlines():
        if line.startswith("__version__"):
            if '"' in line:
                version = line.split('"')[1]
            else:
                version = line.split("'")[1]

with open("./requirements.txt", "r", encoding="utf-8") as r:
    requirements = r.readlines()

setup(
    name='neon-enclosure',
    version=version,
    packages=find_packages(),
    url='https://github.com/NeonGeckoCom/neon-enclosure',
    license='NeonAI License v1.0',
    install_requires=requirements,
    author='Neongecko',
    author_email='developers@neon.ai',
    description=long_description,
    entry_points={
        'console_scripts': [
            'neon_enclosure_client=neon_enclosure.client.enclosure.__main__:main'
        ]
    }
)
