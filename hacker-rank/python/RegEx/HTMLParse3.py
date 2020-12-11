from HTMLParser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print tag
        for ele in attrs:
            print '->', ele[0], '>', ele[1]


html = "\n".join([raw_input() for _ in range(int(raw_input()))])

parser = MyHTMLParser()
parser.feed(html)
parser.close()
