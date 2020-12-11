import sys
import xml.etree.ElementTree as etree


def get_attr_number(node):
    # print node.attrib
    s = 0
    for n in node.iter():
        s += len(n.attrib)
        # print n.attrib
    return s


if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print get_attr_number(root)
