# Guia: Usando as GPIO, Raspberry Pi.
<hr>
## Usando o Git:

### Setup:
git config --global user.name "Gabriel Pivato"
git config --global user.email "pivatogabriel@gmail.com"

### Criando Repo:
git clone https://gitlab.com/MrPivato/raspGPIO.git
cd raspGPIO
touch README.md
git add README.md
git commit -m "add README"
git push -u origin master

### Pasta já existente:
cd existing_folder
git init
git remote add origin https://gitlab.com/MrPivato/raspGPIO.git
git add .
git commit -m "Initial commit"
git push -u origin master

### Repo já existente:
cd existing_repo
git remote rename origin old-origin
git remote add origin https://gitlab.com/MrPivato/raspGPIO.git
git push -u origin --all
git push -u origin --tags