# The following lab will involve mutliple mathematical problems, which are related and will be solved.

print('****************Rizwan Expressions Lab*****************');
print('   ');
print('The weather in Miami, Florida on a random Monday in the summer time was 98 degrees Fahrenheit.'); # string type
print('My friend, who is from Pakistan, wanted to know what the weather was like, but in degrees Celsius.'); # string type
msgString= "What would be the weather approximately in degrees";
print(msgString + ' Celsius?'); # string type

constant1= 5/9; # integer type, constant used to mutiply with the fahrenheit value
fahrenheit= 98; # fahrenheit value
constant2= 32; # integer type, another constant which is subtracted from the fahrenheit value

print('   ');
print('*celsius= constant1(fahrenheit-constant2) would be the formula to solve this problem*'); # string type, explaining what the formula would be to use to solve the problem
print('  ');
float_number1= float(constant1*(fahrenheit-constant2)); # float type, plugged in the aformentioned formula into the float value
print(float_number1, "degrees Celsius"); # output float number1

print('  ');
print('My other friend who is a scientist from Germany was also in town, he wanted to know the weather in Kelvin'); # string type
print('in order to see if the flowers he brought with him would be able to survive in the humid Miami weather or not.'); # string type
print(msgString + ' Kelvin?'); # string type
print('   ');

print('*celsiusValue+kelvinconstant would be the formula to solve this problem*'); # string type
print('  ');
celsiusValue= float_number1; # integer type, the Celsius value that we found from the previous equation
kelvinConstant= 273.15; # integer type, constant for Kelvin conversion from which we will subtract the Celsius value
float_number2= float(celsiusValue+kelvinConstant); # float type, formula for solving the Kelvin conversion
print(float_number2, "degrees Kelvin"); # output float number2


