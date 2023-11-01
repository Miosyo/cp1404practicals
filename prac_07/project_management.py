"""A program for managing projects
Estimate:   45 minutes
Actual:     .. minutes
"""
import datetime
from datetime import date
from project import Project

MENU = ("- (L)oad projects\n"
        "- (S)ave projects\n"
        "- (D)isplay projects\n"
        "- (F)ilter projects by date\n"
        "- (A)dd new project\n"
        "- (U)pdate project\n"
        "- (Q)uit")


def main():
    current_filename = "projects.txt"
    projects = load_projects(current_filename)

    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            current_filename = input("Load projects from: ")
            projects = load_projects(current_filename)
        elif choice == "S":
            current_filename = input("Save projects to: ")
            save_projects(current_filename, projects)
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            filter_projects(projects)
        elif choice == "A":
            add_project(projects)
        elif choice == "U":
            update_project(projects)
        else:
            print("Invalid Choice!")
        print(MENU)
        choice = input(">>> ").upper()
    save_projects(current_filename, projects)


def filter_projects(projects):
    date_to_filter_by_string = get_valid_date("Show projects that start after (dd/mm/yy): ")
    date_to_filter_by = datetime.datetime.strptime(date_to_filter_by_string, "%d/%m/%Y").date()
    projects_after_date = [project for project in projects
                           if date_to_filter_by < datetime.datetime.strptime(project.start_date, "%d/%m/%Y").date()]
    for project in projects_after_date:
        print(project)


def update_project(projects):
    for i, project in enumerate(projects):
        print(f"{i} {project}")

    choice = get_valid_number("Project Choice: ")
    while choice not in range(0, len(projects)):
        print("Invalid choice")
        choice = get_valid_number("Project Choice: ")
    project_choice = projects[choice]
    print(project_choice)
    new_percentage = get_valid_number("New percentage: ")
    new_priority = get_valid_number("New priority: ")
    project_choice.completion_percentage = new_percentage
    project_choice.priority = new_priority


def add_project(projects):
    print("Let's add a new project")
    name = get_valid_string("Name: ")
    # start_date = get_valid_string("Start date (dd/mm/yy): ")
    start_date = get_valid_date("Start date (dd/mm/yy): ")
    priority = get_valid_number("Priority: ")
    cost_estimate = float(get_valid_number("Cost Estimate: $"))
    percent_complete = get_valid_number("Percent complete: ")
    projects.append(Project(name, start_date, priority, cost_estimate, percent_complete))


def get_valid_date(display_string):
    date_string = get_valid_string("Start date (dd/mm/yy): ")
    while not is_valid_date(date_string):
        date_string = get_valid_string("Start date (dd/mm/yy): ")
    return date_string


def is_valid_date(date_string):
    try:
        date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
        return True
    except ValueError:
        return False


def get_valid_string(display_string):
    """Gets a valid string from the user"""
    user_input = input(display_string)
    while user_input == "":
        print("Input can not be blank.")
        user_input = input(display_string)
    return user_input


def get_valid_number(display_string):
    """Gets valid number from user"""
    is_valid_input = False
    while not is_valid_input:
        try:
            user_input = int(input(display_string))
            is_valid_input = True
        except ValueError:
            print("Invalid input. Not a valid number")
    return user_input


def display_projects(projects):
    """Display projects in two groups. Complete and Incomplete, sorted by priority"""
    complete_projects = sorted([project for project in projects if project.is_complete()])
    incomplete_projects = sorted([project for project in projects if not project.is_complete()])
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
            priority = int(parts[2])
            cost_estimate = float(parts[3])
            completion_percentage = int(parts[4])
            projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))
    return projects


def save_projects(filename, projects):
    """save projects to filename provided"""
    with open(filename, 'w', encoding="utf-8") as file_out:
        print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=file_out, end='\n')
        for project in projects:
            print(
                f"{project.name}\t{project.start_date}\t{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}",
                file=file_out, end='\n')


if __name__ == '__main__':
    main()
