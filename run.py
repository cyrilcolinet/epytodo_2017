#!/usr/bin/env python
##
## EPITECH PROJECT, 2018
## epytodo_2017
## File description:
## run file
##

from app import views
from app import app

if __name__ == "__main__":
    app.secret_key = 'o334eeZzrgrzG.,FEZ,;/FAGE.?_t_SOEIF_OKJOEZAGHR342'
    app.run()
