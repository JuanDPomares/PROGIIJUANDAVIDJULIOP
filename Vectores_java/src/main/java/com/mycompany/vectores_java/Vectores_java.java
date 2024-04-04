/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.vectores_java;
import java.util.ArrayList;
import java.util.Collections;
public class Vectores_java {

    
   public class Main {
    public static void main(String[] args) {

         ArrayList<Integer> listaVacia = new ArrayList<>();

      
        ArrayList<Integer> listaMasDe5 = new ArrayList<>();
        
            listaMasDe5.add(1);
        
        listaMasDe5.add(2);
        listaMasDe5.add(3);
        
        listaMasDe5.add(4);
        
        listaMasDe5.add(5);
        listaMasDe5.add(6);
            
        listaMasDe5.add(7);
        System.out.println(listaMasDe5);
        
        int longitudListaVacia = listaVacia.size();
        int longitudListaMasDe5 = listaMasDe5.size();
        int primerElementoListaMasDe5 = listaMasDe5.get(0);
        int elementoCentralListaMasDe5 = listaMasDe5.get(listaMasDe5.size() / 2);
        int ultimoElementoListaMasDe5 = listaMasDe5.get(listaMasDe5.size() - 1);
            System.out.println("la longitud de la lista mas de 5 es de:" +longitudListaMasDe5);
            System.out.println("la longitud de la lista vacia de:" +longitudListaVacia);
        
        
        ArrayList<Object> datosPersonales = new ArrayList<>();
            datosPersonales.add("Juan David Julio Pomares");
            datosPersonales.add(19);
            datosPersonales.add(1.73);
            datosPersonales.add("soltero");
            datosPersonales.add("cartagena");
            System.out.println(datosPersonales);
        
      
        ArrayList<String> itCompanies = new ArrayList<>();
        itCompanies.add("Facebook");
        itCompanies.add("Google");
        
        itCompanies.add("Microsoft");
        itCompanies.add("Apple");
        
        itCompanies.add("IBM");
        itCompanies.add("Oracle");
        itCompanies.add("Amazon");
        System.out.println(itCompanies);
            
        itCompanies.add(2, "Twitter");
        
            
        String empresaABuscar = "Google";
       
        boolean existeEmpresa = itCompanies.contains("Google");
        System.out.println("¿Existe google en la empresa? "  +existeEmpresa);
        
        Collections.sort(itCompanies);

        
        Collections.reverse(itCompanies);

        
        String primerEmpresaEliminada = itCompanies.remove(0);

        itCompanies.clear();
    }
}
}
