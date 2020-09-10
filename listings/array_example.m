% EXAMPLE: Array definition, initialization and 
%
clc;            %clear screen

myArray=[];     %definition, 'myArray' exists
length(myArray) %but is not initialized yet
%myArray(1) would give error at this point

%really definition and initialization can be done in one step
myArray2 = rand(1,10)
length(myArray2)

%what's the last element?
myArray2(length(myArray2))

%more dimensions?
myArray3 = rand(1:3);
myArray3(1,2,3)

