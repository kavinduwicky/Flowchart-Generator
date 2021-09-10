print('Welcome to cab Service')
class Vehilist:
    def __init__(self):
        self._make = ''
        self._model = ''
        self._num = ''
        self._passenger = 0
        self._ac = ''
    def addVehicle(self):
        try:
            self._make = input('Enter vehicle Type (Car, Van, 3-Wheeler, Lorry, Truck): ')
            self._model = input('Enter vehicle model: ')
            self._year = int(input('Enter vehicle mileage: '))
            self._passenger = int(input('Enter Passenger Count: '))
            self._ac = input('Is there AC or not?(YES or NO): ')
            
            return True
        except ValueError:
            print('Please try entering vehicle information again using only whole numbers for Vehicle number and mileage')
            return False
    def __str__(self):
        return '\t'.join(str(x) for x in [self._make, self._model, self._num, self._passenger, self._ac])

class Cab:
    def __init__(self):
        self.vehicles = []
    def addVehicle(self):
        vehicle = Vehilist()
        if vehicle.addVehicle() == True:
            self.vehicles.append(vehicle)
            print ()
            print('This vehicle has been added, Thank you')
    def viewCab(self):
        print('\t'.join(['','Type', 'Model','Year', 'Color', 'Vehicle', 'Passengers', 'Condition']))
        for idx, vehicle in enumerate(self.vehicles) :
            print(idx + 1, end='\t')
            print(vehicle)

cab = Cab()
class Data:
    def __init__(self):
        self._name = ''
        self._location = ''
        self._drop = ''
        self._sv = 0
        self._tel = 0
        
    def addCustomer(self):
        try:
            self._name = input('Enter Your Name: ')
            self._location = input('Enter Your pick up location: ')
            self._drop = input('Enter Your droping: ')
            self._sv = int(input('Enter Selected vehicle: '))
            self._tel = int(input('Enter Your Phone no: '))
            
            return True
        except ValueError:
            print('Please try entering vehicle')
            return False
    def __str__(self):
        return '\t'.join(str(x) for x in [self._name, self._location, self._drop, self._sv, self._tel])

class Pick:
    def __init__(self):
        self.customers = []
    def addCustomer(self):
        customer = Data()
        if customer.addCustomer() == True:
            self.customers.append(customer)
            print ()
            print(' vehicle added, Thank you')
    def viewPick(self):
        print('\t'.join(['', 'Name', 'Get-Drop', 'V.No', 'Phone No']))
        for idx, customer in enumerate(self.customers) :
            print(idx + 1, end='\t')
            print(customer)

pick = Pick()
while True:
    print('Press 1 to Add  new vehicle to the system')
    print('Press 2 to Remove avehicle from the system')
    print('Press 3 to View Available Vehicles')
    print('Press 4 to Assign a hire')
    print('Press 5 to Release form hire after completing')
    print('Press 6 to See available vehicles in each category')
    print('Press 7 to EXIT')
    userInput=input(' Select  option from above: ')

    #add  vehicle
    if userInput=="1": 
        cab.addVehicle()

    #delete  vehicle
    elif userInput=='2':
        if len(cab.vehicles) < 1:
            print('there are no vehicles now in Cab Service')
            continue
        cab.viewCab()
        item = int(input('enter the number vehicle to be removed: '))
        if item - 1  > len(cab.vehicles):
            print('This is invalid number')
        else:
            cab.vehicles.remove(cab.vehicles[item - 1])
            print ()
            print('This vehicle removed')
            
    #list all vehicles        
    elif userInput == '3':
        if len(cab.vehicles) < 1:
            print(' there are no vehicles now in Cab Service')
            continue
        cab.viewCab()
        
    #add Customer   
    if userInput=="4":
            pick.addCustomer()
            
    #delete  Customer
    elif userInput=='5':
        if len(pick.customers) < 1:
            print('There are no customers now in Cab Service')
            continue
        pick.viewPick()
        item = int(input('enter the number customer to be removed: '))
        
        if item - 1  > len(pick.customers):
            print('This is invalid number')
        else:
            pick.customers.remove(pick.customers[item - 1])
            print ()
            print('This customer removed')
            
    #exit in loop        
    elif userInput == '6':
        if len(pick.customers) < 1:
            print('No one rented a vehicle ')
            continue
        pick.viewPick()
        
    #exit in loop    
    elif userInput == '7':
        print('Thank You, Come Again')
        break

#invalid user input enter
else:
        print('This is an invalid input. Please try again.')
