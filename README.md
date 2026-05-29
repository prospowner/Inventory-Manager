# Inventory Manager CLI

An interactive, terminal-based stock management application written in Python. This utility serves as a clean execution model for tracking data mappings dynamically in-memory using dictionary structures.

## Features
* **Key-Value State Tracking:** Implements a Python dictionary tracking mechanism (`inventory = {}`) to dynamically pair strings (item names) with numerical data states (stock quantities).
* **Interactive Control Matrix:** Built with responsive CLI conditional branches (`if/elif/else`), enabling a user to perform conditional lookup and removal operations on the fly.
* **Mutating Methods:** Demonstrates clean utilization of dictionary pop sequences (`inventory.pop()`) to gracefully extract keys and safely reduce active memory profiles when an asset is removed.

## Future Engineering Enhancements
* Implement a `while True:` execution loop so the script keeps running continuously until the user chooses to exit.
* Add structural file reading and writing operations (`json` or `csv`) to persist the data locally between program restarts.

## How to Run
1. Ensure you have Python installed on your system.
2. Run the application utility from your terminal interface:
   ```bash
   python inventory.py
