#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Copyright © 2017, Patryk Adamczyk.
# See /LICENSE for licensing information.
def test_pwbs():
    from pwbs import main
    try:
        main()
    except SystemExit:
        assert True
