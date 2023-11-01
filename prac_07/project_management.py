"""A program for managing projects"""

from project import Project

MENU = ("- (L)oad projects\n"
        "- (S)ave projects\n"
        "- (D)isplay projects\n"
        "- (F)ilter projects by date\n"
        "- (A)dd new project\n"
        "- (U)pdate project\n"
        "- (Q)uit")


def main():
    projects = load_projects("projects.txt")  # Test line

    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            filename = input("Load projects from: ")
            projects = load_projects(filename)
        elif choice == "S":
            pass
        elif choice == "D":
            pass
        elif choice == "F":
            pass
        elif choice == "A":
            pass
        elif choice == "U":
            pass
        else:
            print("Invalid Choice!")
        print(MENU)
        choice = input(">>> ").upper()

    # filename = input("Save projects to: ")
    # save_projects(filename, projects)


def display_projects(projects):
    complete_projects = [project for project in projects if project.is_complete()]
    incomplete_projects = [project for project in projects if not project.is_complete()]
    print("Incomplete Projects:")
    for project in incomplete_projects:
        print(f"\t{project}")
    print("Complete Projects:")
    for project in complete_projects:
        print(f"\t{project}")


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
            completion_percentage = float(parts[4])
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
