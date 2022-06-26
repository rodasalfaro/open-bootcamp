import javax.swing.text.StyledEditorKit.BoldAction;

public class Main {

    public static void main(String[] args) {
        Cliente comprador = new Cliente();
        Trabajador empleado = new Trabajador();

        //Setter para objeto comprador de la clase Cliente
        comprador.setEdad(25);
        comprador.setNombre("Gerson");
        comprador.setTelefono("22359698");
        comprador.setCredito(true);

        //Setter para objeto empleado de la clase Trabajador
        empleado.setEdad(25);
        empleado.setNombre("Gerson");
        empleado.setTelefono("22359698");
        empleado.setSalario(2500);

        //Salida en pantalla resultado de asignacion a objeto comprador
        System.out.println("**************************************************************");  
        System.out.println(comprador.getEdad());
        System.out.println(comprador.getNombre());
        System.out.println(comprador.getTelefono());  
        System.out.println(comprador.isCredito()); 

        System.out.println("**************************************************************");         
    //Salida en pantalla resultado de asignacion a objeto empleado
        System.out.println(empleado.getEdad());
        System.out.println(empleado.getNombre());
        System.out.println(empleado.getTelefono());  
        System.out.println(empleado.getSalario());    
        System.out.println("**************************************************************");  
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

class Cliente extends Persona {
    Boolean credito;
    public void setCredito(boolean credito){
        this.credito = credito;
    }
    public Boolean isCredito(){
        return this.credito;
    }

}

class Trabajador extends Persona {
    int salario;

    public void setSalario(int salario){
        this.salario=salario;
    }
    
    public int getSalario(){
        return this.salario;
    }
}