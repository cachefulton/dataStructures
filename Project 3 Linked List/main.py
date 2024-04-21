from courselist import CourseList
from course import Course

def main():
    file = open("data.txt", 'r')

    student_course = CourseList()
    for line in file:
        strip_line = line.strip().split(',')
        student_course.insert(Course(strip_line[0], strip_line[1], strip_line[2], strip_line[3]))

    print(f"Current List: ({student_course.size()})")
    print(student_course)
    print(f"\nCumulative GPA: {round(student_course.calculate_gpa(), 3)}")

if __name__ == "__main__":
    main()