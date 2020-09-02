import pyautogui
import window_manager

class AutoLogin:
    def __init__(self, password_field_image, username, password):
        self.password_field_image = password_field_image
        self.username = username
        self.password = password

    def login(self):
        window_manager.bring_to_top('riot client')
        self.find_password_box(self.password_field_image)
        self.parse_values(self.password_box)
        self.current_pos = pyautogui.position()
        self.fill_username(self.username_pos[0], self.username_pos[1])
        self.fill_password(self.password_pos[0], self.password_pos[1])
        self.confirm(self.confirm_pos[0], self.confirm_pos[1])
        self.go_back(self.current_pos[0], self.current_pos[1])

    def find_password_box(self, image):
        self.password_box = None
        for i in range(10):
            self.password_box = pyautogui.locateOnScreen(self.password_field_image, grayscale = True)
            if self.password_box != None:
                break

    def parse_values(self, password_box) :
        self.password_pos = (password_box[0] + 10, password_box[1] + 10)
        self.username_pos = (self.password_pos[0], self.password_pos[1] - 75)
        self.confirm_pos = (self.password_pos[0] + 120, self.password_pos[1] + 150)

    def fill_username(self, username_x, username_y):
        pyautogui.click(username_x, username_y)
        pyautogui.write(self.username)

    def fill_password(self, password_x, password_y):
        pyautogui.click(password_x, password_y)
        pyautogui.write(self.password)

    def confirm(self, confirm_x, confirm_y):
        pyautogui.click(confirm_x, confirm_y)

    def go_back(self, current_x, current_y):
        pyautogui.moveTo(current_x, current_y)
