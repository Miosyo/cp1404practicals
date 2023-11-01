"""A program for managing projects"""

from project import Project


def main():
    filename = input("Load projects from: ")
    projects = load_projects(filename)
    print(projects)

    filename = input("Save projects to: ")
    save_projects(filename, projects)


def load_projects(filename):
    projects = []
    with open(filename, encoding="utf-8") as file_in:
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


def save_projects(filename, projects):
    with open(filename, 'w', encoding="utf-8") as file_out:
        print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=file_out, end='')
        for project in projects:
            print(f"{project.name}\t{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}",
                  file=file_out, end='')


if __name__ == '__main__':
    main()
