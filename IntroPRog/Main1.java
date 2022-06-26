public class Main {

    public static void main(String[] args) {
        
        int numero;
        int numeroCon;
        int esta;
        String mensaje, estaciones;

        mensaje = "Posible Cero";


        //Determinando si un numero positivo o negativo
        numero=1;
        if (numero!=0 && numero>0) {
            mensaje = "el numero es positivo";
        } else {
            mensaje = "el numero es negativo";
        }
        System.out.println(mensaje);

        //Contando de numeros usando while
        numeroCon=0;
        while(numeroCon<3){
            numeroCon++;
            System.out.println(numeroCon);
        }   

        //Ahora contando numeros con do while
        numeroCon=0;
        do {
            numeroCon++;
            System.out.println(numeroCon);
        } while(numeroCon<3);

        //Ahora contando numeros con For
        for(int numeroFor=0;numeroFor<3;numeroFor++){
            System.out.println(numeroFor);
        }
        //Sabiendo las estaciones con Switch case
        esta=4;
        switch (esta) {
            case 1:
                estaciones="Es Primavera";
                break;
            case 2:
                estaciones="Es Verano";
                break;
            case 3:
                estaciones="Es Otonio";
                break;  
            case 4:
                estaciones="Es invierno";
                break;            
            default:
                estaciones="No ha definido";
        }
        System.out.println(estaciones);
    }


}