linea = "  2026-10-15 09:41:07 | ERROR | srv-web | Timeout en puerto 8080  "

fecha, codigo, servicio, mensaje = [c.strip() for c in linea.strip().split("|")]
puerto = int(mensaje.split()[-1])
print(puerto + 1)