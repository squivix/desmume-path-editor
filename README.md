# desmume-path-editor
A script that edits the path settings of [DeSmuME](http://desmume.org/) to make sure it always treats the directory where the rom is run as the save directory for States, Screenshots, StateSlots, Cheats, and SramImportExport. I made this because I prefer saving nds roms into seperate folders in order to have multiple profiles of the emulator. 

# Usage
On windows, download desmume-path-editor.exe from [releases](https://github.com/squivix/desmume-path-editor/releases/latest), copy it to the directory where you store the nds rom, run it instead of running the rom. The script will edit the path settings of DeSmuME to the current directory then run the nds rom from there. First time running it will ask you for the path of the desmume.ini file. This is typically found where you installed DeSmuME.
