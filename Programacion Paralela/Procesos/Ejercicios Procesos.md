UD02 · Procesos

Bloque F · Conceptos y estados
30. Explica con tus palabras la diferencia entre programa y proceso usando una analogía propia (distinta a las de arriba).
31. Imprime el PID de tu proceso y el de su padre, y comprueba cuál es el PID del padre en el Administrador de tareas o con ps. Pista: os.getpid, os.getppid.
32. Dibuja a mano el diagrama de estados de un proceso con todas sus flechas. Después responde: ¿por qué un proceso bloqueado no puede pasar directamente a ejecución?
33. Clasifica en el estado correcto (NUEVO, LISTO, EJECUCIÓN, BLOQUEADO, TERMINADO) cada una de estas situaciones: (a) un proceso esperando a que el usuario escriba, (b) un proceso en cola esperando CPU, (c) un proceso que acaba de ser creado, (d) un proceso al que se le ha agotado el quantum.
34. Pon un ejemplo de cada: algo que sería computación paralela, algo distribuido y algo solo concurrente.
35. Usa Pool para calcular los cubos de los números del 1 al 8 en paralelo, protegiendo la ejecución correctamente. Pista: multiprocessing.Pool, map, __name__.

Bloque G · run()
36. Ejecuta python --version desde tu programa y muestra solo el número de versión. Pista: capture_output, text, .stdout, .split().
37. Ejecuta un comando que falle a propósito (por ejemplo, un argumento inválido) y muestra el código de retorno y el mensaje de error sin que el programa se detenga. Pista: .returncode, .stderr.
38. Haz lo mismo del ejercicio anterior, pero ahora con check=True, capturando la excepción y mostrando el código. Pista: CalledProcessError.
39. Lanza un ping con un timeout de 3 segundos y muestra "Tardó demasiado" si se supera. Pista: TimeoutExpired; el parámetro de número de paquetes cambia según el sistema.
40. Crea un directorio llamado prueba_psp desde Python, adaptando el comando a tu sistema operativo. Pista: cmd /c en Windows.

Bloque H · Popen()
41. Abre un programa gráfico, muestra su PID y espera a que lo cierres para imprimir su código de retorno. Pista: Popen, .pid, .wait().
42. Abre un programa y, mientras siga vivo, muestra "Sigue abierto..." cada segundo. Pista: poll(), None, time.sleep.
43. Abre tres programas distintos, espera 5 segundos y ábrelos y ciérralos con terminate(). Anota cuál no se cierra y por qué. Pista: lista de Popen.
44. Lanza un proceso largo (por ejemplo, ping continuo o sleep), pídele que termine y, si tras 3 segundos no lo ha hecho, mátalo. Pista: terminate, wait(timeout=...), kill.
45. Lanza 5 procesos y mata todos menos uno, recogiendo después el código de retorno de los muertos. Pista: lista, terminate, wait.
46. Cumple este pedido: "Lanza dos programas, indica cuál de los dos terminó antes y su código de retorno". Pista: poll en bucle.

Bloque I · Comunicación
47. Lanza un hijo en Python que lea una frase por stdin y devuelva su longitud, enviando la frase desde el padre. Pista: Popen, PIPE, communicate(input=...).
48. Lanza un hijo que reciba un número por stdin y devuelva su doble. Envía tres números en llamadas distintas y explica por qué communicate() no te lo permite. Pista: solo se puede llamar una vez.
49. Haz que un proceso hijo invierta el texto que recibe (de "hola" a "aloh") y que el padre lo muestre. Pista: slicing [::-1].
50. Lanza un hijo que escriba algo por stderr a propósito y recupéralo en el padre. Pista: stderr=PIPE, segundo valor de communicate().
51. Explica con un dibujo qué es un deadlock de pipe y cómo lo evita communicate().
Bloque J · Seguridad, zombies y teoría
52. Reescribe en forma segura esta llamada peligrosa: subprocess.run("dir " + carpeta, shell=True). Explica qué podría pasar si carpeta valiera x & del /q *.*.
53. Explica qué es un proceso zombie, en qué sistemas aparece y qué llamada lo evita. Después explica qué es un huérfano y quién lo adopta en Linux.
54. Haz una tabla comparando proceso e hilo en cuatro aspectos (memoria, coste, qué pasa si falla, comunicación).
55. Responde en voz alta, como en una entrevista: ¿cuándo usarías run() y cuándo Popen()? Pon un ejemplo real de cada uno.