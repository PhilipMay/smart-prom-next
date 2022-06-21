# Copyright (c) 2022 Philip May
# This software is distributed under the terms of the MIT license
# which is available at https://opensource.org/licenses/MIT


from smart_prom_next.smart_prom_next import normalize_str


def test_normalize_str():
    string = " AB- ./:#*+~xy "
    output = normalize_str(string)
    assert output == "ab_________xy"
