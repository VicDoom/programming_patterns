import zope.interface
from zope.interface import implements, implementer
from zope.component import adapts
import datetime
from dateutil.relativedelta import relativedelta

class InterfaceSeparateFioDate(zope.interface.Interface):

    def get_fio(self):
        """Getting FIO"""
        pass

    def get_birth_date(self):
        """Getting Date"""
        pass


class InterfaceJointlyFioDate(zope.interface.Interface):

    def get_initials_birth_date(self):
        """Getting FIO and Date"""
        pass


class User:
    def __init__(self, fio, date):
        self.fio = fio
        self.date = date


@implementer(InterfaceSeparateFioDate)
class SeparateFioDate(User):

    def get_fio(self):
        return self.fio

    def get_birth_date(self):
        return self.date


# @implementer(InterfaceJointlyFioDate)
# class JointFioDate(User):
#
#     def get_initials_birth_date(self):
#         return self.fio + ' ' + self.date

@implementer(InterfaceJointlyFioDate)
class AdapterForSeparateFioDate:

    def __init__(self, obj: InterfaceSeparateFioDate):
        self.obj = obj

    def get_initials_birth_date(self):
        first, name, surname = self.obj.fio.split(' ')
        initials = name[0], surname[0]

        day, month, year = map(int, self.obj.date.split('.'))
        date_birth = datetime.date(year, month, day)
        day_now = datetime.date.today()

        date_relative = relativedelta(day_now, date_birth)
        return f'initials: {initials[0]}.{initials[1]}.' + " " + str(date_relative.years)


def client_code(obj: InterfaceJointlyFioDate):
    print(obj.get_initials_birth_date() + '\n')


if __name__ == '__main__':
    separate = SeparateFioDate("Kushnaryov Nikita Mihailovich", "19.07.1999")
    try:
        print(separate.get_fio())
        client_code(separate)
    except:
        print("Uncopetible types\n")

    adapter = AdapterForSeparateFioDate(separate)
    client_code(adapter)



