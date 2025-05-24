from msilib.schema import PublishComponent


#
# class Bird:
#     def fly(self):
#         print('Bird flying')
#
#
# class Plane:
#     def fly(self):
#         print('Plane flying')
#
#
#
# b = Bird()
# p = Plane()
#
# b.fly()
# p.fly()
#
#
# class CreditCard:
#     def __init__(self,credit_amount, credit_currency):
#         self.credit_amount = credit_amount
#         self.credit_currency = credit_currency
#
#
#     def transaction(self, sum):
#         self.credit_amount -= sum
#
#
# class MobilePayment:
#     def __init__(self, mobile_number, card_number, amount):
#         self.mobile_number = mobile_number
#         self.card_number = card_number
#         self.amount = amount
#
#     def transaction(self, sum):
#         self.amount -= sum
#
# mobile = MobilePayment('+996770324534', '123445678', 50000)
# credit = CreditCard(10000, 'USD')
#
# mobile.transaction(10000)
# credit.transaction(10000)
#

#
# class Electronics:
#     def __init__(self, ):


class BankAccount:
    def __init__(self, card_number, balance, cvv):
        self.card_number = card_number  # public
        self._balance = balance  #protected
        self.__cvv = cvv        # private

    def get_cvv(self, role):
        if role != 'Admin':
            raise ValueError('Role must be admin')
        else:
            return self.__cvv


    def set_cvv(self, cvv, role):
        if role != 'Admin':
            raise ValueError('Role must be admin')
        self.__cvv = cvv


aza = BankAccount('123456', '10000', 123)

print(aza.card_number)
print(aza._balance)
print(aza._BankAccount__cvv)


print(aza.get_cvv(admin))
aza.set_cvv(222, user)
print(aza.set_cvv())