import datetime
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
class Record:
    def __init__(self, forename, surname, dob, gender, isCSStudent):
        self.__forename = forename
        self.__surname = surname
        self.__dob = dob
        self.__gender = gender
        self.__CS_student = isCSStudent
        self.time_of_creation = datetime.datetime.now()

    def Invalid(self):
        print("Invalid Data Type")

    def getFName(self):
        return self.__forename

    def setFName(self, value):
        if type(value) == str:
            self.forename = value
            return
        self.Invalid()

    def getLName(self):
        return self.__surname

    def setLName(self, value):
        if type(value) == str:
            self.__surname = value
            return
        self.Invalid()

    def getDOB(self):
        return self.__dob

    def getAge(self):
        age = datetime.date.today().year - int(self.__dob[6:])
        return age

    def setAge(self, value):
        if type(value) == int:
            self.__age = value
            return
        self.Invalid()

    def getGender(self):
        return self.__gender

    def setGender(self, value):
        if value.lower() == "m" or value.lower() == "f" or value.lower() == "male" or value.lower() == "female":
            self.__gender = value.title()
            return
        self.Invalid()

    def getCSStudent(self):
        return self.__CS_student

    def setCSStudent(self, value):
        if type(value) == bool:
            self.__CS_student = value
            return
        self.Invalid()

    def created(self):
        return self.time_of_creation

    def day_born(self):
        unit_date = int(self.__dob[:2]) if self.__dob[0] != "0" else int(self.__dob[1])
        date = datetime.datetime(int(self.__dob[6:]), int(self.__dob[3:5]), unit_date)
        return days[date.weekday()]

me = Record("Taimur", "Shaikh", "16/01/2004", "M", True)
