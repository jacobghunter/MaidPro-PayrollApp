class employee:
    def __init__(self, employee_name, code):
        self.employee_name = employee_name
        self.code = code
        self.categories = {}
        # stored as ints
        self.tip = 0
        self.reimbursement = 0
    def update_hours(self, category, hours):
        if category in self.categories.keys():
            self.categories[category] += hours
        else:
            self.categories[category] = hours
    def update_tip(self, tip):
        self.tip += tip
    def update_reimbursement(self, reimbursement):
        self.reimbursement += reimbursement
    def final_output(self):
        # subtract overtime from 'regular' hours
        # convert back to floats
        
        pass
    def __str__(self):
        return self.employee_name + " " + self.code + " " + str(self.tip / 100) + " " + str(self.reimbursement / 100) + ' ' + str(self.categories)