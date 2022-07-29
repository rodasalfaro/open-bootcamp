import os

os.system('clear')



class Alumno():
    
    def crear(self, nombrealumno, notaalumno):
        self.nombrealumno = nombrealumno
        self.notaalumno = notaalumno
        
    def imprime(self):
        print("Nombre del alumno :", self.nombrealumno)
        print("Nota obtenida :", self.notaalumno)
            
    def statusalumno(self):
        if self.notaalumno<6:
            print("Alumno reprobado\n")
        else:
            print("Alumno Aprobado\n")
    
    
    
primeralumno = Alumno()
segundoalumno = Alumno()
terceralumno = Alumno()

primeralumno.crear("Jose Alberto Perez",8)
segundoalumno.crear("Yoana Azucena Valdez",9)
terceralumno.crear("Joaquin Alvarado",4)

primeralumno.imprime()
primeralumno.statusalumno()
segundoalumno.imprime()
segundoalumno.statusalumno()
terceralumno.imprime()
terceralumno.statusalumno()
