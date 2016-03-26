Study planner
=============

How to use
----------
Actually this is not so usable for anyone except for possibly myself/Imperial DoC students for now.

Look at the configuration section in the `studyplan.py`.

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
This is an example showing how to configure the script to generate your perfect/imperfect study plan. After configuring, simply do `python studyplan.py > studyplan.txt` which will then export a file called `studyplan.txt` which contains the studyplan.

Sample output with the sample configuration
---------
	2016-03-28   Revise   [C221=MC221] Compilers (Day 1)
	2016-03-29   Revise   [C233] Computational Techniques (Day 1)
	2016-03-30   Revise   [C233] Computational Techniques (Day 2)
	2016-03-31   Revise   [C233] Computational Techniques (Day 3)
	2016-04-01   Revise   [C212] Networks and Communications (Day 1)
	2016-04-02   Revise   [C231=MC231] Introduction to Artificial Intelligence (Day 1)
	2016-04-03   Revise   [C231=MC231] Introduction to Artificial Intelligence (Day 2)
	2016-04-04   Revise   [C231=MC231] Introduction to Artificial Intelligence (Day 3)
	2016-04-05   Revise   [C240=MC240] Models of Computation (Day 1)
	2016-04-06   Revise   [C240=MC240] Models of Computation (Day 2)
	2016-04-07   Revise   [C240=MC240] Models of Computation (Day 3)
	2016-04-08   Revise   [C240=MC240] Models of Computation (Day 4)
	2016-04-09   Revise   [C223=MC223] Concurrency (Day 1)
	2016-04-10   Revise   [C245] Statistics (Day 1)
	2016-04-11   Revise   [C245] Statistics (Day 2)
	2016-04-12   Revise   [C245] Statistics (Day 3)
	2016-04-13   Revise   [C245] Statistics (Day 4)
	2016-04-14   Revise   [C211=MC211] Operating Systems (Day 1)
	2016-04-15   Revise   [C211=MC211] Operating Systems (Day 2)
	2016-04-16   Revise   [C211=MC211] Operating Systems (Day 3)
	2016-04-17   Revise   [C202=MC202] Software Engineering - Algorithms (Day 1)
	2016-04-18   Revise   [C202=MC202] Software Engineering - Algorithms (Day 2)
	2016-04-19   Revise   [C202=MC202] Software Engineering - Algorithms (Day 3)
	2016-04-20   Revise   [C202=MC202] Software Engineering - Algorithms (Day 4)
	2016-04-21   Revise   [C220=MC220] Software Engineering Design (Day 1)
	2016-04-22   Revise   [C220=MC220] Software Engineering Design (Day 2)
	2016-04-23   Revise   [C220=MC220] Software Engineering Design (Day 3)
	2016-04-24   Revise   [C220=MC220] Software Engineering Design (Day 4)
	2016-04-25   Exam     [C220=MC220] Software Engineering Design
	             Revise   [C202=MC202] Software Engineering - Algorithms (Day 5)
	2016-04-26   Exam     [C202=MC202] Software Engineering - Algorithms
	             Revise   [C211=MC211] Operating Systems (Day 4)
	2016-04-27   Revise   [C211=MC211] Operating Systems (Day 5)
	2016-04-28   Exam     [C211=MC211] Operating Systems
	             Revise   [C245] Statistics (Day 5)
	2016-04-29   Exam     [C245] Statistics
	             Revise   [C223=MC223] Concurrency (Day 2)
	2016-04-30   Revise   [C223=MC223] Concurrency (Day 3)
	2016-05-01   Revise   [C223=MC223] Concurrency (Day 4)
	2016-05-02   Revise   [C223=MC223] Concurrency (Day 5)
	2016-05-03   Exam     [C223=MC223] Concurrency
	             Revise   [C240=MC240] Models of Computation (Day 5)
	2016-05-04   Exam     [C240=MC240] Models of Computation
	             Revise   [C231=MC231] Introduction to Artificial Intelligence (Day 4)
	2016-05-05   Revise   [C231=MC231] Introduction to Artificial Intelligence (Day 5)
	2016-05-06   Exam     [C231=MC231] Introduction to Artificial Intelligence
	             Revise   [C212] Networks and Communications (Day 2)
	2016-05-07   Revise   [C212] Networks and Communications (Day 3)
	2016-05-08   Revise   [C212] Networks and Communications (Day 4)
	2016-05-09   Revise   [C212] Networks and Communications (Day 5)
	2016-05-10   Exam     [C212] Networks and Communications
	             Revise   [C233] Computational Techniques (Day 4)
	2016-05-11   Revise   [C233] Computational Techniques (Day 5)
	2016-05-12   Exam     [C233] Computational Techniques
	             Revise   [C221=MC221] Compilers (Day 2)
	2016-05-13   Revise   [C221=MC221] Compilers (Day 3)
	2016-05-14   Revise   [C221=MC221] Compilers (Day 4)
	2016-05-15   Revise   [C221=MC221] Compilers (Day 5)
	2016-05-16   Exam     [C221=MC221] Compilers