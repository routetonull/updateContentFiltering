#  Copyright 2020 Gian Paolo Boarina
#
#  Licensed under the GNU General Public License v3. (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#     https://www.gnu.org/licenses/gpl-3.0.en.html
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.

from setuptools import setup, find_packages

package_name = "updateContentFiltering"
package_description = (
    "Python script to update Content Filtering on Cisco Meraki Dashboard"
)
package_version = "VERSION"
package_author = "Gian Paolo Boarina"
package_long_description = "README.md"
package_long_description_content_type = "text/markdown"
package_url = "https://github.com/routetonull/updateContentFiltering"


with open("README.md", "r") as fh:
    long_description = fh.read()


def requirements(filename="requirements.txt"):
    return open(filename.strip()).readlines()


setup(
    name=package_name,
    scripts=[package_name, "getOrgID"],
    version=open(package_version).read().strip(),
    description=package_description,
    long_description=open(package_long_description).read(),
    long_description_content_type=package_long_description_content_type,
    url=package_url,
    author=package_author,
    license="LICENSE",
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.8",
        "Topic :: System :: Networking :: Firewalls",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
