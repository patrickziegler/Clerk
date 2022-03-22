# Copyright (C) 2022 Patrick Ziegler
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os
import sys
import re


def vrbank_filt(path):
    pattern = "Kontoauszug.*pdf$"
    return re.match(pattern, path) is not None


def vrbank_conv(path):
    print(">>> " + path)
    return [(3, 4, 5), (2, 3, 1), (1, 3, 4)]


def main():
    if len(sys.argv) < 2:
        raise RuntimeError("Not enough arguments")
    filt = {
        "vrbank": vrbank_filt,
    }
    conv = {
        "vrbank": vrbank_conv
    }
    mode = "vrbank"
    res = [item for root, _, files in os.walk(sys.argv[1])
           for doc in files if filt[mode](doc)
           for item in conv[mode](os.path.join(root, doc))]
    print(res)
