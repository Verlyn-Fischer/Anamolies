import random
import csv

class document:
    def __init__(self):
        self.id = 0
        self.day = 0
        self.type = 'none' # email, slack, pdf
        self.sender = 'none' # adam, bob, charlie
        self.recipients = [] # darla, fran, harriet
        self.topics = [] # trek, cosmology, pizza

def generateDocSet():
    documentSet = []
    number_of_days = 50
    range_docs_per_day = (10,40)
    docID = 0

    for day in range(number_of_days):
        numberDocs = random.randint(range_docs_per_day[0],range_docs_per_day[1])
        for doc in range(numberDocs):
            docID += 1
            myDoc = document()
            myDoc.id = docID
            myDoc.day = day
            documentSet.append(myDoc)

    return documentSet

def addKnownSignal(docSet):
    interestingSpan = (19,32)
    documentWithSignature = 0.15 # percent of document that recieve the signature
    for doc in docSet:
        if doc.day >= interestingSpan[0] and doc.day <= interestingSpan[1]:
            if random.random() < documentWithSignature:
                doc.sender = 'bob'
                doc.recipients.append('harriet')
                doc.topics.append('cosmology')
                doc.type = 'slack'

def addBackgroundSignal(docSet):
    for doc in docSet:
        if doc.sender == 'none':
            doc.sender = random.choice(['adam','bob','charlie'])
        for i in range(3):
            topic = random.choice(['trek','cosmology','pizza'])
            if topic not in doc.topics:
                doc.topics.append(topic)
        for i in range(3):
            recipient = random.choice(['darla','fran','harriet'])
            if recipient not in doc.recipients and recipient != doc.sender:
                doc.recipients.append(recipient)
        if doc.type == 'none':
            doc.type = random.choice(['email','slack','pdf'])

def exportDocs(docSet):
    outputList = []
    line = ('docID','day','type','sender','darla','fran','harriet','trek','cosmology','pizza')
    outputList.append(line)
    # docID, day, type, sender, recipient1, recipient2, recipient3, topic1, topic2, topic3
    for doc in docSet:
        if 'darla' in doc.recipients:
            rec1 = 1
        else:
            rec1 = 0

        if 'fran' in doc.recipients:
            rec2 = 1
        else:
            rec2 = 0

        if 'harriet' in doc.recipients:
            rec3 = 1
        else:
            rec3 = 0

        if 'trek' in doc.topics:
            top1 = 1
        else:
            top1 = 0

        if 'cosmology' in doc.topics:
            top2 = 1
        else:
            top2 = 0

        if 'pizza' in doc.topics:
            top3 = 1
        else:
            top3 = 0


        line = (doc.id,doc.day,doc.type,doc.sender,rec1,rec2,rec3,top1,top2,top3)

        outputList.append(line)

    with open('docList.csv', 'w', newline='') as csvfile:
        csvWriter = csv.writer(csvfile, delimiter=',')
        csvWriter.writerows(outputList)

def main():
    docSet = generateDocSet()
    addKnownSignal(docSet)
    addBackgroundSignal(docSet)
    exportDocs(docSet)
    print('Document Set Completed')


main()
