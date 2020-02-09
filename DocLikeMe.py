import random
import math

class slimDoc():
    def __init__(self,docID):
        self.docID = docID
        self.properties = []

# Properties and values are represented as such: topic:finance
# Properties in this simulation will include:
#   topic
#   type
#   sender
#   receiver

def buildCorpus(documentCount):

    propertySpace = {'topic': ['finance', 'marketing', 'boating', 'avionics'], 'sender': ['ken', 'jack', 'bill'],
                     'receiver':
                         ['sally', 'jen', 'carol'], 'type': ['word', 'excel']}
    doc_list = []

    for idx in range(documentCount):
        doc = slimDoc(idx)

        # Add single sender
        pos_index = random.randint(0,len(propertySpace['sender'])-1)
        for item_index in range(len(propertySpace['sender'])):
            if item_index == pos_index:
                doc.properties.append('pos:sender:' + propertySpace['sender'][item_index])
            else:
                doc.properties.append('neg:sender:' + propertySpace['sender'][item_index])

        # Add single type
        pos_index = random.randint(0, len(propertySpace['type']) - 1)
        for item_index in range(len(propertySpace['type'])):
            if item_index == pos_index:
                doc.properties.append('pos:type:' + propertySpace['type'][item_index])
            else:
                doc.properties.append('neg:type:' + propertySpace['type'][item_index])

        # Add multiple topics (each with a 50% chance of occurring)
        for item_index in range(len(propertySpace['topic'])):
            choice = random.randint(0,1)
            if choice == 1:
                doc.properties.append('pos:topic:' + propertySpace['topic'][item_index])
            else:
                doc.properties.append('neg:topic:' + propertySpace['topic'][item_index])

        # Add multiple receivers (each with a 50% chance of occurring)
        for item_index in range(len(propertySpace['receiver'])):
            choice = random.randint(0, 1)
            if choice == 1:
                doc.properties.append('pos:receiver:' + propertySpace['receiver'][item_index])
            else:
                doc.properties.append('neg:receiver:' + propertySpace['receiver'][item_index])

        doc_list.append(doc)

    return doc_list

def countEntries(doc_list,doc_count):

    stats = {}

    for doc in doc_list:
        for prop in doc.properties:
            if prop in stats.keys():
                stats[prop] = stats[prop] + 1
            else:
                stats[prop] = 1

    for myKey in stats.keys():
        newValue = 1 - math.erf(stats[myKey]/doc_count)
        stats[myKey] = newValue

    return stats

def findSimilarDoc(target,doc_list,stats):
    rankedDocs = []
    for doc in doc_list:
        similarity = 0
        for doc_prop in doc.properties:
            for tgt_prop in target.properties:
                if doc_prop == tgt_prop:
                    similarity += stats[doc_prop]
        rankedDocs.append((doc.docID,similarity))

    return rankedDocs

def main():
    doc_count = 8
    doc_list = buildCorpus(doc_count)
    stats = countEntries(doc_list,doc_count)
    target = doc_list[random.randint(0,doc_count-1)]
    rankedDocs = findSimilarDoc(target, doc_list, stats)

    for doc in doc_list:
        print(f'Doc ID: {doc.docID}')
        for prop in doc.properties:
            # print(prop[:2])
            if prop[:3] == 'pos':
                print(f'   {prop[4:]}')
    print()

    print(f'Find Like This: {target.docID}')
    for prop in target.properties:
        if prop[:3] == 'pos':
            print(f'   {prop[4:]}')

    print()
    print('ID   Score')
    for rank in rankedDocs:
        print(f'{rank[0]}    {rank[1]}')


main()







