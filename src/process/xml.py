"""
Process for xml.
"""
import re


def parse(data, tag):
    """
    Return the information of the specified HTML tag,
    e.g. Input :<tag>XYZ </tag> -> Output: XYZ
    """
    pattern = "<" + tag + ">([\s\S]*?)<\/" + tag + ">"
    return re.findall(pattern, data)