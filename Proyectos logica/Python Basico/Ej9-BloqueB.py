alumnosIngles = {"Pablo", "Marta", "Omar", "Jesus", "Lucia", "Pedro"}
alumnosFrances = {"Omar", "Laura", "Ivan", "Pedro", "Lucia", "Manuel"}

print(f"Alumnos en ambas: {alumnosIngles & alumnosFrances}")
print(f"Alumnos en alguna de las dos: {alumnosIngles | alumnosFrances}")
print(f"Alumnos solo en Ingles: {alumnosIngles - alumnosFrances}")