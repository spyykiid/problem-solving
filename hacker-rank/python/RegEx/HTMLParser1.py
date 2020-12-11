from HTMLParser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print "Start :", tag
        for ele in attrs:
            print '->', ele[0], '>', ele[1]

    def handle_endtag(self, tag):
        print "End   :", tag

    def handle_startendtag(self, tag, attrs):
        print "Empty :", tag
        for ele in attrs:
            print '->', ele[0], '>', ele[1]


html_str = "\n".join([raw_input() for _ in range(int(raw_input()))])

parser = MyHTMLParser()
parser.feed(html_str)
