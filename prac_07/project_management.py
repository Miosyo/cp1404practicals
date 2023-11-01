"""A program for managing projects"""

from project import Project

FILENAME = "projects.txt"


def main():
    projects = load_projects()
    print(projects)
    save_projects(projects)


def load_projects():
    projects = []
    with open(FILENAME, encoding="utf-8") as file_in:
        file_in.readline()  # Remove heading
        for line in file_in.readlines():
            parts = line.split('\t')
            name = parts[0]
            start_date = parts[1]
            priority = parts[2]
            cost_estimate = parts[3]
            completion_percentage = parts[4]
            projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))
    return projects


def save_projects(projects):
    pass


if __name__ == '__main__':
    main()
