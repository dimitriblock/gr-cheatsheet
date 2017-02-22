% Open recorded cfile
f = fopen ('filename.cfile', 'rb');

% Activate recorded data type
%type = 'int'; % For int values
%type = 'char'; % For char values
%type = 'short'; % For cshort values
type = 'float'; % For float/complex values

% Read
v = fread (f, Inf, type);

% Activate for complex data type:
%v = v(1:2:end)+v(2:2:end)*j;

% Close cfile
fclose (f);

% Plot values
plot(v)


