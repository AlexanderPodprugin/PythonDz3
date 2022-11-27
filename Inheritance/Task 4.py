class Work():
    def __init__(self, place):
        self.place = place

    def workinfo(self):
        print(": ", self.place)

class WorkingStudent(Work):
    def __init__(self,place, name, study):
        super().__init__(place)
        self.name = name
        self.study = study

    def print_info(self):
        print(": ", self.name)
        print(": ", self.study)
        self.workinfo()

Alex = WorkingStudent("", "", "" )
Alex.print_info()