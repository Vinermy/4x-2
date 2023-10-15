# Savefile structure
### 4x<sup>2</sup> ver 0.1.0

## General structure
The savefile consists of a `save.ini` file and a `save-data` directory.
The `save.ini` file acts as a header for the save,
describing general parameters of the saved game (e.g. stats of the player's civilization),
while the `save-data` folder stores the bulk of information, like discovered systems, built spaceships,
fleets and more.

## The `save.ini` file structure
* GAME-INFO
  * current-ingame-date `YYYY-MM-DD`
  * current-system-name `str`
* CIV-INFO
  * civilization-name `str`

## The `save-data` dir structure
```
./save-data
├─ /systems
│   └─ /system-names.json
```
