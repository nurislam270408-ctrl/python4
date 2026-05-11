from analytics import FileManager, DataLoader, ResultSaver, Report
from analytics.analyser import TopStudentsAnalyser, CountryAnalyser


fm = FileManager('students.csv')
fm.check_file()
fm.create_output_folder()

dl = DataLoader('students.csv')
dl.load()
dl.preview()

# Task1 Base class demo
from analytics import DataAnalyser

base = DataAnalyser(dl.students)
print(base)
base.analyse()
print()

# Task5 Polymorphism
analysers = [TopStudentsAnalyser(dl.students), CountryAnalyser(dl.students)]

print("-" * 30)
print("Running all analysers:")
print("-" * 30)
for a in analysers:
    print(a)
    a.analyse()
    a.print_results()
    print()

# Task4 Report
saver = ResultSaver(analysers[0].result, 'output/result.json')
report = Report(analysers[0], saver)
report.generate()
