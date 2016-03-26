import datetime

# confiuration #

REVISION_START_DATE = datetime.date(2016, 3, 28)

TURBO_MODE_DAYS = 4

exams = [
("C220=MC220", "Software Engineering Design",             "25-Apr"),
("C202=MC202", "Software Engineering - Algorithms",       "26-Apr"),
("C211=MC211", "Operating Systems",                       "28-Apr"),
("C245",       "Statistics",                              "29-Apr"),
("C223=MC223", "Concurrency",                             "3-May"),
("C240=MC240", "Models of Computation",                   "4-May"),
("C231=MC231", "Introduction to Artificial Intelligence", "6-May"),
("C212",       "Networks and Communications",             "10-May"),
("C233",       "Computational Techniques",                "12-May"),
("C221=MC221", "Compilers",                               "16-May")
]

# END: confiuration #

CURR_YEAR = datetime.date.today().year
DAY_DELTA = datetime.timedelta(days=1)
TURBO_MODE_DAYS = datetime.timedelta(days=TURBO_MODE_DAYS)

def dateRange(current, end, step=DAY_DELTA):
    r = []
    while not(current == end):
        r.append(current)
        current = current+step
    return r

class Exam(tuple):
    def __new__(cls, code, subject, date):
        return super(Exam, cls).__new__(cls, (code, subject, date))

    def __init__(self, code, subject, date):
        self.code = code
        self.subject = subject
        self.date = date
    def __str__(self):
        return "[" + self.code + "] "+self.subject
    def __eq__(self, other):
        return other.code==self.code

class Timetable:
    def __init__(self):
        self.exams = []
    def addExam(self, exam):
        self.exams.append(exam)
        self.exams.sort(key=lambda exam: exam.date)
    def findExamsByDate(self, queryDate):
        return filter(lambda (_code, _subject, date): date==queryDate, self.exams)
    def findUpcomingExams(self, queryDate):
        return filter(lambda (_code, _subject, date): date>queryDate, self.exams)

class Plan:
    def __init__(self):
        self.plans = []
    def __str__(self):
        planItemCount = {}
        currentdate = None
        s = ""
        for (date, planitem) in self.plans:
            planItemCount[planitem.desc] = 0
        for (date, planitem) in self.plans:
            if(planitem.type == "Revise"):
                planItemCount[planitem.desc] += 1

            if(not(currentdate == date)):
                s += str(date) + "   "
                currentdate = date
            else:
                s += "             "
            s += str(planitem) 
            if(planitem.type == "Revise"):
                s += " (Day " + str(planItemCount[planitem.desc]) + ")"
            s += "\n"
        return s
    def addItem(self, queryDate, planItem):
        self.plans.append((queryDate, planItem))
        self.plans.sort(key=lambda (_, planItem): -planItem.weight)
        self.plans.sort(key=lambda (date, _): date)
    def removeItem(self, queryDate, queryItem):
        self.plans.remove((queryDate, queryItem))

class PlanItem:
    def __init__(self, weight, type, desc):
        self.weight = weight
        self.type = type
        self.desc = desc
    def __str__(self):
        return "%-8s %s" % (self.type, self.desc)
    def __eq__(self, other):
        return (self.weight == other.weight) and \
               (self.type   == other.type)   and \
               (self.desc   == other.desc)

class RevisionCounters:
    class Counter:
        def __init__(self, exam):
            self.exam = exam
            self.count = 0
        def inc(self):
            self.count += 1
    def __init__(self):
        self.counters = []
    def addExam(self, exam):
        self.counters.append(self.Counter(exam))
    def revise(self, revisedExam):
        for counter in filter(lambda counter: counter.exam.code==revisedExam.code, self.counters):
            counter.inc()


timetable = Timetable()
plan = Plan()

revision_counters = {}
# import exams to timetable
for (code, subject, date) in exams:
    date = datetime.datetime.strptime(date, "%d-%b").replace(year=2016).date()
    exam = Exam(code, subject, date)
    timetable.addExam(exam)
    revision_counters[exam.code]=0
    plan.addItem(date, PlanItem(1, "Exam", exam))

average_days_per_subject = ((timetable.exams[-1].date - REVISION_START_DATE).days / len(timetable.exams)) + 1
# naive time planning
for date in dateRange(REVISION_START_DATE, timetable.exams[-1].date, DAY_DELTA):
    upcomingExam = timetable.findUpcomingExams(date)[0]
    revision_counters[upcomingExam.code]+=1
    plan.addItem(date, PlanItem(0, "Revise", upcomingExam))

examToImproveIndex = len(timetable.exams) -1
date = REVISION_START_DATE
while examToImproveIndex > 0:
    upcomingExam = timetable.findUpcomingExams(date)[0]
    examToImprove = timetable.exams[examToImproveIndex]
    if(revision_counters[examToImprove.code]<average_days_per_subject):
        revision_counters[examToImprove.code] += 1
        revision_counters[upcomingExam.code] -= 1
        plan.removeItem(date, PlanItem(0, "Revise", upcomingExam))
        plan.addItem(date, PlanItem(0, "Revise", examToImprove))
        date += DAY_DELTA
    if(revision_counters[examToImprove.code] >= average_days_per_subject):
        examToImproveIndex -= 1
print plan
