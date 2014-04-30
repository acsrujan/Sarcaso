from stanford_parser.parser import Parser

stanford_parser = Parser()

dependencies = stanford_parser.parseToStanfordDependencies("The girl I met was your sister.")

dependencies = dependencies.split()

reqd_tuple = []

for t in dependencies:
    s = t.encode('ascii','ignore')
    s=s.split('/')
    reqd_tuple.append(s)

i = 0
l = len(reqd_tuple)
while i<l:
    #print reqd_tuple[i][1],'a'
    if reqd_tuple[i][1]=='NN' or reqd_tuple[i][1]=='NNP' or reqd_tuple[i][1]=='NNPS' or reqd_tuple[i][1]=='NNS':
        print reqd_tuple[i][0]
    i+=1

#print reqd_tuple
