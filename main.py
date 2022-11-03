from notifypy import Notify
from course import Course
from scraper import CourseScrapper
from secrets import INPUT_FILE


def read_file(file_name):
    courses = []
    with open(file_name, encoding='utf-8') as f:
        for line in f:
            course_data = line.split(" ")

            # 0: term
            # 1: year
            # 2: college
            # 3: dept
            # 4: course_num
            c = Course(course_data[0], course_data[1],
                       course_data[2], course_data[3], course_data[4])

            # if there's input for sectiion
            if len(course_data) == 6:
                c.set_section(course_data[5])

            courses.append(c)

    return courses


def run(scraper: CourseScrapper, courses):
    # print("==== START RUNNING ====")
    notif = ""
    for course in courses:
        if scraper.search_course(course) == 0:
            # succeed finding the class schedule
            if scraper.find_open_seat(course) == 0:
                # Found the numbe rof open seats
                if course.has_open_seats():
                    # only care about those that is opened
                    notif += f"✔️ Open: {str(course)}\n"
                else:
                    notif += f"❌ Closed: {str(course)}\n"
            else:
                notif += f"⚠️ Warning: {course} is not available.\n"
        else:
            notif += f"❗❗❗ Error: Invalid Course {course}.\n"

        scraper. reset()

    # print("==== FINISH RUNNING ====")
    return notif


def notify(message):
    notification = Notify()
    notification.application_name = "Course Reg Notif"
    notification.title = "Course Open Seat Notification"
    notification.message = message
    notification.icon = "./bot_icon.png"
    notification.send(block=False)


if __name__ == "__main__":
    courses = read_file(INPUT_FILE)
    scraper = CourseScrapper()
    notif = run(scraper, courses)

    notify(notif)
    scraper.close()
