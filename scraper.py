from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from secrets import PORT, DRIVER_PATH
from selenium.webdriver.common.action_chains import ActionChains
from course import Course


class CourseScrapper:
    CLASS_SCHED_URL = "https://www.bu.edu/link/bin/uiscgi_studentlink.pl/1667162470?ModuleName=univschs.pl"

    def __init__(self, port=PORT) -> None:
        self.driver = Chrome(DRIVER_PATH, PORT)
        self.actions = ActionChains(self.driver)

    def search_course(self, course):
        # Navigate to class schedule
        try:
            self.driver.get(self.CLASS_SCHED_URL)

            # Select semester
            select = Select(self.driver.find_element(By.NAME, "SemList"))
            # need to change to course sem later
            select.select_by_visible_text(f"{course.get_sem()}")

            # Select College
            college_select = Select(
                self.driver.find_element(By.NAME, "College"))
            college_select.select_by_visible_text(course.college)

            # Input Department name
            dept_fill = self.driver.find_element(By.NAME, "Dept")
            dept_fill.clear()
            dept_fill.send_keys(course.dept)

            # Input for Course number
            number_fill = self.driver.find_element(By.NAME, "Course")
            number_fill.clear()
            number_fill.send_keys(course.course_num)

            # Click the go button
            go_button = self.driver.find_element(
                By.XPATH, "//input[@type= 'button'][@onclick='SearchSchedule()']")
            self.actions.click(go_button).perform()

            return 0
        except:
            return -1

    def find_open_seat(self, course):
        try:
            num_seats = self.driver.find_element(
                By.XPATH, f"//tr[./td/font[contains(a, '{course.course_num}') and contains(a, 'A1')]]/td[7]")

            course.set_open_seats(int(num_seats.text))

            return 0
        except:
            return -1

    def reset(self):
        self.driver.get(self.CLASS_SCHED_URL)

    def close(self):
        self.driver.close()


if __name__ == "__main__":
    c = Course("SPRG 23", "CAS", "CS", "411")
    s = CourseScrapper()
    s.search_course(c)
    s.find_open_seat(c)
