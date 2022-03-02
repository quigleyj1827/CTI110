services = {'-': 0, 'Oil change' : 35, 'Tire rotation' : 19, 'Car wash' : 7, 'Car wax' : 12}

print('Davy\'s auto shop services')
print('Oil change -- $35')
print('Tire rotation -- $19')
print('Car wash -- $7')
print('Car wax -- $12\n')
oil_change = 35
tire_rotation = 19
car_wash = 7
car_wax = 12

service_one = input('Select first service:\n')

service_two = input('Select second service:\n')
print('')

print('Davy\'s auto shop invoice\n')
if(service_one == '-'):
  print('Service 1: No service')
else:
  print('Service 1: %s, $%d' % (service_one, services.get(service_one)))
if(service_two == '-'):
  print('Service 2: No service')
else:
  print('Service 2: %s, $%d' % (service_two, services.get(service_two)))
invoice_total = services.get(service_one) + services.get(service_two)
print('')
print('Total: $%d' % (invoice_total))
 

 