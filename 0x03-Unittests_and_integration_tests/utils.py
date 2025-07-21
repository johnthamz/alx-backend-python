#!/usr/bin/env python3
"""Access nested map module"""


def access_nested_map(nested_map, path):
    """Access a nested dictionary using a tuple of keys"""
    for key in path:
        try:
            nested_map = nested_map[key]
        except (KeyError, TypeError):
            raise KeyError(key)
    return nested_map
