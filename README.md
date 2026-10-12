# Restaurant Order Management System

A menu-driven Python console application for managing pizza orders with persistent CSV-formatted text storage.

## Project background

Created by **Prakash Bahadur G C** for **Software Design & Development**, International Study Centre, University of Huddersfield. The original portfolio was titled *Order Management Database Structure for the restaurant*.

## Features

- Place orders for Pepperoni or Veggie pizzas.
- Record customer name, email, phone number, order date and payment status.
- Calculate the total from pizza price and quantity.
- View all orders or search by customer name, email or phone number.
- Update customer details, pizza selection, quantity or payment status.
- Delete orders by order number.
- Save changes automatically and reload records on startup.

## Skills demonstrated

Python functions, lists, dictionaries, loops, conditional statements, string processing, basic input validation, exception handling, CSV file I/O and date handling.

## Run locally

Install Python 3.8 or newer. No third-party dependencies are required. From the repository root:

```bash
python src/order_manager.py
```

Use `python3` if that is your Python command.

## Menu

| Option | Action |
| --- | --- |
| 1 | Place an order |
| 2 | View all orders |
| 3 | Find orders |
| 4 | Update an order |
| 5 | Delete an order |
| 6 | Exit |

Example coursework menu prices: Pepperoni **£9.99**, Veggie **£5.99**. These are demonstration values, not verified current restaurant prices. Two Veggie pizzas total **£11.98**.

## Storage

The program writes `prakash.txt` in the current working directory, using eight CSV fields without a header. Python's `csv` module handles quoting, including commas in names. The generated file is excluded from Git. This is file-based storage, not a database server.

Use fictional customer details when trying the application. The payment field only records a yes/no status; the application does not process payments. The restaurant name in the console is retained from the coursework scenario; this is an independent student project, not an official restaurant application.


## Limitations and future improvements

Phone validation retains the original requirement for exactly 10 digits; it is not a general UK or international phone validator. Email validation is basic and differs between creation and updating. Records use floating-point totals, and malformed numeric values in manually edited storage can cause loading errors. Saving overwrites the file directly. There is no authentication or encryption. Order numbers can be reused if the highest-numbered order is deleted; they are unique among currently saved orders, not immutable historical identifiers.

Future improvements include stronger validation, decimal currency arithmetic, immutable IDs, atomic saves, database storage, automated tests and a graphical interface.
