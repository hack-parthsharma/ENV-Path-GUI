<h1 align="center">env-path-gui<br><br>

![Screenshot_2021-06-30-58_842x510](https://user-images.githubusercontent.com/54891285/123993164-d7704a80-d9e9-11eb-88df-3d2d1eeb7743.png)

</h1>

<h3 align="center">

<p align='center'>This helps you add or remove Linux $PATH Variables, easily.</p>
<p align='center'>A Tkinter based GUI to modify linux environment paths ($PATH)</p>

![Python](https://img.shields.io/badge/-python-333333?style=flat-square&logo=python)  


</h3>

## Support
- OS: Debian, Arch and Fedora-based OSs
- Shells: ZSH
- ⭕ Fish only supports adding paths (for now) ⭕

## Steps for installation

### Python3 and pip3 (Prereq)

- Debian Based
```
sudo apt-get -y install python3
sudo apt-get -y install python3-pip
```

- Arch Based
```
sudo pacman -S python
sudo pacman -S python-pip
```

- RedHat Based
```
sudo dnf install python3 -y
sudo dnf install python3-pip -y
```


### Tkinter Library (Prereq)

- Debian Based
```
sudo apt-get install python3-tk
```

- Arch Based
```
sudo pacman -S tk
```

- RedHat Based
```
sudo dnf install  python3-tkinter
```

## Setup
### Chmod and Run Setup
```
sudo chmod +x setup.sh
./setup.sh
```

## Run Using Terminal
```
python3 -u /usr/local/bin/main.py
```

## Run Using App Browser
Search for ```env-path-gui``` and run it.<br>
Terminal is set to open b default for debugging purposes.

## TODO
- [x] Setup.sh
- [x] Club Delete PATH and PATHS -> PATH
- [ ] Redesign UI
- [ ] Add support to modify the $PATHs
- [x] .desktop icon
- [x] .desktop file
- [ ] scrollbar
