# Task1 Base class DataAnalyser
class DataAnalyser:
    def __init__(self, students):
        self.students = students
        self.result = {}

    def analyse(self):
        print("Not implemented — use a child class")

    def print_results(self):
        for key, value in self.result.items():
            print(f"{key}: {value}")

    def __str__(self):
        return f"DataAnalyser: base class, {len(self.students)} students"


# Task2 Child class TopStudentsAnalyser
class TopStudentsAnalyser(DataAnalyser):
    def __init__(self, students):
        super().__init__(students)

    def analyse(self):
        # Convert GPA and final_exam_score to float using lambda
        get_gpa = lambda s: float(s["GPA"])
        get_score = lambda s: float(s["final_exam_score"])

        # Filter students with GPA > 3.5 using filter + lambda
        high_gpa_students = list(filter(lambda s: float(s["GPA"]) > 3.5, self.students))

        # Sort all students by final_exam_score descending
        sorted_students = sorted(self.students, key=get_score, reverse=True)

        # Top 10 students: list of tuples (student_id, GPA, final_exam_score)
        top_10 = []
        for s in sorted_students[:10]:
            try:
                top_10.append((
                    s.get("student_id", "N/A"),
                    float(s["GPA"]),
                    float(s["final_exam_score"])
                ))
            except (ValueError, KeyError) as e:
                print(f"Skipping student due to error: {e}")

        gpas = list(map(get_gpa, self.students))

        self.result = {
            "total_students": len(self.students),
            "top_10": top_10,
            "average_gpa": round(sum(gpas) / len(gpas), 2),
            "high_gpa_count": len(high_gpa_students)
        }

    # Task 3 — Override print_results()
    def print_results(self):
        print("=" * 30)
        print("TOP STUDENTS ANALYSIS REPORT")
        print("=" * 30)
        super().print_results()
        print("=" * 30)

    def __str__(self):
        return f"TopStudentsAnalyser: Top Students Analysis, {len(self.students)} students"


# Extra child class for Task 5 — Polymorphism
class CountryAnalyser(DataAnalyser):
    def __init__(self, students):
        super().__init__(students)

    def analyse(self):
        country_count = {}
        for s in self.students:
            country = s.get("country", "Unknown")
            country_count[country] = country_count.get(country, 0) + 1

        sorted_countries = sorted(country_count.items(), key=lambda x: x[1], reverse=True)
        top_3 = sorted_countries[:3]

        # Filter countries with more than 100 students using filter + lambda
        popular = list(filter(lambda c: c[1] > 100, sorted_countries))

        self.result = {
            "total_students": len(self.students),
            "total_countries": len(country_count),
            "top_3": top_3,
            "all_countries": sorted_countries
        }

    # Task3 Override print_results()
    def print_results(self):
        print("=" * 30)
        print("COUNTRY ANALYSIS REPORT")
        print("=" * 30)
        super().print_results()
        print("=" * 30)

    def __str__(self):
        return f"CountryAnalyser: Country Analysis, {len(self.students)} students"
