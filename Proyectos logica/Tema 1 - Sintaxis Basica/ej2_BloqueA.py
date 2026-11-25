tareas = 47
hilos = 6
tareasrest = tareas%hilos
tareaporhilo = tareas//hilos

print(f"Cada hilo puede realizar: {tareas//hilos} tareas. Y sobrarian {tareas%hilos} tareas sin realizar")

for i in range(1, hilos + 1):
    print(f"Hilo-{i}: {tareaporhilo + (1 if i <= tareasrest else 0)} tareas")
    


