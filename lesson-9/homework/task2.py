import csv

def read_grades(file_path):
    """Reads grades from a CSV file and returns a list of grades."""
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        return [{'Subject': row['Subject'], 'Grade': int(row['Grade'])} for row in reader]

def calculate_average_grades(grades):
    """Calculates the average grade for each subject."""
    totals = {}
    counts = {}

    for entry in grades:
        subject = entry['Subject']
        grade = entry['Grade']
        totals[subject] = totals.get(subject, 0) + grade
        counts[subject] = counts.get(subject, 0) + 1

    return {subject: totals[subject] / counts[subject] for subject in totals}

def write_average_grades(file_path, averages):
    """Writes average grades to a CSV file."""
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Subject', 'Average Grade'])
        writer.writerows(averages.items())

# Main execution
if __name__ == "__main__":
    input_file = 'grades.csv'
    output_file = 'average_grades.csv'

    grades = read_grades(input_file)
    averages = calculate_average_grades(grades)
    write_average_grades(output_file, averages)

    print(f"Average grades written to {output_file}.")
