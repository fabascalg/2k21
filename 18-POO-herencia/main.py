# utilizar clases - herencia

import clases


print("\nProgando clase \"Persona\"\n")

persona = clases.Persona()

persona.setNombre("Fernando")
persona.setApellidos("Robles")
persona.setAltura("190cm")
persona.setEdad("800 años")

print(f"{persona.informe()}")

print(persona.hablar())
print(persona.dormir())
print(persona.caminar())



print("\nProbando clase \"Informático\"")

tecnico = clases.Informatico()

tecnico.setNombre("Pedro")
tecnico.setApellidos("Ruíz")
tecnico.setAltura("202cm")
tecnico.setEdad("39 años")

print("-> desplegando datos heredados:")
print(tecnico.informe())
print("-> desplegando atributos propios:")
print(tecnico.getLenguajes())
print(tecnico.programar())
print(tecnico.repararOrdenador())


print("\nProbando clase \"Técnico de Redes\"")

teleco = clases.TecnicoRedes()

print(teleco.auditoria())
print(teleco.getLenguajes())
print(teleco.getExperiencia())
print(teleco.getAuditarRedes())
