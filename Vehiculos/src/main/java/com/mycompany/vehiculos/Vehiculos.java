/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.vehiculos;

/**
 *
 * @author Admin
 */
public class Vehiculos {

    public static void main(String[] args) {
        Carro p = new Carro();
        p.setMarca("Marca:nissan,");
        System.out.println(p.getMarca());
        p.setModelo("Modelo: V-Drive,");
        System.out.println(p.getModelo());
        p.setColor("Color: verde,");
        System.out.println(p.getColor());
        System.out.print("Precio:");
        p.setPrecio(7.2990000);
        System.out.println(p.getPrecio());        
        p.setAltura( 1.509);
        System.out.println("altura(mm):");
        System.out.println(p.getAltura());
        System.out.print("Largo(mm):");
        p.setLargo( 4.492);
        System.out.println(p.getLargo());
        System.out.print("Ancho(mm):");
        p.setAncho( 1.695);
        System.out.println(p.getAncho());
        System.out.print("Peso(kg):");
        p.setPeso( 1.070);
        System.out.println(p.getPeso());
        System.out.print("Año:");
        p.setAño( 2015);
        System.out.println(p.getAño());
    }
}
