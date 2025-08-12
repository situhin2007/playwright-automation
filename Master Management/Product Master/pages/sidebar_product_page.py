class Sidebar:
    def __init__(self, page):
        self.page = page
        self.employee_menu = "text=Employees"

    def go_to_employee_module(self):
        self.page.click("text='HR & WORKFORCE MANAGEMENT'")
        self.page.click(self.employee_menu)
