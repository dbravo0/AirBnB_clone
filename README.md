# AirBnB clone - The console


## Description :page_facing_up:
first part of the prototype clone of AirBnB.

## Requirements & Installation :memo:
Have experience using python3, a linux terminal CLI (Command-Line Interface) that will work as the enviroment of the project.

For install and setup prototype you will need to first clone it through this command:
```
sudo git clone https://github.com/dbravo0/AirBnB_clone.git
```
then paste it on your terminal and press enter.

## How to use :wrench:
Opening the console you'll need to navigate to the project folder name as "AirBnB" then enter ./console.py in your terminal the user will meet a prompt labelled "(hbnb)" in your interface, all set and ready fo\
r usage.

### List of Commands
| **Command name** | **Description** |
| ---------------- | --------------- |
|[all] | Shows all objects of one type or all types |
|[create] | Creates an object |
|[destroy] | Deletes an object based on class name and ID (Saves the change into the JSON file) |
|[help] | Shows the description of all commands |
|[quit/EOF] | Exit the console |
|[show] | Shows an object based on class name & ID |
|[update] | Updates an object based on the class name and ID by adding or updating attribute (Saves the change into the JSON file) |
|["class".all()] | Retrieve all instances of a class |
|["class".count()] | Retrieve the number of instances of a class |
|["class".destroy("id")] | Destroy an instance based on his ID |
|["class".update("id", "attribute name", "attribute value")] | Destroy an instance based on his ID |
|["class".update("id", "dictionary representation")] | Update an instance based on his ID with a dictionary|

## Supported Classes :clipboard:
 - BaseModel
 - User
 - State
 - City
 - Amenity
 - Place
 - Review

### Start using the console
start the console with
```./console```
you will see:
```(hbnb)```
and can start to use the hbnb console
## How to use the HBNB console
### Syntax:
``` <command> <classname> <id>```
id don't apply to create command
### For help:
```help <command>```
### Examples:
#### For Help:
```
(hbnb)help create
create a new instace of a class
(hbnb)
```

### Example of how to use the console

#### help command:
```
(hbnb) help create

        Create a new instance and save it
```
#### user creation:
```
(hbnb) create User
d4eea5f1-1568-4652-a0df-91411c9700cc
```
#### show and update:
```
(hbnb) all
[[User] (d4eea5f1-1568-4652-a0df-91411c9700cc) {'created_at': datetime.datetime(2020, 2, 20, 1, 3, 15, 392308), 'updated_at': datetime.datetime(2020, 2, 20, 1, 3, 15, 392454), 'id': 'd4eea5f1-1568-4652-a0df-91411c9700cc'}]
(hbnb) show User
** instance id missing **
```
#### it requeires to type the ID of the user we are working on
```
(hbnb) show User d4eea5f1-1568-4652-a0df-91411c9700cc
[User] (d4eea5f1-1568-4652-a0df-91411c9700cc) {'created_at': datetime.datetime(2020, 2, 20, 1, 3, 15, 392308), 'updated_at': datetime.datetime(2020, 2, 20, 1, 3, 15, 392454), 'id': 'd4eea5f1-1568-4652-a0df-91411c9700cc'}
```
#### update allows to add traits and info to the user:
```
(hbnb) update User d4eea5f1-1568-4652-a0df-91411c9700cc first_name David
(hbnb) show User d4eea5f1-1568-4652-a0df-91411c9700cc
[User] (d4eea5f1-1568-4652-a0df-91411c9700cc) {'first_name': 'David', 'updated_at': datetime.datetime(2020, 2, 20, 1, 4, 28, 10680), 'id': 'd4eea5f1-1568-4652-a0df-91411c9700cc', 'created_at': datetime.datetime(2020, 2, 20, 1, 3, 15, 392308)}
```
#### destroy the user and exit program:
```
(hbnb) destroy User d4eea5f1-1568-4652-a0df-91411c9700cc
(hbnb) all
[]
(hbnb) EOF
```

### Built with
python3 (3.4.3)

## Authors
David Bravo Beltran - @dbravo0
