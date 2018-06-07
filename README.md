# Guia: Usando as GPIOs, do Raspberry Pi.

## Passo 1: aprendendo a usar um pouco do Git.

### Segue abaixo a setup básica, usada por mim, a fim de exemplificar:

### Definindo usuário e e-mail:
    git config --global user.name "Gabriel Pivato"
    git config --global user.email "pivatogabriel@gmail.com"

### Criando o repositório no computador:
    git clone https://gitlab.com/MrPivato/raspGPIO.git
    cd raspGPIO
    touch README.md
    git add README.md
    git commit -m "add README"
    git push -u origin master

## Caso já o possua:

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

### Resultado:

![alt text](imgs/screen1.png "asdasd")

## No momento, apenas execute:
    git clone https://gitlab.com/MrPivato/raspGPIO.git