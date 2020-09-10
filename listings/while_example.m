% while ( CONDITION ) 
%   STATEMENT
% end.
% 
% EXAMPLE: Tell me when a new minute starts
%
clc;            %clear screen
c=clock;        %get time vector

% 6th element of c is seconds
while ( c(6) < 59.9)
    c=clock;
end
disp('start new minute of your life');
