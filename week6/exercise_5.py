data=("John","Doe",53.44)
format_string="Hello"

print(format_string + " %s %s. Your current balance is $%s." % ( data[0], data[1] , data[2]) )