import sys
import os

'''
PALANTIR CODING CHALLENGE TEST FILE
Wasn't able to fully implement picking out specific shortened job from batch job completion, but here's as far as I got.
Passed Test Case 8, but failed Test Case 7 (which I passed before), so I just needed some more time to test
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
                potentialShortened = 0
                shortenedJobs = 0
                susBatch = None
                startFraud = False
                potentialViolations = []
                invoiceList = [int(x) for x in invoiceList]
                invoiceList.sort()
                for invoice in invoiceList:
                    print('Invoice: ' + str(invoice))
                    lastInv = startMap[contractor][0].lastID
                    print('Last invoice: ' + str(lastInv))
                    if lastInv > invoice:
                        startFraud = True
                        print('Appending violation')
                        shortenedJobs += 1
                        potentialShortened += 1
                        susBatch = startMap[contractor][0].suspiciousBatch(i + 1) if susBatch is None else susBatch
                        potentialViolations.append(startMap[contractor][0].shortenedViolation())
                        startMap[contractor].pop(0)
                        for x in startMap[contractor]:
                            print(x)
                    else:
                        if startFraud:
                            potentialShortened = 0
                        print('Next inv')
                        lastID = invoice if invoice > lastID else lastID
                        startMap[contractor].pop(0)
                        for x in startMap[contractor]:
                            print(x)
                print(potentialViolations)
                if shortenedJobs == potentialShortened:
                    violations.extend(potentialViolations)
                    violations.append(susBatch)
                    break
                elif shortenedJobs > 0:
                    violations.append(susBatch)
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
    data6 = ['Jeremy;START',
'Leah;START',
'Leah;50',
'Jeremy;START',
'Leah;START',
'Leah;100',
'Jeremy;START',
'Leah;START',
'Leah;150',
'Jeremy;START',
'Jeremy;37,52,68,86',
'John;START',
'John;START',
'John;500,5000'
    ]
    # print(findViolations(data1))
    print(findViolations(data5))
