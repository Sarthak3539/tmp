fewshorts = [
    {
        "input": "List all departments.",
        "query": "SELECT * FROM Department;"
    },
    {
        "input": "Get the names of all projects.",
        "query": "SELECT title FROM Project;"
    },
    {
        "input": "Find the birthdate of 'Alice Johnson'.",
        "query": "SELECT dayOfBirth FROM Person WHERE name = 'Alice Johnson';"
    },
    {
        "input": "List all projects with start dates in 2023.",
        "query": "SELECT * FROM Project WHERE startDate >= '2023-01-01' AND startDate <= '2023-12-31';"
    },
    {
        "input": "Get the names of people involved in 'ML Project 1'.",
        "query": "SELECT Person.name FROM Person JOIN Project_Members ON Person.ID = Project_Members.personID WHERE Project_Members.projectID = 1;"
    },
    {
        "input": "List all department leads.",
        "query": "SELECT name FROM Person WHERE ID IN (SELECT leadPersonID FROM Department);"
    },
    {
        "input": "Get the titles of projects in the 'Data Science' department.",
        "query": "SELECT title FROM Project WHERE departmentID = (SELECT ID FROM Department WHERE name = 'Data Science');"
    },
    {
        "input": "Count the number of projects for each department.",
        "query": "SELECT Department.name, COUNT(Project.ID) AS project_count FROM Department JOIN Project ON Department.ID = Project.departmentID GROUP BY Department.name;"
    },
    {
        "input": "List all people and their roles in 'DS Project 2'.",
        "query": "SELECT Person.name, Project_Members.role FROM Person JOIN Project_Members ON Person.ID = Project_Members.personID WHERE Project_Members.projectID = 4;"
    },
    {
        "input": "Get the name and start date of all projects, ordered by start date.",
        "query": "SELECT title, startDate FROM Project ORDER BY startDate;"
    },
    {
        "input": "Find the average duration of projects (in days) for each department.",
        "query": "SELECT Department.name, AVG(julianday(Project.endDate) - julianday(Project.startDate)) AS avg_duration FROM Department JOIN Project ON Department.ID = Project.departmentID GROUP BY Department.name;"
    },
    {
        "input": "List all persons born after 1990.",
        "query": "SELECT * FROM Person WHERE dayOfBirth > '1990-01-01';"
    },
    {
        "input": "Get the names of all members of the 'Machine Learning' department.",
        "query": "SELECT name FROM Person WHERE ID IN (SELECT personID FROM Department_Members WHERE departmentID = (SELECT ID FROM Department WHERE name = 'Machine Learning'));"
    },
    {
        "input": "List all projects with their department names.",
        "query": "SELECT Project.title, Department.name FROM Project JOIN Department ON Project.departmentID = Department.ID;"
    },
    {
        "input": "Find the total number of members in each project.",
        "query": "SELECT Project.title, COUNT(Project_Members.personID) AS member_count FROM Project JOIN Project_Members ON Project.ID = Project_Members.projectID GROUP BY Project.title;"
    },
    {
        "input": "List the name and department of each department lead.",
        "query": "SELECT Person.name, Department.name FROM Person JOIN Department ON Person.ID = Department.leadPersonID;"
    },
    {
        "input": "Find the name of the lead person for the 'Cyber Security' department.",
        "query": "SELECT name FROM Person WHERE ID = (SELECT leadPersonID FROM Department WHERE name = 'Cyber Security');"
    },
    {
        "input": "List all projects that have members with the role 'Lead'.",
        "query": "SELECT DISTINCT Project.title FROM Project JOIN Project_Members ON Project.ID = Project_Members.projectID WHERE Project_Members.role = 'Lead';"
    },
    {
        "input": "Get the names of all members of the 'Cloud Computing' projects.",
        "query": "SELECT DISTINCT Person.name FROM Person JOIN Project_Members ON Person.ID = Project_Members.personID WHERE Project_Members.projectID IN (SELECT ID FROM Project WHERE departmentID = (SELECT ID FROM Department WHERE name = 'Cloud Computing'));"
    },
    {
        "input": "Count the number of departments each person is a member of.",
        "query": "SELECT Person.name, COUNT(Department_Members.departmentID) AS department_count FROM Person JOIN Department_Members ON Person.ID = Department_Members.personID GROUP BY Person.name;"
    },
    {
        "input": "List all projects and their duration in days.",
        "query": "SELECT title, julianday(endDate) - julianday(startDate) AS duration_days FROM Project;"
    },
    {
        "input": "Get the names of people involved in more than one project.",
        "query": "SELECT Person.name FROM Person JOIN Project_Members ON Person.ID = Project_Members.personID GROUP BY Person.name HAVING COUNT(Project_Members.projectID) > 1;"
    },
    {
        "input": "List all projects without members.",
        "query": "SELECT title FROM Project WHERE ID NOT IN (SELECT projectID FROM Project_Members);"
    },
    {
        "input": "Find the name and birthdate of the youngest person.",
        "query": "SELECT name, dayOfBirth FROM Person ORDER BY dayOfBirth DESC LIMIT 1;"
    },
    {
        "input": "Get the names of all people who are leads in any project.",
        "query": "SELECT DISTINCT Person.name FROM Person JOIN Project_Members ON Person.ID = Project_Members.personID WHERE Project_Members.role = 'Lead';"
    },
    {
        "input": "List all projects with their start and end dates, and the number of members.",
        "query": "SELECT Project.title, Project.startDate, Project.endDate, COUNT(Project_Members.personID) AS member_count FROM Project LEFT JOIN Project_Members ON Project.ID = Project_Members.projectID GROUP BY Project.title;"
    },
    {
        "input": "Find the average age of all department leads.",
        "query": "SELECT AVG(julianday('now') - julianday(dayOfBirth)) / 365.25 AS avg_age FROM Person WHERE ID IN (SELECT leadPersonID FROM Department);"
    },
    {
        "input": "Get the names and roles of all members of 'SD Project 1'.",
        "query": "SELECT Person.name, Project_Members.role FROM Person JOIN Project_Members ON Person.ID = Project_Members.personID WHERE Project_Members.projectID = 6;"
    },
    {
        "input": "List all departments and the number of projects in each.",
        "query": "SELECT Department.name, COUNT(Project.ID) AS project_count FROM Department LEFT JOIN Project ON Department.ID = Project.departmentID GROUP BY Department.name;"
    },
    {
        "input": "Find the titles of projects that have no end date set.",
        "query": "SELECT title FROM Project WHERE endDate IS NULL;"
    },
    {
        "input": "Get the names of all people who are not members of any department.",
        "query": "SELECT name FROM Person WHERE ID NOT IN (SELECT personID FROM Department_Members);"
    },
    {
        "input": "List all projects with their start and end dates, and the total duration in days.",
        "query": "SELECT title, startDate, endDate, (julianday(endDate) - julianday(startDate)) AS duration_days FROM Project;"
    },
    {
        "input": "Get the name and department of the person with the earliest birthdate.",
        "query": "SELECT Person.name, Department.name FROM Person JOIN Department ON Person.ID = Department.leadPersonID ORDER BY dayOfBirth ASC LIMIT 1;"
    },
    {
        "input": "Find the name of the person who is a lead in the most projects.",
        "query": "SELECT Person.name FROM Person JOIN Project_Members ON Person.ID = Project_Members.personID WHERE Project_Members.role = 'Lead' GROUP BY Person.name ORDER BY COUNT(Project_Members.projectID) DESC LIMIT 1;"
    },
    {
        "input": "List all departments that have no members.",
        "query": "SELECT name FROM Department WHERE ID NOT IN (SELECT departmentID FROM Department_Members);"
    },
    {
        "input": "Get the titles of projects and their corresponding department names, ordered by department.",
        "query": "SELECT Project.title, Department.name FROM Project JOIN Department ON Project.departmentID = Department.ID ORDER BY Department.name;"
    },
    {
        "input": "Find the total number of projects each person is involved in.",
        "query": "SELECT Person.name, COUNT(Project_Members.projectID) AS project_count FROM Person JOIN Project_Members ON Person.ID = Project_Members.personID GROUP BY Person.name;"
    },
    {
        "input": "Get the names of people who are members of the 'Data Science' department but not involved in any projects.",
        "query": "SELECT Person.name FROM Person WHERE ID IN (SELECT personID FROM Department_Members WHERE departmentID = (SELECT ID FROM Department WHERE name = 'Data Science')) AND ID NOT IN (SELECT personID FROM Project_Members);"
    },
    {
        "input": "List all projects that have more than 3 members.",
        "query": "SELECT Project.title FROM Project JOIN Project_Members ON Project.ID = Project_Members.projectID GROUP BY Project.title HAVING COUNT(Project_Members.personID) > 3;"
    },
    {
        "input": "Find the average number of members per project.",
        "query": "SELECT AVG(member_count) FROM (SELECT COUNT(personID) AS member_count FROM Project_Members GROUP BY projectID);"
    },
    {
        "input": "Get the names of all people who are either leads in projects or department leads.",
        "query": "SELECT DISTINCT Person.name FROM Person WHERE ID IN (SELECT personID FROM Project_Members WHERE role = 'Lead') OR ID IN (SELECT leadPersonID FROM Department);"
    },
    {
        "input": "List all projects and their total duration in days, ordered by duration.",
        "query": "SELECT title, (julianday(endDate) - julianday(startDate)) AS duration_days FROM Project ORDER BY duration_days DESC;"
    },
    {
        "input": "Find the name and department of the person who is the lead of the most projects.",
        "query": "SELECT Person.name, Department.name FROM Person JOIN Project_Members ON Person.ID = Project_Members.personID JOIN Project ON Project_Members.projectID = Project.ID JOIN Department ON Project.departmentID = Department.ID WHERE Project_Members.role = 'Lead' GROUP BY Person.ID ORDER BY COUNT(Project_Members.projectID) DESC LIMIT 1;"
    },
    {
        "input": "Get the names of all people who are members of both 'Machine Learning' and 'Data Science' departments.",
        "query": "SELECT DISTINCT p1.name FROM Person p1 JOIN Department_Members d1 ON p1.ID = d1.personID JOIN Department_Members d2 ON p1.ID = d2.personID WHERE d1.departmentID = (SELECT ID FROM Department WHERE name = 'Machine Learning') AND d2.departmentID = (SELECT ID FROM Department WHERE name = 'Data Science');"
    },
    {
        "input": "List the titles of all projects along with the names of their department leads.",
        "query": "SELECT Project.title, Person.name FROM Project JOIN Department ON Project.departmentID = Department.ID JOIN Person ON Department.leadPersonID = Person.ID;"
    },
    {
        "input": "Find the titles of all projects that have members from more than one department.",
        "query": "SELECT DISTINCT p.title FROM Project p JOIN Project_Members pm1 ON p.ID = pm1.projectID JOIN Department_Members dm1 ON pm1.personID = dm1.personID JOIN Project_Members pm2 ON p.ID = pm2.projectID JOIN Department_Members dm2 ON pm2.personID = dm2.personID WHERE dm1.departmentID != dm2.departmentID;"
    },
    {
        "input": "Get the names of people who are both department leads and project leads.",
        "query": "SELECT DISTINCT Person.name FROM Person WHERE ID IN (SELECT leadPersonID FROM Department) AND ID IN (SELECT personID FROM Project_Members WHERE role = 'Lead');"
    },
    {
        "input": "List all projects that span more than 6 months.",
        "query": "SELECT title FROM Project WHERE (julianday(endDate) - julianday(startDate)) > 180;"
    },
    {
        "input": "Find the names and roles of all members of the 'SD Project 2', ordered by role.",
        "query": "SELECT Person.name, Project_Members.role FROM Person JOIN Project_Members ON Person.ID = Project_Members.personID WHERE Project_Members.projectID = 7 ORDER BY Project_Members.role;"
    },
    {
        "input": "Get the names of all people who are members of exactly two projects.",
        "query": "SELECT Person.name FROM Person JOIN Project_Members ON Person.ID = Project_Members.personID GROUP BY Person.name HAVING COUNT(Project_Members.projectID) = 2;"
    },
    {
        "input": "List the titles of all projects that have no members from the 'Software Development' department.",
        "query": "SELECT title FROM Project WHERE ID NOT IN (SELECT projectID FROM Project_Members WHERE personID IN (SELECT personID FROM Department_Members WHERE departmentID = (SELECT ID FROM Department WHERE name = 'Software Development')));"
    },
    {
        "input": "Find the average number of members per project for each department.",
        "query": "SELECT Department.name, AVG(member_count) AS avg_members FROM (SELECT Project.departmentID, COUNT(Project_Members.personID) AS member_count FROM Project LEFT JOIN Project_Members ON Project.ID = Project_Members.projectID GROUP BY Project.ID) AS ProjectCounts JOIN Department ON ProjectCounts.departmentID = Department.ID GROUP BY Department.name;"
    },
    {
        "input": "Get the names and birthdates of the oldest person in each department.",
        "query": "SELECT Department.name, Person.name, Person.dayOfBirth FROM Department JOIN Department_Members ON Department.ID = Department_Members.departmentID JOIN Person ON Department_Members.personID = Person.ID WHERE Person.dayOfBirth = (SELECT MIN(dayOfBirth) FROM Person JOIN Department_Members ON Person.ID = Department_Members.personID WHERE Department_Members.departmentID = Department.ID);"
    },
    {
        "input": "List all projects and the number of members in each, including projects with no members.",
        "query": "SELECT Project.title, COUNT(Project_Members.personID) AS member_count FROM Project LEFT JOIN Project_Members ON Project.ID = Project_Members.projectID GROUP BY Project.title;"
    },
    {
        "input": "Find the names of people who are leads in projects within the 'Machine Learning' department.",
        "query": "SELECT DISTINCT Person.name FROM Person JOIN Project_Members ON Person.ID = Project_Members.personID JOIN Project ON Project_Members.projectID = Project.ID WHERE Project.departmentID = (SELECT ID FROM Department WHERE name = 'Machine Learning') AND Project_Members.role = 'Lead';"
    },
    {
        "input": "Get the titles and start dates of all projects that have more than 5 members, ordered by start date.",
        "query": "SELECT Project.title, Project.startDate FROM Project JOIN Project_Members ON Project.ID = Project_Members.projectID GROUP BY Project.ID HAVING COUNT(Project_Members.personID) > 5 ORDER BY Project.startDate;"
    },
    {
        "input": "List the names of people who are involved in projects that span more than 200 days.",
        "query": "SELECT DISTINCT Person.name FROM Person JOIN Project_Members ON Person.ID = Project_Members.personID JOIN Project ON Project_Members.projectID = Project.ID WHERE (julianday(Project.endDate) - julianday(Project.startDate)) > 200;"
    },
    {
        "input": "Find the names of people who are members of both 'Cyber Security' and 'Cloud Computing' departments.",
        "query": "SELECT DISTINCT p1.name FROM Person p1 JOIN Department_Members d1 ON p1.ID = d1.personID JOIN Department_Members d2 ON p1.ID = d2.personID WHERE d1.departmentID = (SELECT ID FROM Department WHERE name = 'Cyber Security') AND d2.departmentID = (SELECT ID FROM Department WHERE name = 'Cloud Computing');"
    },
    {
        "input": "List all departments and the total number of members in each.",
        "query": "SELECT Department.name, COUNT(Department_Members.personID) AS member_count FROM Department LEFT JOIN Department_Members ON Department.ID = Department_Members.departmentID GROUP BY Department.name;"
    },
    {
        "input": "Get the names of all people who are involved in exactly three projects.",
        "query": "SELECT Person.name FROM Person JOIN Project_Members ON Person.ID = Project_Members.personID GROUP BY Person.name HAVING COUNT(Project_Members.projectID) = 3;"
    },
    {
        "input": "Find the names and birthdates of the youngest person in each department.",
        "query": "SELECT Department.name, Person.name, Person.dayOfBirth FROM Department JOIN Department_Members ON Department.ID = Department_Members.departmentID JOIN Person ON Department_Members.personID = Person.ID WHERE Person.dayOfBirth = (SELECT MAX(dayOfBirth) FROM Person JOIN Department_Members ON Person.ID = Department_Members.personID WHERE Department_Members.departmentID = Department.ID);"
    },
    {
        "input": "List all projects along with their start dates, end dates, and the department lead name.",
        "query": "SELECT Project.title, Project.startDate, Project.endDate, Person.name AS lead_name FROM Project JOIN Department ON Project.departmentID = Department.ID JOIN Person ON Department.leadPersonID = Person.ID;"
    },
    {
        "input": "Get the names of people who are leads in projects within the 'Cloud Computing' department.",
        "query": "SELECT DISTINCT Person.name FROM Person JOIN Project_Members ON Person.ID = Project_Members.personID JOIN Project ON Project_Members.projectID = Project.ID WHERE Project.departmentID = (SELECT ID FROM Department WHERE name = 'Cloud Computing') AND Project_Members.role = 'Lead';"
    },
    {
        "input": "List all projects that have members from exactly two departments.",
        "query": "SELECT DISTINCT p.title FROM Project p JOIN Project_Members pm1 ON p.ID = pm1.projectID JOIN Department_Members dm1 ON pm1.personID = dm1.personID JOIN Project_Members pm2 ON p.ID = pm2.projectID JOIN Department_Members dm2 ON pm2.personID = dm2.personID WHERE dm1.departmentID != dm2.departmentID GROUP BY p.title HAVING COUNT(DISTINCT dm1.departmentID) = 2;"
    },
    {
        "input": "Get the names of people who are members of projects spanning more than one year.",
        "query": "SELECT DISTINCT Person.name FROM Person JOIN Project_Members ON Person.ID = Project_Members.personID JOIN Project ON Project_Members.projectID = Project.ID WHERE (julianday(Project.endDate) - julianday(Project.startDate)) > 365;"
    },
    {
        "input": "Find the names of people who are involved in both 'ML Project 1' and 'ML Project 2'.",
        "query": "SELECT DISTINCT p1.name FROM Person p1 JOIN Project_Members pm1 ON p1.ID = pm1.personID JOIN Project_Members pm2 ON p1.ID = pm2.personID WHERE pm1.projectID = 1 AND pm2.projectID = 2;"
    },
    {
        "input": "List all departments and their leads' names.",
        "query": "SELECT Department.name, Person.name AS lead_name FROM Department JOIN Person ON Department.leadPersonID = Person.ID;"
    },
    {
        "input": "Get the names of people who are members of 'Cyber Security' department and leads in projects.",
        "query": "SELECT DISTINCT Person.name FROM Person JOIN Department_Members ON Person.ID = Department_Members.personID JOIN Project_Members ON Person.ID = Project_Members.personID WHERE Department_Members.departmentID = (SELECT ID FROM Department WHERE name = 'Cyber Security') AND Project_Members.role = 'Lead';"
    },
    {
        "input": "List all projects with their department names and the total number of members.",
        "query": "SELECT Project.title, Department.name AS department_name, COUNT(Project_Members.personID) AS member_count FROM Project JOIN Department ON Project.departmentID = Department.ID LEFT JOIN Project_Members ON Project.ID = Project_Members.projectID GROUP BY Project.title;"
    },
    {
        "input": "Find the titles of projects with members from at least three different departments.",
        "query": "SELECT DISTINCT p.title FROM Project p JOIN Project_Members pm ON p.ID = pm.projectID JOIN Department_Members dm ON pm.personID = dm.personID GROUP BY p.title HAVING COUNT(DISTINCT dm.departmentID) >= 3;"
    },
    {
        "input": "Get the names of people who are involved in projects within the 'Data Science' department and are project leads.",
        "query": "SELECT DISTINCT Person.name FROM Person JOIN Project_Members ON Person.ID = Project_Members.personID JOIN Project ON Project_Members.projectID = Project.ID WHERE Project.departmentID = (SELECT ID FROM Department WHERE name = 'Data Science') AND Project_Members.role = 'Lead';"
    },
    {
        "input": "List all departments and the average number of members per project for each.",
        "query": "SELECT Department.name, AVG(member_count) AS avg_members FROM (SELECT Project.departmentID, COUNT(Project_Members.personID) AS member_count FROM Project LEFT JOIN Project_Members ON Project.ID = Project_Members.projectID GROUP BY Project.ID) AS ProjectCounts JOIN Department ON ProjectCounts.departmentID = Department.ID GROUP BY Department.name;"
    },
    {
        "input": "Find the names of people who are members of the 'Machine Learning' department and leads in projects.",
        "query": "SELECT DISTINCT Person.name FROM Person JOIN Department_Members ON Person.ID = Department_Members.personID JOIN Project_Members ON Person.ID = Project_Members.personID WHERE Department_Members.departmentID = (SELECT ID FROM Department WHERE name = 'Machine Learning') AND Project_Members.role = 'Lead';"
    },
    {
        "input": "List all projects with their start dates and end dates, and the names of the members ordered by their names.",
        "query": "SELECT Project.title, Project.startDate, Project.endDate, Person.name FROM Project JOIN Project_Members ON Project.ID = Project_Members.projectID JOIN Person ON Project_Members.personID = Person.ID ORDER BY Person.name;"
    },
    {
        "input": "Get the names of people who are leads in projects and also department leads.",
        "query": "SELECT DISTINCT Person.name FROM Person WHERE ID IN (SELECT leadPersonID FROM Department) AND ID IN (SELECT personID FROM Project_Members WHERE role = 'Lead');"
    },
    {
        "input": "List all departments and the total number of projects each is responsible for.",
        "query": "SELECT Department.name, COUNT(Project.ID) AS project_count FROM Department LEFT JOIN Project ON Department.ID = Project.departmentID GROUP BY Department.name;"
    },
    {
        "input": "Find the titles of projects with members from more than three departments.",
        "query": "SELECT DISTINCT p.title FROM Project p JOIN Project_Members pm ON p.ID = pm.projectID JOIN Department_Members dm ON pm.personID = dm.personID GROUP BY p.title HAVING COUNT(DISTINCT dm.departmentID) > 3;"
    },
    {
        "input": "Get the names of people who are involved in projects within the 'Software Development' department and are project leads.",
        "query": "SELECT DISTINCT Person.name FROM Person JOIN Project_Members ON Person.ID = Project_Members.personID JOIN Project ON Project_Members.projectID = Project.ID WHERE Project.departmentID = (SELECT ID FROM Department WHERE name = 'Software Development') AND Project_Members.role = 'Lead';"
    },
    {
        "input": "List all departments and their leads' names, and the total number of members in each department.",
        "query": "SELECT Department.name, Person.name AS lead_name, COUNT(Department_Members.personID) AS member_count FROM Department JOIN Person ON Department.leadPersonID = Person.ID LEFT JOIN Department_Members ON Department.ID = Department_Members.departmentID GROUP BY Department.name;"
    },
    {
        "input": "Find the titles of projects with members from at least two different departments.",
        "query": "SELECT DISTINCT p.title FROM Project p JOIN Project_Members pm ON p.ID = pm.projectID JOIN Department_Members dm ON pm.personID = dm.personID GROUP BY p.title HAVING COUNT(DISTINCT dm.departmentID) >= 2;"
    },
    {
        "input": "Get the names of people who are involved in projects within the 'Cyber Security' department and are project leads.",
        "query": "SELECT DISTINCT Person.name FROM Person JOIN Project_Members ON Person.ID = Project_Members.personID JOIN Project ON Project_Members.projectID = Project.ID WHERE Project.departmentID = (SELECT ID FROM Department WHERE name = 'Cyber Security') AND Project_Members.role = 'Lead';"
    },
    {
        "input": "List all projects with their start dates, end dates, and the names of the department leads.",
        "query": "SELECT Project.title, Project.startDate, Project.endDate, Person.name AS lead_name FROM Project JOIN Department ON Project.departmentID = Department.ID JOIN Person ON Department.leadPersonID = Person.ID;"
    }
]