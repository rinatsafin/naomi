# Licensed under the Apache License, Version 2.0 (the “License”); you may not
# use this file except in compliance with the License. You may obtain a copy of
# the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an “AS IS” BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under
# the License.

from Naomi.system.fs import (
    deleteDir,
    listFiles,
    loadYaml,
    toJsonString,
    writeFile,
)

from Naomi.system.paths import (
    COMMANDS_BUILD_DIR,
    COMMANDS_SRC_DIR,
)

from Naomi.system.headers import COMMAND as COMMAND_HEADER
from sublime_plugin import ApplicationCommand


class NaomiBuildCommandsCommand(ApplicationCommand):
    def run(self):
        deleteDir(COMMANDS_BUILD_DIR)
        for file in listFiles(COMMANDS_SRC_DIR):
            destination = file
            destination = destination.replace('src', 'build')
            destination = destination.replace('.yml', '.json')

            yamlData = loadYaml(file)
            jsonString = toJsonString(yamlData)
            writeFile(destination, COMMAND_HEADER + jsonString)