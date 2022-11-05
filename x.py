class Form:
    IS_FORM = True

    def __init__(self, ssn):
        self.ssn = ssn

    @staticmethod
    def ask_for_ssn_again():
        ssn = input("What is your ssn? ")
        print(f"Thanks for givinng me {ssn}")


class DischargeForm(Form):

    FORM_VERSION = "DD-215"

    def __init__(self, ssn, name, dob):
        super().__init__(ssn)
        self.name = name
        self.dob = dob
        print(self.IS_FORM)


d = DischargeForm(1234, "Bob", "12-12-1234")
print(d.ssn)
d.ask_for_ssn_again()
