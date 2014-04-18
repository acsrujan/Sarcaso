from stanford_parser.parser import Parser

def analyze_likes():

    stanford_parser = Parser()

    dependencies = stanford_parser.parseToStanfordDependencies('The girl I met was your sister.')

    print "\nDone parsing. REturned value:\n"
    print dependencies


if __name__=='__main__':
    analyze_likes()
