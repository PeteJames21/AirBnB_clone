# **AirBnB clone**
A backend console for an AirBnB clone application

## **Usage**
```
./console.py
```

## **Supported Commands**

| Command   | Syntax                                           | Purpose                                                     |
| --------- | -------------------------------------------------| ------------------------------------------------------------|
| `help`    | `help`                                           | display all available commands                              |
| `create`  | `<className>.create()`                           | create a new instance of the given class and print the id   |
| `update`  | `<className>.update(<id>, <fieldName>, <value>)` | update an attribute of an object                            |
| `destroy` | `<className>.destroy(<id>)`                      | destroy a specific object                                   |
| `show`    | `<className>.show(<id>)`                         | print the string representation of a specific object        |
| `all`     | `<className>.all()`                              | display all instnaces of a given class                      |
| `count`   | `<className>.count()`                            | display the number of instances of a given class            |
| `quit`    | `quit`                                           | quit the program                                            |

`<className>` can be any class that inherits from `BaseModel`

The above commands can also be called using the following syntax:
```
<command> [className] [args]...
```

For example, the alternative syntax for the `create` command is:
```
create User
```
