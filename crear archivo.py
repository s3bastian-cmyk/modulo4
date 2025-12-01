import os

carpeta = "poo y funciones"

os.makedirs(carpeta, exist_ok=True)

for i in range(1, 100):
    ruta_archivo = os.path.join(carpeta, f"archivo_{i}.py")

    with open(ruta_archivo, "w") as f:
        f.write(f"#Este es el archivo número sebastian murcia {i}\n")

print("Archivos creados exitosamente.")