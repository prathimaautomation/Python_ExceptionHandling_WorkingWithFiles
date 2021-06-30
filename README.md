# Working with Files
## Exception handling
### File permissions

##### Example of errors/exception
- 'ValueError'
- 'SyntaxError'
- 'TypeError'
- 'AttributeError'
- 'KeyError'
- `ZeroDivisionError`
- `FileNotFoundError`

##### File permissions

- 'r' This is the default mode. It opens file for reading
- 'w' This mode opens file for writing. If file doesn't exist, it creates a new file for us
- 'x' Creates a new file, if already exists, the operation fails
- 'a' Opens the file in Append Mode, if file doesn't exist it creates a new one
- 't' This is the default mode to open in text mode
- 'b' This is for binary mode
- '+' This will open a file for reading and writing(updating)

** we have 'try' 'except' and 'finally' **
- 'try' works as 'if condition'
- 'except' works as 'elif'
- 'finally' works as else, finally we execute regardless of 'try' and 'except' conditions
