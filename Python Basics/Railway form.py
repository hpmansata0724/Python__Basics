class RailwayForm:
    formType="Reservation Form"
    def getData(self):
        print("Train No:",self.trainno)
        print("Train Name:",self.train)
        print("Passenger Name:",self.name)

rajApplication=RailwayForm()
rajApplication.name="Raj"
rajApplication.train="Gujarat Mail"
rajApplication.trainno=140080
print("*********",rajApplication.formType,"**********")
rajApplication.getData()
