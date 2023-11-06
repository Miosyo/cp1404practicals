"""A program for managing projects
Estimate:   45 minutes
Actual:     90 minutes
"""
import datetime
from project import Project

MENU = ("- (L)oad projects\n"
        "- (S)ave projects\n"
        "- (D)isplay projects\n"
        "- (F)ilter projects by date\n"
        "- (A)dd new project\n"
        "- (U)pdate project\n"
        "- (Q)uit")


def main():
    """Let the user read, update, filter and save projects."""
    current_filename = "projects.txt"
    projects = load_projects(current_filename)

    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            current_filename = get_valid_string("Load projects from: ")
            projects = load_projects(current_filename)
        elif choice == "S":
            current_filename = get_valid_string("Save projects to: ")
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
    print("Thank you for using custom-built project management software")
    save_projects(current_filename, projects)


def filter_projects(projects):
    """Filters projects by a given date and prints them out for the user."""
    date_to_filter_by_string = get_valid_date("Show projects that start after (dd/mm/yy): ")
    date_to_filter_by = datetime.datetime.strptime(date_to_filter_by_string, "%d/%m/%Y").date()
    projects_after_date = sorted([project for project in projects
                                  if date_to_filter_by < datetime.datetime.strptime
                                  (project.start_date, "%d/%m/%Y").date()])
    for project in projects_after_date:
        print(project)


def update_project(projects):
    """Update the completion percentage and priority of a project."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")

    choice = get_valid_number("Project Choice: ")
    while choice not in range(0, len(projects)):
        print("Invalid choice")
        choice = get_valid_number("Project Choice: ")
    project_choice = projects[choice]
    print(project_choice)

    # Should probably be a function (Maybe update get_valid_number()???)
    is_valid_number = False
    new_percentage_string = input("New percentage: ")
    if new_percentage_string:
        while not is_valid_number:
            try:
                new_percentage = int(new_percentage_string)
                project_choice.completion_percentage = new_percentage
                is_valid_number = True
            except TypeError:
                print("Invalid number")
                new_percentage_string = input("New percentage: ")

    # DRY
    is_valid_number = False
    new_priority_string = input("New priority: ")
    if new_priority_string:
        while not is_valid_number:
            try:
                new_priority = int(new_priority_string)
                project_choice.priority = new_priority
                is_valid_number = True
            except TypeError:
                print("Invalid number")
                new_priority_string = input("Priority: ")


def add_project(projects):
    """Get user input and add new project to projects list."""
    print("Let's add a new project")
    name = get_valid_string("Name: ")
    start_date = get_valid_date("Start date (dd/mm/yy): ")
    priority = get_valid_number("Priority: ")
    cost_estimate = float(get_valid_number("Cost Estimate: $"))
    percent_complete = get_valid_number("Percent complete: ")
    projects.append(Project(name, start_date, priority, cost_estimate, percent_complete))


def get_valid_date(display_string):
    """Get a valid date from the user."""
    date_string = get_valid_string(display_string)
    while not is_valid_date(date_string):
        print("Invalid date")
        date_string = get_valid_string(display_string)
    return date_string


def is_valid_date(date_string):
    """Check to see if date is valid by passing it into datetime."""
    try:
        datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
        return True
    except ValueError:
        return False


def get_valid_string(display_string):
    """Gets a valid string from the user."""
    user_input = input(display_string)
    while user_input == "":
        print("Input can not be blank.")
        user_input = input(display_string)
    return user_input


def get_valid_number(display_string):
    """Gets valid number from user."""
    is_valid_input = False
    while not is_valid_input:
        try:
            user_input = int(input(display_string))
            is_valid_input = True
        except ValueError:
            print("Invalid input. Not a valid number")
    return user_input


def display_projects(projects):
    """Display projects in two groups. Complete and Incomplete, sorted by priority."""
    complete_projects = sorted([project for project in projects if project.is_complete()])
    incomplete_projects = sorted([project for project in projects if not project.is_complete()])
    print("Incomplete Projects:")
    for project in incomplete_projects:
        print(f"\t{project}")
    print("Complete Projects:")
    for project in complete_projects:
        print(f"\t{project}")


def load_projects(filename):
    """load projects from specified file.

    Format is: Name,Start Date,Priority,Cost Estimate,Completion Percentage
    Seperated by a '\t'.
    """
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
            projects.append(
                Project(name, start_date, priority, cost_estimate, completion_percentage))
    return projects


def save_projects(filename, projects):
    """save projects to filename provided"""
    with open(filename, 'w', encoding="utf-8") as file_out:
        print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage",
              file=file_out, end='\n')
        for project in projects:
            print(
                f"{project.name}\t{project.start_date}\t{project.priority}\t"
                f"{project.cost_estimate}\t{project.completion_percentage}",
                file=file_out, end='\n')


if __name__ == '__main__':
    main()
