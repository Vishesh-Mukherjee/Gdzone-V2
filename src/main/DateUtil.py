from datetime import datetime

class DateUtil:

    @staticmethod
    def stringToDate(str):
        return datetime.strptime(str, "%d-%m-%Y")

    @staticmethod
    def compareDate(date):
        if date == None:
            return True
        return date > datetime.now()

