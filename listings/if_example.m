% if ( CONDITION ) STATEMENT
% [elseif STATEMENT ]
% [else STATEMENT ]
% end.
% 
% EXAMPLE: What are we gonna 
% do today?
%

day=weekday(now);

if (day == 6 )
   disp('PUB!')
elseif (day == 1 || day == 7)
      disp('sleep')
else
   disp('duh.') 
end

