# AirBnB Clone Project

Welcome to the AirBnB clone project! This project involves creating a command interpreter to manage AirBnB objects. The command interpreter allows you to create, retrieve, update, and delete objects related to the AirBnB project.

## Table of Contents

- [Introduction](#introduction)
- [Command Interpreter](#command-interpreter)
- [Usage](#usage)
- [Execution](#execution)

## Introduction

The AirBnB clone project is a multi-step project aimed at building a full web application. The first step involves creating a command interpreter in Python using the `cmd` module. This command interpreter allows users to manage AirBnB objects by performing various operations such as creating, retrieving, updating, and deleting objects.

## Command Interpreter

The command interpreter is similar to a shell but is limited to specific use cases. It allows users to interact with the AirBnB objects through a set of commands. Some of the key functionalities include:

- Creating a new object (e.g., User, State, City, Place)
- Retrieving an object from a file or database
- Performing operations on objects (e.g., counting, computing stats)
- Updating attributes of an object
- Destroying an object

## Usage

To use the command interpreter, follow these steps:

1. Clone the project repository to your local machine.
2. Navigate to the project folder.
3. Run the command interpreter script: `./console.py`
4. Use the available commands to manage AirBnB objects.

## Execution

The command interpreter works in both interactive and non-interactive modes. In interactive mode, the prompt should be `(hbnb)`, and the user can enter various commands. In non-interactive mode, the interpreter should accept commands from standard input.

Example of interactive mode:
```bash
$ ./console.py
(hbnb) help
Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
(hbnb) quit
$
```

Example of non-interactive mode:
```bash
$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```
