import datetime
import os
from time import sleep

from selenium.webdriver.common.by import By


class TakeScreenshot:

    def __init__(self, driver):
        self.driver = driver
        self.working_dir = ""
        self.file_names = []
        self.used_file_names = []
        self.img_desc = []
        self.img_result = []

    def set_working_dir(self) -> object:
        """Set working directory, it is used for storing images, pdf report, and log file
        Args:
            None
        Notes:
            1. Get the current user's local documents directory
            2. Create a new folder inside the documents directory
            3. Create a 'working directory' based on strftime yyyy-mm-dd-hh.mm
        """
        documents_dir = os.path.expanduser("~/Documents")  # 1
        new_folder_name = "Test Capture"
        new_folder_path = os.path.join(documents_dir, new_folder_name)
        os.makedirs(new_folder_path, exist_ok=True)  # 2
        current_dt = datetime.datetime.now()
        formatted_dt = current_dt.strftime("%Y-%m-%d-%H.%M.%S")
        working_folder_name = "NCMS" + " " + formatted_dt
        working_folder_path = os.path.join(new_folder_path, working_folder_name)
        self.working_dir = working_folder_path
        os.makedirs(working_folder_path, exist_ok=True)  # 3

    def take_ss_w_desc(self,
                       result="Passed",
                       filename="filename_null",
                       desc="description_null",
                       duration=2  # default value (in seconds), for sleep before taking screenshot
                       ):
        """Take Element Screenshot of /html page
        Args:
            result (string): Result of that screenshot, either "Passed" (default), "Failed", "Warning", or "Done"
            filename (string): Screenshot saved using this string (by default is using .jpg), used in pdf file
            desc (string): Screenshot image description, used in pdf file
            duration (int or float): Sleep time before taking screenshot (default=2)
        Notes:
            Please beware to use certain string variable on 'filename'
            Reason: because windows by default can't naming a file using special char
            Furthermore see "Windows filesystems and naming conventions"
        """
        self.img_desc.append(desc)
        self.img_result.append(result)
        sleep(duration)
        if not os.path.exists(self.working_dir):
            os.makedirs(self.working_dir)
        screenshot_path = os.path.join(self.working_dir, datetime.datetime.now().strftime(
            "%H%M%S")  # datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S")
                                       + " "
                                       + filename
                                       + '.png')
        self.driver.find_element(By.XPATH, "/html").screenshot(screenshot_path)

    def write_scenario_txt(self, scenario_name, append_write=True):
        """Write scenario into ~data/scenario_result.txt
        Args:
            scenario_name (string): Scenario Name used in 1st column in scenario_result.txt
            append_write (bool, True): Choosing write condition to append or write a new one
        Notes:
            1. Based on working directory make a list of all files inside it,
            2. Ignore .log and .txt file inside directory,
            3. Remove the file on the list if is used/written into scenario_result.txt
            4. Declaring new_file_path to be written into ~data/scenario_result.txt
            5. Declaring open_mode to the file: a(append) or w(write)
            6. Write into ~data/scenario_result.txt
            7. Emptying working list img_desc and img_result
            8. Aggregating used_file_names (see point 3)
        """
        self.file_names = [f for f in os.listdir(self.working_dir) if
                           os.path.isfile(os.path.join(self.working_dir, f))]  # 1
        self.file_names = [a for a in self.file_names if ".log" not in a]  # 2
        self.file_names = [a for a in self.file_names if ".txt" not in a]  # 2
        self.file_names = [a for a in self.file_names if a not in self.used_file_names]  # 3
        new_file_name = "scenario_result.txt"  # 4
        new_file_path = os.path.join("data/", new_file_name)
        open_mode = "a"  # 5
        if append_write is False:
            open_mode = "w"
        with open(new_file_path, open_mode) as file:  # 6
            for index, file_name in enumerate(self.file_names):
                file.write(scenario_name
                           + "|" + str(index + 1) + ". " + file_name[7:-4]
                           + "|" + self.img_result[index]
                           + "|" + self.working_dir
                           + "\\" + file_name
                           + "|" + self.img_desc[index]
                           + "\n")
            self.img_desc = []  # 7
            self.img_result = []
        self.used_file_names += self.file_names  # 8

