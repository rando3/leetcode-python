import sys
import os

'''
PALANTIR CODING CHALLENGE
DETECTING CONTRACTOR FRAUD V4
PASSED 7/8 TEST CASES
(dont need to pass all to pass)
This is the submitted version. (I think, may be a little off)
Wasn't able to fully implement being able to pick out shortened jobs in batch, but the try is in the testing file for this. Would have gotten it done if I had 5 more minutes to test, I'm sure.
'''

def findViolations(datafeed):
    if datafeed is None:
        return None
    if len(datafeed) == 0:
        return []
    violations = []
    startMap = {}
    lastID = -sys.maxsize - 1

    for i, v in enumerate(datafeed):
        eventList = v.split(";")
        contractor = eventList[0]
        print('Contractor = ' + contractor)
        e = eventList[1]
        print('Event = ' + e)
        if e == "START":
            if contractor not in startMap:
                startMap[contractor] = [StartEvent(contractor, i + 1, lastID)]
                for x in startMap[contractor]:
                    print(x)
            else:
                startMap[contractor].append(StartEvent(contractor, i + 1, lastID))
                for x in startMap[contractor]:
                    print(x)
        else:
            invoiceList = e.split(",")
            if len(invoiceList) == 1:
                invoice = int(invoiceList[0])
                print('Invoice: ' + str(invoice))
                lastInv = startMap[contractor][0].lastID
                print('Last invoice: ' + str(lastInv))
                if lastInv > invoice:
                    print('Appending violation')
                    violations.append(startMap[contractor][0].shortenedViolation())
                    startMap[contractor].pop(0)
                else:
                    lastID = invoice if invoice > lastID else lastID
                    startMap[contractor].pop(0)
            elif len(invoiceList) > 1:
                invoiceList = [int(x) for x in invoiceList]
                invoiceList.sort()
                for invoice in invoiceList:
                    print('Invoice: ' + str(invoice))
                    lastInv = startMap[contractor][0].lastID
                    print('Last invoice: ' + str(lastInv))
                    if lastInv > invoice:
                        print('Appending violation')
                        violations.append(startMap[contractor][0].suspiciousBatch(i + 1))
                        startMap[contractor].pop(0)
                        for x in startMap[contractor]:
                            print(x)
                    else:
                        print('Next inv')
                        lastID = invoice if invoice > lastID else lastID
                        startMap[contractor].pop(0)
                        for x in startMap[contractor]:
                            print(x)
    return violations


class StartEvent:
    def __init__(self, contractor, line, lastID):
        self.contractor = contractor
        self.line = line
        self.lastID = lastID

    def __str__(self):
        return 'StartEvent(contractor={}, line#={}, lastInvoiceID={})'.format(self.contractor, self.line, self.lastID)

    def shortenedViolation(self):
        violation = "SHORTENED_JOB"
        viol = str(self.line) + ";" + self.contractor + ";" + violation
        return viol

    def suspiciousBatch(self, line):
        violation = "SUSPICIOUS_BATCH"
        viol = str(line) + ";" + self.contractor + ";" + violation
        return viol


if __name__ == "__main__":
    data1 = ['Alice;START',
                'Bob;START',
                'Bob;1',
                'Carson;START',
                'Alice;15',
                'Carson;6',
                'David;START',
                'David;24',
                'Evil;START',
                'Evil;24',
                'Evil;START',
                'Evil;18'
            ]
    data2 = ['Tom;START',
                'Jeremy;START',
                'Dana;START',
                'Jeremy;4',
                'Dana;2',
                'James;START',
                'Leah;START',
                'James;5',
                'Nick;START',
                'Tom;1',
                'Nick;6',
                'Leah;3',
            ]
    data3 = ['Alice;START',
                'Alice;2',
                'Alice;START',
                'Alice;1',
                'Alice;START',
                'Alice;4',
                'Alice;START',
                'Bob;START',
                'Bob;4',
                'Alice;3']
    data4 = ['Jeremy;START',
                'Jeremy;-5',
                'Tom;START',
                'Tom;-6']

    data5 = ['Nick;START',
                'Jeremy;START',
                'Leah;START',
                'Nick;10',
                'Jeremy;START',
                'Jeremy;START',
                'Leah;15',
                'Jeremy;8,14,9'
                ]
    # print(findViolations(data1))
    print(findViolations(data5))
