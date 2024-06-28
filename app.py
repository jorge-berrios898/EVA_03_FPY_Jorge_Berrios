from modules_construccion import listar, limpieza, sol_data , existencia
from modules_data import sol_ans, rutaj, rutac


while True:
    listar(menup)
    ans = sol_ans
    limpieza()
    if ans == '1':
        existencia()
    if ans == '2':
        pass
    if ans == '3':
        pass
    if ans == '4':
        pass
    if ans == '5':
        exit('Error en el codigo')