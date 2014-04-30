from stanford_parser.parser import Parser
import sys

def get_dict_relations(sentence):

    '''
    #Get the tweet as text
    sentence = ''
    for w in sys.argv[1:]:
        sentence += w+' '
    '''

    #Initiate parser to get parts of speech along with the dependencies
    stanford_parser = Parser()
    parts_of_speech, dependencies = stanford_parser.parseToStanfordDependencies(sentence.strip())
    parts_of_speech = parts_of_speech.split()


    #Create list of tuples of words with their parts of speech
    part_of_speech_tuple = []
    for t in parts_of_speech:
        s = t.encode('ascii','ignore')
        s=s.split('/')
        part_of_speech_tuple.append(s)


    #Extract the nouns from the list reqd_tuple
    i = 0
    l = len(part_of_speech_tuple)
    noun_list = []
    while i<l:
        #print reqd_tuple[i][1],'a'
        if part_of_speech_tuple[i][1]=='NN' or part_of_speech_tuple[i][1]=='NNP' or part_of_speech_tuple[i][1]=='NNPS' or part_of_speech_tuple[i][1]=='NNS':
            #print reqd_tuple[i][0]
            if part_of_speech_tuple[i][0] not in noun_list:
                noun_list.append(part_of_speech_tuple[i][0])
        i+=1

    print noun_list


    #Convert, clean dependency list
    depend_string = str(dependencies)

    depend_list = depend_string.split('\n')
    depend_list.pop(0)
    depend_list.pop()

    print depend_list

    #Obtain noun-adjective pair from noun_list and depend_list and add to dict
    dict_relations = {}
    for noun in noun_list:
        search_str_noun = 'amod(' + noun + ','
        
        for dep in depend_list:
            if dep.find(search_str_noun) == 0:

                adjective = ''
                adverb = ''
                
                #Extract adjective
                adjective = dep[len(search_str_noun)+1:len(dep)-1]
                search_str_adj = 'advmod(' + adjective + ','

                for dep2 in depend_list:
                    if dep2.find(search_str_adj) == 0:
                        #Extract adverb
                        adverb = dep2[len(search_str_adj)+1:len(dep2)-1]

                #Create adverb - adjective tuple
                adv_adj_tuple = [adverb,adjective]

                #If noun has been added to dict once already
                if noun in dict_relations.keys():
                    dict_relations[noun].append(adv_adj_tuple)
                else:
                    dict_relations[noun] = [adv_adj_tuple,]

    return dict_relations

'''
print dict_relations
print "DONE!"

#print parts_of_speech
#print str(dependencies)
#print dir(dependencies)
#print dependencies.tokens
#print dir(dependencies.relForConstituents)
'''
