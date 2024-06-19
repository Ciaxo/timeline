# TimeLine

This project was created to facilitate determining the chronological order of events based on small pieces of information, such as those presented in the book "Cain's Jawbone".

## Project Description

The project consists of two main components:
- **LiniaCzasuApp**: An interface for visualizing and manipulating dots on a timeline.
- **OknoZLabelami**: Dialog windows for editing detailed information related to each dot on the timeline.

## Features
- **Adding Dots**: Upon launching the program, the user sees an empty timeline. To add a dot, simply click the middle mouse button on the timeline, enter a number, and confirm the selection. After these steps, a new dot appears on the timeline.

- **Categorization**: Double-clicking the left mouse button on a dot opens a category window. Categories are marked with colors, and next to each category is text describing it. To change the category text, double-click on it to open a window for entering new text and confirming the changes.

- **Moving Dots**: Hold the left mouse button on the dot and drag it to the desired position, then release the button.

- **Changing Dot Color**: To change the color of a dot, the user clicks Button-5 (one of the side buttons on the mouse), which opens a color selection window. After selecting a color, confirm the changes.

- **Deleting Dots**: Deleting a dot from the timeline is simple. Right-click on the dot, and the program will execute the deletion.

## File Structure

- `timeline.py`: Main application file containing the tkinter GUI setup.
- `info.txt`: Stores event details associated with each dot on the timeline.
- `colors.txt`: Stores color preferences for each dot on the timeline.

### LiniaCzasuApp

The `LiniaCzasuApp` class creates an interactive interface that includes a timeline and allows for adding, moving, editing, and deleting dots representing events on the timeline.

#### Functions

- `rysuj_linie_czasu`: Draws the timeline and updates dot positions based on data from a file.
- `dodaj_kropke`: Adds a new dot to the timeline when right-clicked.
- `przesuwaj_kropke`: Allows for dragging a dot on the timeline when left-clicked and dragged.
- `usun_kropke`: Deletes a dot from the timeline when right-clicked.
- `wyswietl_okno_z_labelami`: Displays a dialog window with detailed information about the selected dot when double-clicked with the left mouse button.

### OknoZLabelami

The `OknoZLabelami` class handles displaying a dialog window with five categories of information related to each dot on the timeline.

#### Functions

- `edytuj_tekst`: Allows editing texts for each of the five categories (season, time of day, place, people, events) when double-clicked on the respective label.
- `wczytaj_dane` and `zapisz_dane`: Functions for reading from and writing to a text file "info.txt" according to the dot index on the timeline.

### Technologies

The project utilizes the `tkinter` library for building the graphical interface and file operations for storing dot data and their details.
