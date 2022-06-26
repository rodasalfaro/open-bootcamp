public class tarea8 {

    public static void main(String[] args) {
        Persona alumno = new Persona();

        alumno.setEdad(25);
        alumno.setNombre("Gerson");
        alumno.setTelefono("22359698");

        System.out.println(alumno.getEdad());
        System.out.println(alumno.getNombre());
        System.out.println(alumno.getTelefono());               
    }


}

class Persona{
//Definiendo variables de propiedades    
    private int edad;
    private String nombre;
    private String telefono;
    
//Definiendo los Setters
    public void setEdad(int edad){
        this.edad = edad;
    }
    public void setNombre(String nombre){
        this.nombre = nombre;
    }
    public void setTelefono(String telefono){
        this.telefono = telefono;
    }
//Definiendo los Getters
    public int getEdad(){
        return this.edad;
    }
    public String getNombre(){
        return this.nombre;
    }
    public String getTelefono(){
        return this.telefono;
    }

}