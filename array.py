courses = ["MIT","Cybersecurity","Datascience","Mathematics"]
print(courses)
# Accessing an element in an array
print(courses[1])

# Looping through an array
for course in courses:
    print(course)

# Adding an element into an array
courses.append("Android Development")
print(courses)

# Deleting an element from an array
courses.remove("Datascience")
print(courses)