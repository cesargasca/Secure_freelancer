/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author hidal
 */


package FirmaDigital;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.security.Security;
import java.util.logging.Level;
import org.bouncycastle.jce.provider.BouncyCastleProvider;
import org.bouncycastle.util.encoders.*;
import org.bouncycastle.crypto.digests.*;

/**
* @author http://myprogramminglab.blogspot.com/
*/

public class hashBouncy {
   /* public static void main(String[] args) throws IOException, NoSuchAlgorithmException {
        //add the security provider
        //not required if you have Install the library
        //by Configuring the Java Runtime
        Security.addProvider(new BouncyCastleProvider());

        //abrimos el archivo
          String cadena,cadena2="";
          FileReader f;
        try {
            f = new FileReader("C:\\Users\\hidal\\Desktop\\Semestre5\\crypto\\aes_aunmejor\\AES\\src\\contrato.pdf");
            BufferedReader b = new BufferedReader(f);
            while((cadena= b.readLine())!=null) {
                cadena2 = cadena2.concat(cadena);
            }
            b.close();
        } catch (FileNotFoundException ex) {
        }
            
        //todo el archivo en una cadena    
        System.out.println(cadena2);
        //cadena para sacar hash
        byte [] input =  cadena2.getBytes();
        
        /* MD5
        //this is the input;

        //update the input of MD5
        MD5Digest md5 = new MD5Digest();
        md5.update(input, 0, input.length);

        //get the output/ digest size and hash it
        byte[] digest = new byte[md5.getDigestSize()];
        md5.doFinal(digest, 0);
        */
         /*
        MessageDigest digest = MessageDigest.getInstance("SHA-256");
        byte[] digest2 = digest.digest(input);
        
        //show the input and output
        System.out.println("Input (hex): " +
            new String(Hex.encode(input)));
        System.out.println("Output (hex): " +
            new String(Hex.encode(digest2)));
        
        BufferedWriter out = new BufferedWriter(new FileWriter("hash.txt"));
        out.write(new String(Hex.encode(digest2)));
        out.close();
        
    } */
    
    public String generarHash(String archivo) throws IOException, NoSuchAlgorithmException{
         //add the security provider
        //not required if you have Install the library
        //by Configuring the Java Runtime
        Security.addProvider(new BouncyCastleProvider());

        //abrimos el archivo
          String cadena,cadena2="";
          FileReader f;
        try {
            f = new FileReader(archivo);
            BufferedReader b = new BufferedReader(f);
            while((cadena= b.readLine())!=null) {
                cadena2 = cadena2.concat(cadena);
            }
            b.close();
        } catch (FileNotFoundException ex) {
        }
            
        //todo el archivo en una cadena    
        //System.out.println(cadena2);
        //cadena para sacar hash
        byte [] input =  cadena2.getBytes();
        

        
        MessageDigest digest = MessageDigest.getInstance("SHA-256");
        byte[] digest2 = digest.digest(input);
        System.out.println("archivo: "+archivo);
        //show the input and output
        //System.out.println("Input (hex): " +
        //    new String(Hex.encode(input)));
        System.out.println("Output (hex): " +
           new String(Hex.encode(digest2)));
        
        return new String(Hex.encode(digest2));
    }
}
