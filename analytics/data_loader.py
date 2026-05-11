import csv


class DataLoader:
    def __init__(self, filepath):
        self.filepath = filepath
        self.students = []

    def load(self):
        try:
            with open(self.filepath, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                self.students = list(reader)
            print(f"Loaded {len(self.students)} students.")
        except FileNotFoundError:
            print(f"Error: file '{self.filepath}' not found.")
        except Exception as e:
            print(f"Error loading data: {e}")

    def preview(self, n=5):
        print(f"\nFirst {n} students:")
        for s in self.students[:n]:
            print(s)
        print()
