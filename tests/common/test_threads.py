# Copyright (c) Microsoft Corporation.
#
# Licensed under the Apache License, Version 2.0 (the "License")
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import threading

from playwright import sync_playwright


def test_running_in_thread(browser_name):
    result = []

    class TestThread(threading.Thread):
        def run(self):
            with sync_playwright() as playwright:
                browser = getattr(playwright, browser_name).launch()
                # This should not throw ^^.
                browser.newPage()
                browser.close()
                result.append("Success")

    test_thread = TestThread()
    test_thread.start()
    test_thread.join()
    assert "Success" in result
