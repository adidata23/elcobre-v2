import datetime
import os
import re
import shutil
from collections import deque, OrderedDict

from PIL import Image
from fpdf import FPDF


# Inheriting original FPDF (header and footer overriding)
class PDF(FPDF):
    # Class Constants
    font_size_lv0 = 18  # page title / test scenario font size
    font_size_lv1 = 12  # test step font size
    font_size_img_desc = 10  # image description font size
    left_indent = 15.5
    remaining_y = 0
    actual_y_needed = 0
    test_summary_list = []
    table_data = []
    cvpg_title = ""
    cvpg_subtitle = ""
    cvpg_author = ""
    cvpg_tcid = ""
    header_tcid = ""
    header_author = ""

    def __init__(self,
                 pdf_filename="",
                 param_path="D://Exploration//elcobre-v2//data//param.txt",
                 result_path="D://Exploration//elcobre-v2//data//scenario_result.txt",
                 cvpg_title="",
                 cvpg_subtitle="",
                 cvpg_author="",
                 cvpg_tcid="",
                 header_tcid="",
                 header_author="",
                 **kwargs
                 ):
        super().__init__(**kwargs)  # Call the parent class's __init__ method

        # Original data cruncher class variable
        self.SCENARIO_SAMPLE = []
        self.SCENARIO_LIST = []
        self.TC_PER_SCENARIO = []
        self.DICT_SCENARIO_COUNT = {}
        self.SUMMARY = {}
        self.PARAM = {}
        self.WORKING_DIR = ""
        self.result_path = result_path
        self.param_path = param_path
        self.cvpg_title = cvpg_title
        self.cvpg_subtitle = cvpg_subtitle
        self.cvpg_author = cvpg_author
        self.cvpg_tcid = cvpg_tcid
        self.header_tcid = header_tcid
        self.header_author = header_author

        # Additional for modular purposes
        if pdf_filename:  # is any string exist on pdf_filename
            pass
        else:
            print("pdf_filename is not defined")
            time_now_strf = datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S")
            pdf_filename = os.path.expanduser(f"~/Documents/result_from_{time_now_strf}.pdf")
        self.pdf_filename = pdf_filename
        print("pdf_filename: " + pdf_filename)

    # Imported (standalone) function for table of contents
    def render_toc(self, pdf, outline_list):
        toc_format = "{:<40} {:>10}"
        self.set_font("Helvetica", size=16)
        self.multi_cell(w=self.epw, h=self.font_size * 1.2, text="", new_x="LMARGIN", new_y="NEXT")
        self.set_font("Courier", size=10, style="B")  # Courier 10
        for section in outline_list:
            link = self.add_link(page=section.page_number)
            self.multi_cell(w=self.epw,
                            h=self.font_size * 1.2,
                            text=f'{" " * section.level * 2} {section.name} {"." * (83 - section.level * 2 - len(section.name))} {section.page_number}',
                            new_x="LMARGIN",
                            new_y="NEXT",
                            align="L",
                            link=link,
                            wrapmode="CHAR",
                            border=0)

    def header(self):
        if self.page_no() > 1:
            # set position of the header
            self.set_y(10)
            # Calculate effective page width
            self.margin_left = 10  # Example left margin in millimeters
            self.margin_right = 10  # Example right margin in millimeters
            self.total_page_width = 210  # Example total page width in millimeters (A4 size)
            # self.epw = total_page_width - (margin_left + margin_right)
            # Header
            self.set_font("Helvetica", size=9)
            line_height = self.font_size * 1.2
            col_width = self.epw / 10
            self.set_font(style="I", family="Helvetica")
            self.multi_cell(w=col_width * 1, h=line_height, text="", new_x="RIGHT", new_y="TOP")
            self.multi_cell(w=col_width * 1.5, h=line_height, text="Title", new_x="RIGHT", new_y="TOP", border=1,
                            align="L")
            self.set_font(style="BI", family="Helvetica")
            self.cell(col_width * 6.5, line_height, self.PARAM["header_title"], border=1, align="L")
            self.multi_cell(w=col_width * 1, h=line_height, text="", new_x="LMARGIN", new_y="NEXT")
            self.set_font(style="I", family="Helvetica")
            self.multi_cell(w=col_width * 1, h=line_height, text="", new_x="RIGHT", new_y="TOP")
            self.cell(col_width * 1.5, line_height, "Author", border=1, align="L")
            self.cell(col_width * 4.1, line_height,
                      self.header_author if self.header_author else self.PARAM["header_author"], border=1, align="L")
            self.cell(col_width * 1.2, line_height * 3, "Page", border=1, align="C")
            self.cell(col_width * 1.2, line_height * 3, f"{'  '}{self.page_no()} of {{nb}}", border=1, align="C")
            self.multi_cell(w=col_width * 1, h=line_height, text="", new_x="LMARGIN", new_y="NEXT")
            self.multi_cell(w=col_width * 1, h=line_height, text="", new_x="RIGHT", new_y="TOP")
            self.cell(col_width * 1.5, line_height, "Tools", border=1, align="L")
            self.cell(col_width * 4.1, line_height, self.PARAM["header_tools"], border=1, align="L")
            self.multi_cell(w=col_width * 1, h=line_height, text="", new_x="LMARGIN", new_y="NEXT")
            self.multi_cell(w=col_width * 1, h=line_height, text="", new_x="RIGHT", new_y="TOP")
            self.cell(col_width * 1.5, line_height, "Test Case ID", border=1, align="L")
            self.cell(col_width * 4.1, line_height, self.header_tcid if self.header_tcid else self.PARAM["header_tcid"],
                      border=1, align="L")
            self.ln(line_height * 2)

    def footer(self):
        if self.page_no() > 1:
            # set position of the footer
            self.set_y(-25)
            # set font
            self.set_font("Helvetica", 'I', 9)
            # page number
            col_width = self.epw / 9
            line_height = self.font_size * 1.5
            # draw line in this block of cell
            x = self.get_x()
            y = self.get_y() + 4
            self.line(x, y, x + col_width * 9, y)
            # move to next line
            self.ln(line_height)
            self.cell(col_width * 3, line_height, "Confidential", align="L")
            self.cell(col_width * 3, line_height, self.PARAM["footer_center"], align="C")
            self.cell(col_width * 3, line_height, f'Page {self.page_no()} of {{nb}}', align='R')

    def data_reader(self):
        # Make Directory, original fucntion: set_working_dir
        # Is removed, make directory now in take_screenshot.py (when capturing test images)

        # Original function: read_param(self, filename)
        script_dir = os.path.dirname(os.path.abspath(__file__))
        script_dir = os.path.dirname(script_dir)  # Up one directory, modified because moving report_pdf into /script
        script_dir = os.path.dirname(script_dir)
        file_path = os.path.join(script_dir, self.param_path)
        with open(file_path, 'r') as file:
            for line in file:
                key, value = line.strip().split('=')
                self.PARAM[key] = value

        # Original function: read_test_result(self, filename)
        script_dir = os.path.dirname(os.path.abspath(__file__))
        script_dir = os.path.dirname(script_dir)  # Up one directory, modified because moving report_pdf into /script
        script_dir = os.path.dirname(script_dir)
        file_path = os.path.join(script_dir, self.result_path)
        with open(file_path, 'r') as file:
            for line in file:
                parts = line.strip().split('|')
                # number below is determined by how many column on the txt files
                if len(parts) == 5:
                    self.SCENARIO_SAMPLE.append(list(parts))

        # Original function: get_unique_scenario
        unique_scenarios = OrderedDict()
        for scenario in self.SCENARIO_SAMPLE:
            unique_scenarios[scenario[0]] = None
        self.SCENARIO_LIST = list(unique_scenarios.keys())

        # Original function: get_count_unique_scenario and get_dict_scenario_count
        # self.get_unique_scenario()  # Make sure SCENARIO_LIST is populated first
        self.TC_PER_SCENARIO = [sum(1 for scenario in self.SCENARIO_SAMPLE if scenario[0] == unique_scenario) for
                                unique_scenario in self.SCENARIO_LIST]
        # self.get_count_unique_scenario()  # Make sure TC_PER_SCENARIO is populated first
        self.DICT_SCENARIO_COUNT = {scenario: count for scenario, count in
                                    zip(self.SCENARIO_LIST, self.TC_PER_SCENARIO)}

        # Create a dictionary to store the descriptions and statuses
        dummy_scenario_sample = [[a[0], a[2]] for a in self.SCENARIO_SAMPLE]
        scenario_status_dict = {}

        # Populate the dictionary with the statuses, giving priority to "Failed", "Warning", and then "Done"
        for description, status in dummy_scenario_sample:
            if description not in scenario_status_dict:
                scenario_status_dict[description] = status
            elif scenario_status_dict[description] == "Passed" and status == "Done":
                scenario_status_dict[description] = status
            elif scenario_status_dict[description] != "Failed" and scenario_status_dict[description] != "Warning":
                if status == "Failed" or status == "Warning":
                    scenario_status_dict[description] = status
                elif scenario_status_dict[description] != "Done":
                    scenario_status_dict[description] = status

        # Create the modified dummy_scenario_sample
        self.modified_dummy_scenario_sample = [[desc, status] for desc, status in scenario_status_dict.items()]
        # print(self.modified_dummy_scenario_sample)
        status_labels = ['Passed', 'Failed', 'Warning', 'Done', 'Total']
        summary_dict = {label: 0 for label in status_labels}
        for _, status in self.modified_dummy_scenario_sample:
            summary_dict[status] += 1
            summary_dict['Total'] += 1

        print(summary_dict)
        self.SUMMARY = summary_dict

    def generate_report(self):
        ###                      ###
        ### 1st Page Cover Title ###
        ###                      ###
        self.alias_nb_pages()
        self.add_page()
        self.set_font(family="Helvetica", style="", size=25)
        # Calculate effective page width
        margin_left = 10  # Example left margin in millimeters
        margin_right = 10  # Example right margin in millimeters
        total_page_width = 210  # Example total page width in millimeters (A4 size)
        epw = total_page_width - (margin_left + margin_right)
        col_width = epw / 10

        # Set BSI logo
        self.image("D://Exploration//elcobre-v2//data//bsi_logo.png", self.w - 70, 30, 60, 0)

        # Set 1st page cover title
        line_height = self.font_size * 1
        self.set_font('Helvetica', size=28, style="B")
        available_height = self.h - self.get_y()  # Calculate available height from current Y-coordinate
        content_height = line_height * 5  # Height of your multi_cell content
        y_coordinate = self.get_y() + (
                    available_height - content_height) / 2  # Calculate Y-coordinate to center the content vertically
        self.set_y(y_coordinate)  # Set the Y-coordinate for the next content
        self.multi_cell(w=col_width * 10, h=line_height,
                        text=self.cvpg_title if self.cvpg_title else self.PARAM["cover_page_title"], align="R",
                        new_x="LEFT", new_y="NEXT", border=0)

        # Set 1st page title description
        self.set_font('Helvetica', size=14, style="BI")
        self.multi_cell(w=col_width * 10, h=line_height,
                        text=self.cvpg_subtitle if self.cvpg_subtitle else self.PARAM["cover_page_subtitle"], align="R",
                        new_x="LEFT", new_y="NEXT", border=0)

        # Set 1st page author
        self.set_font('Helvetica', size=12, style="")
        self.multi_cell(w=col_width * 10, h=line_height * 9, text="", new_x="LEFT", new_y="NEXT", border=0)
        self.multi_cell(w=col_width * 3.5, h=line_height, text="", new_x="RIGHT", new_y="TOP", border=0)
        self.multi_cell(w=col_width * 1.5, h=line_height, text="Author", align="L", new_x="RIGHT", new_y="TOP", border=0)
        self.multi_cell(w=col_width * 4, h=line_height,
                        text=": " + self.cvpg_author if self.cvpg_author else ": " + self.PARAM["cover_page_author"],
                        align="L", new_x="RIGHT", new_y="TOP", border=0)
        self.multi_cell(w=col_width * 1, h=line_height, text="", new_x="LMARGIN", new_y="NEXT", border=0)
        self.multi_cell(w=col_width * 3.5, h=line_height, text="", new_x="RIGHT", new_y="TOP", border=0)
        self.multi_cell(w=col_width * 1.5, h=line_height, text="Test Case Id", align="L", new_x="RIGHT", new_y="TOP",
                        border=0)
        self.multi_cell(w=col_width * 4, h=line_height,
                        text=": " + self.cvpg_tcid if self.cvpg_tcid else ": " + self.PARAM["cover_page_tcid"],
                        align="L", new_x="RIGHT", new_y="TOP", border=0)
        self.multi_cell(w=col_width * 1, h=line_height, text="", new_x="LMARGIN", new_y="NEXT", border=0)

        ###                      ###
        ###       2nd Page       ###
        ###   Table of Contents  ###
        ###                      ###
        self.add_page()
        self.start_section(name="Table of Contents", level=0, strict=True)
        line_height = self.font_size * 1.15
        self.set_font('Helvetica', size=18, style="B")
        self.multi_cell(w=col_width * 10, h=line_height * 3, text="Table of Contents", align="C", new_x="LMARGIN",
                        new_y="NEXT", border=0)

        # Write the table of contents using fpdf2 built-in
        # Insert rendering by approximate counting of total line in TOC (Using Helvetica 18)
        # Find this term in fpdf.py and comment it "ncms_edit"
        toc_line_count = 2 + len(self.SCENARIO_LIST) + len(self.SCENARIO_SAMPLE)
        if toc_line_count < 54:
            self.insert_toc_placeholder(self.render_toc, 1)
        elif toc_line_count < 108:
            self.insert_toc_placeholder(self.render_toc, 2)
        else:
            self.insert_toc_placeholder(self.render_toc, 3)

        ###                      ###
        ###       3rd Page       ###
        ### Environment Details  ###
        ###                      ###

        ###                      ###
        ###   Document Summary   ###
        ###                      ###

        # self.add_page() # commented because toc_placeholder built-in method has include add_page()
        self.start_section(name="Document Summary", level=0, strict=True)
        self.set_font('Helvetica', size=18, style="B")
        self.multi_cell(w=col_width * 10, h=line_height * 4, text="Document Summary", align="C", new_x="LMARGIN",
                        new_y="NEXT", border=0)

        # Test Summary
        self.set_font("Helvetica", size=11, style="B")
        self.set_fill_color(135, 206, 235)  # Sky blue color
        test_summary_list = [list(self.SUMMARY.keys()), [str(value) for value in
                                                         self.SUMMARY.values()]]  # Convert the test_summary dictionary into the list format
        self.multi_cell(w=col_width * 2, h=line_height * 1.5, text=test_summary_list[0][0], align="C", new_x="RIGHT",
                        new_y="TOP", border=1, fill=True)
        self.multi_cell(w=col_width * 2, h=line_height * 1.5, text=test_summary_list[0][1], align="C", new_x="RIGHT",
                        new_y="TOP", border=1, fill=True)
        self.multi_cell(w=col_width * 2, h=line_height * 1.5, text=test_summary_list[0][2], align="C", new_x="RIGHT",
                        new_y="TOP", border=1, fill=True)
        self.multi_cell(w=col_width * 2, h=line_height * 1.5, text=test_summary_list[0][3], align="C", new_x="RIGHT",
                        new_y="TOP", border=1, fill=True)
        self.multi_cell(w=col_width * 2, h=line_height * 1.5, text=test_summary_list[0][4], align="C", new_x="LMARGIN",
                        new_y="NEXT", border=1, fill=True)
        self.multi_cell(w=col_width * 2, h=line_height * 1.5, text=test_summary_list[1][0], align="C", new_x="RIGHT",
                        new_y="TOP", border=1)
        self.multi_cell(w=col_width * 2, h=line_height * 1.5, text=test_summary_list[1][1], align="C", new_x="RIGHT",
                        new_y="TOP", border=1)
        self.multi_cell(w=col_width * 2, h=line_height * 1.5, text=test_summary_list[1][2], align="C", new_x="RIGHT",
                        new_y="TOP", border=1)
        self.multi_cell(w=col_width * 2, h=line_height * 1.5, text=test_summary_list[1][3], align="C", new_x="RIGHT",
                        new_y="TOP", border=1)
        self.multi_cell(w=col_width * 2, h=line_height * 1.5, text=test_summary_list[1][4], align="C", new_x="LMARGIN",
                        new_y="NEXT", border=1)
        self.ln(line_height * 0.5)

        # Test Summary Legends
        self.set_font("Helvetica", size=9, style="B")
        self.multi_cell(w=col_width * 10, h=self.font_size, text="Legend :", align="L", new_x="LMARGIN", new_y="NEXT",
                        border=0)
        self.set_font("Helvetica", size=7, style="B")
        self.set_text_color(0, 128, 0)
        self.multi_cell(w=col_width * 0.7, h=self.font_size, text="Passed", align="L", new_x="RIGHT", new_y="TOP",
                        border=0)
        self.set_text_color(0, 0, 0)
        self.multi_cell(w=col_width * 9.3, h=self.font_size,
                        text=": A step with a success verification/a scenario with success verification without "
                             "warning/failed step",
                        align="L", new_x="LMARGIN", new_y="NEXT", border=0)
        self.set_text_color(220, 50, 0)
        self.multi_cell(w=col_width * 0.7, h=self.font_size, text="Failed", align="L", new_x="RIGHT", new_y="TOP",
                        border=0)
        self.set_text_color(0, 0, 0)
        self.multi_cell(w=col_width * 9.3, h=self.font_size,
                        text=": A step with a failed verification/a scenario that contains any failed step", align="L",
                        new_x="LMARGIN", new_y="NEXT", border=0)
        self.set_text_color(255, 204, 0)
        self.multi_cell(w=col_width * 0.7, h=self.font_size, text="Warning", align="L", new_x="RIGHT", new_y="TOP",
                        border=0)
        self.set_text_color(0, 0, 0)
        self.multi_cell(w=col_width * 9.3, h=self.font_size,
                        text=": A step with minor bug or defect/a scenario that contain any warning step without any failed step. e.g: Displayed message is incorrect.",
                        align="L", new_x="LMARGIN", new_y="NEXT", border=0)
        self.multi_cell(w=col_width * 0.7, h=self.font_size, text="Done", align="L", new_x="RIGHT", new_y="TOP",
                        border=0)
        self.multi_cell(w=col_width * 9.3, h=self.font_size,
                        text=": A step without any verification/a scenario without any passed, warning or failed step",
                        align="L", new_x="LMARGIN", new_y="NEXT", border=0)
        self.ln(line_height)

        # Write table header
        self.set_font("Helvetica", size=11, style="B")
        self.set_fill_color(135, 206, 235)  # Sky blue color
        line_height = self.font_size * 1.8
        self.cell(col_width * 2.5, line_height, "Scenario Name", border=1, align="C", fill=True)
        self.cell(col_width * 6, line_height, "Step Name", border=1, align="C", fill=True)
        self.cell(col_width * 1.5, line_height, "Status", border=1, align="C", fill=True)
        self.ln()

        # Make a deque data structure to improving performance on pop->popleft function (using "from collections
        # import deque") Read these "why pop() is efficient on deque (double ended queue) rather than list"
        deque_test_step = deque(self.SCENARIO_SAMPLE)
        # write the content table
        line_height = self.font_size * 1.4
        for index, unique_scenario in enumerate(self.SCENARIO_LIST):
            self.set_font("Helvetica", size=11, style="B")
            count = self.DICT_SCENARIO_COUNT.get(unique_scenario, 0)
            self.cell(col_width * 2.5, line_height * count, "", border=1, align="L", new_x="LEFT", new_y="TOP")
            if self.modified_dummy_scenario_sample[index][1] == "Passed":
                self.set_text_color(0, 128, 0)
            elif self.modified_dummy_scenario_sample[index][1] == "Warning":
                self.set_text_color(255, 204, 0)
            elif self.modified_dummy_scenario_sample[index][1] == "Failed":
                self.set_text_color(220, 50, 0)
            self.multi_cell(w=col_width * 2.5, h=line_height, text=unique_scenario, align="L", new_x="RIGHT",
                            new_y="TOP")
            self.set_text_color(0, 0, 0)
            iteration_cnt = 0
            for _ in range(count):
                # Your code to iterate here
                iteration_cnt += 1
                # print(f"Iterating for scenario: {unique_scenario} " + str(deque_test_step[0]))
                if iteration_cnt != 1:
                    self.cell(col_width * 2.5)
                self.set_font("Helvetica", size=11, style="")
                self.cell(col_width * 6, line_height, deque_test_step[0][1], border=1, align="L")
                self.set_font("Helvetica", size=11, style="B")
                if deque_test_step[0][2] == "Passed":
                    self.set_text_color(0, 128, 0)
                elif deque_test_step[0][2] == "Warning":
                    self.set_text_color(220, 220, 0)
                elif deque_test_step[0][2] == "Failed":
                    self.set_text_color(220, 50, 0)
                self.cell(col_width * 1.5, line_height, deque_test_step[0][2], border=1, align="C")
                self.set_text_color(0, 0, 0)
                self.ln(line_height)
                deque_test_step.popleft()

        ###                      ###
        ###     Main Content     ###
        ###        Example       ###

        # Same format as to write the Document Summary with some tweaking
        deque_test_step = deque(self.SCENARIO_SAMPLE)
        # Check the remaining x for image width compression
        img_max_w = int(self.w - self.get_x() - self.left_indent)  # print(img_max_w) = 184.5015555555555
        # write the content table
        for index, unique_scenario in enumerate(self.SCENARIO_LIST, start=1):
            # print(index, self.TC_PER_SCENARIO[index-1], unique_scenario)
            self.add_page()
            self.set_font('Helvetica', size=self.font_size_lv0, style="B")
            count = self.DICT_SCENARIO_COUNT.get(unique_scenario, 0)
            self.start_section(name=unique_scenario, level=0, strict=True)
            self.multi_cell(w=col_width * 10, h=line_height * 1.2, text=unique_scenario, align="C", new_x="LMARGIN",
                            new_y="NEXT", border=0)
            self.multi_cell(w=col_width * 10, h=line_height, text="", align="C", new_x="LMARGIN", new_y="NEXT", border=0)
            count_step = 0  # used for checking last of test step iteration
            image_desc = ""
            for _ in range(count):
                count_step += 1
                # Checking remaining space here,
                remaining_y = self.h - self.get_y()

                # Using pillow, determine image_height based on original image aspect ratio
                image = Image.open(deque_test_step[0][3])
                original_width, original_height = image.size

                # Calculate the new height while maintaining aspect ratio
                aspect_ratio = original_width / original_height
                image_height = round(0.5 + (img_max_w / aspect_ratio))

                # Calculating y needed for the image, etc
                actual_y_needed = self.font_size_lv1 + image_height + self.font_size_img_desc + line_height  # height of test_step + image + desc + ln
                # print(deque_test_step[0][1],"--" , round(remaining_y), round(actual_y_needed), font_size_lv1, image_height, font_size_img_desc, line_height)
                if count_step == 1:
                    pass
                elif count_step > 1 and remaining_y < actual_y_needed:
                    if count_step != self.TC_PER_SCENARIO[index - 1]:  # checking remaining_y and last_test_step
                        self.add_page()
                    else:
                        self.add_page()

                # Add test case number
                self.set_font('Helvetica', size=self.font_size_lv1, style="B")
                self.set_text_color(50, 50, 220)
                self.start_section(name=deque_test_step[0][1], level=1, strict=True)
                self.multi_cell(w=col_width * 10, h=line_height, text=deque_test_step[0][1], align="L", new_x="LMARGIN",
                                new_y="NEXT", border=0)
                self.set_text_color(0, 0, 0)

                # Add image here
                image_x = self.set_x(self.left_indent)  # left indentation of the image, default is: self.get_x()
                image_y = self.get_y()
                self.image(deque_test_step[0][3], x=image_x, y=image_y, w=img_max_w)  # Adjust w and h as needed
                self.ln(image_height)  # this line drop is needed based on image.h

                if len(deque_test_step[
                           0]) == 4:  # This condition is for older version of scenario_result.txt, use elif instead

                    # Using regex to capture the file name to be inputted into image description
                    match = re.search(r'\\([^\\]+\.png)', deque_test_step[0][3])  # \\image\\(.*\.png)
                    if match:
                        image_desc = match.group(1)
                        image_desc = image_desc[:-4]  # Remove the last 4 characters (.png)

                elif len(deque_test_step[0]) == 5:
                    image_desc = deque_test_step[0][4]

                # Add image description here
                self.set_font('Helvetica', size=self.font_size_img_desc, style="I")
                self.set_x(15)  # left indentation of the img_description
                self.multi_cell(w=col_width * 10, h=line_height, text=image_desc, align="L", new_x="LMARGIN",
                                new_y="NEXT", border=0)
                self.ln()

                deque_test_step.popleft()  # deque_test_step pop every iteration

        # shutil copy of scenario_result.txt only if pdf_filename is exist with working directory
        if self.pdf_filename:
            pattern = r"^(.*\/)"  # capture string from the start until last /
            match = re.search(pattern, self.pdf_filename)
            if match:
                documents_path = match.group(1)
                documents_path += "scenario_result_fin.txt"
            else:
                print("regex pattern not found")
            script_dir = os.path.abspath(__file__)
            script_dir = os.path.dirname(
                script_dir)  # Up one directory, modified because moving report_pdf into /script
            script_dir = os.path.dirname(
                script_dir)  # Up one directory, modified because moving report_pdf into /script
            script_dir = os.path.dirname(script_dir)
            file_path = os.path.join(script_dir, r"D://Exploration//elcobre-v2//data//scenario_result.txt")
            shutil.copyfile(file_path, documents_path)

        # Checking condition if pdf_filename is absolute path or not
        # If it is print pdf file into two places, it absolute path and inside workspace
        output_2nd = re.search(r'[^/\\]+$', self.pdf_filename).group() if re.search(r'[^/\\]+$',
                                                                                    self.pdf_filename) else None
        if '//' in self.pdf_filename or '\\' in self.pdf_filename:
            self.output("report//" + output_2nd)
            self.output(self.pdf_filename)
        else:
            self.output(self.pdf_filename)


"""
# Testing script new, 20231121
a = PDF(cvpg_subtitle="Sprint 5 VA Billing Creation",
        cvpg_author="Automation Team - Alfan",
        cvpg_tcid="VA Billing Static Close",
        header_author="Automation Team - Alfan",
        header_tcid="LIFO Multiple Recur.Daily Waive Fix")
a.data_reader()
a.generate_report()
"""