class employee:    
    def __init__(self, employee_name = None, code = None):
        self.employee_name = employee_name
        self.code = code
        # stored as ints

        self.regular = ["cleaner", "manager"]

        self.hours = {"regular": 0, 
                    "dispatch": 0, 
                    "overtime": 0,
                    "office work": 0,
                    "travel": 0,
                    "trainee": 0,
                    "trainer": 0,
                    "reimbursement": 0,
                    "paycheck tips": 0,
                    "qc": 0,
                    "vacation": 0,
                    "holiday": 0,
                    "bonus": 0,
                    "paid time off": 0}
        
    def update_hours(self, category, time):
        if str(time) == 'nan':
            return
        for item in self.hours.keys():
            if item in category.lower():
                self.hours[item] += time
                return
        if category.lower() in self.regular:
            self.hours["regular"] += time
            return
        print(category.lower())
        print(self.hours.keys())
        print("MISSING HOUR CLASSIFICATIONS")
        exit(1)

    def update_tip(self, tip):
        if str(tip) == 'nan':
            return
        self.hours["paycheck tips"] += tip

    def update_reimbursement(self, reimbursement):
        if str(reimbursement) == 'nan':
            return
        self.hours["reimbursement"] += reimbursement

    def final_hours(self):
        self.hours["regular"] -= self.hours["overtime"]
        # for if they have no regular hours
        if self.hours["regular"] < 0:
            self.hours["regular"] = 0
        hours = []
        for item in self.hours.values():
            if item == 0:
                hours.append('')
            else:
                hours.append(item / 100)
                # [item / 100 for item in self.hours.values()]
        codeOut =  "0" * (9 - len(str(self.code))) + str(self.code)
        return [codeOut] + hours

    def __str__(self):
        return self.employee_name + " " + self.code + " " + str(self.tip / 100) + " " + str(self.reimbursement / 100) + ' ' + str(self.hours)
    
    def __eq__(self, other):
        if self.hours == other.hours:
            return True
        else:
            return False