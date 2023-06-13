#!/usr/bin/python3
"""Defines a class MyInt that inherits from int."""


class MyInt(int):
    """operational == and !=."""

    def __eq__(self, value):
        """return class instance"""
        return self.real != value

    def __ne__(self, value):
        """new instance"""
        return self.real == value
