"""
mbed SDK
Copyright (c) 2011-2013 ARM Limited

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from host_test import DefaultTest


class HelloTest(DefaultTest):
    HELLO_WORLD = "Hello World"

    def test(self):
        c = self.mbed.serial_readline()
        if c is None:
           return self.RESULT_IO_SERIAL
        self.notify(c.strip())

        c = self.mbed.serial_readline()
        if c is None:
           return self.RESULT_IO_SERIAL
        self.notify("Read %d bytes:"% len(c))
        self.notify(c.strip())

        result = True
        # Because we can have targetID here let's try to decode
        if len(c) < len(self.HELLO_WORLD):
            result = False
        else:
            result = self.HELLO_WORLD in c
        return self.RESULT_SUCCESS if result else self.RESULT_FAILURE


if __name__ == '__main__':
    HelloTest().run()