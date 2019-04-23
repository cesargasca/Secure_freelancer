package MAC;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.io.UnsupportedEncodingException;
import java.security.*;
import java.util.Arrays;
import org.bouncycastle.util.encoders.Base64;
import java.util.Scanner;
import javax.crypto.*;
import javax.crypto.spec.SecretKeySpec;
//
// Generate a Message Authentication Code
public class Verify{
    public static String leeTag(String nameofFile){
            File archivo = null;
            FileReader fr = null;
            BufferedReader br = null;
            String texto = "";
      try {
         archivo = new File (nameofFile);
         fr = new FileReader (archivo);
         br = new BufferedReader(fr);
         String linea;
         int i = 0;
         String tag = br.readLine();
           while((linea=br.readLine())!=null){
               //System.out.println(linea);
               if(linea.equals(new String("\n")))
                   System.out.println("---->" + linea);
               else{
                    texto += linea;
                    texto = texto.concat(new String("\n"));
               }
            }
         
      }
      catch(Exception e){
         e.printStackTrace();
      }finally{
         // En el finally cerramos el fichero, para asegurarnos
         // que se cierra tanto si todo va bien como si salta 
         // una excepcion.
         try{                    
            if( null != fr ){   
               fr.close();     
            }                  
         }catch (Exception e2){ 
            e2.printStackTrace();
         }
      }
      texto = texto.replaceAll("(?m)^[ \t]*\r?\n", "");
      return texto;
    }
    public static String lee(String nameofFile) throws IOException{
            File archivo = null;
            FileReader fr = null;
            BufferedReader br = null;
            String texto = "";
      try {
         archivo = new File (nameofFile);
         fr = new FileReader (archivo);
         br = new BufferedReader(fr);
         String linea;
           while((linea=br.readLine())!=null){
               //System.out.println(linea);
               if(linea.equals("\n")){
                   System.out.println("---->" + linea);
               }
               else{
               texto += linea;
               texto = texto.concat(new String("\n"));
               }
            }
         
      }
      catch(Exception e){
         e.printStackTrace();
      }finally{
         // En el finally cerramos el fichero, para asegurarnos
         // que se cierra tanto si todo va bien como si salta 
         // una excepcion.
         try{                    
            if( null != fr ){   
               fr.close();     
            }                  
         }catch (Exception e2){ 
            e2.printStackTrace();
         }
      }
      texto = texto.replaceAll("(?m)^[ \t]*\r?\n", "");
      return texto;
    }
    
    public static void escribe(String nameofFile, String mensaje){
        FileWriter fichero = null;
        PrintWriter pw = null;
        try
        {
            fichero = new FileWriter(nameofFile);
            pw = new PrintWriter(fichero);
                pw.println(mensaje);
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
           try {
           if (null != fichero)
              fichero.close();
           } catch (Exception e2) {
              e2.printStackTrace();
           }
        }
   }
    
     public static String generateMAC(String program,SecretKey k) throws NoSuchAlgorithmException, InvalidKeyException, UnsupportedEncodingException{
          Mac mac = Mac.getInstance("HmacSHA256");
           mac.init(k);
          mac.update(program.getBytes("UTF8"));
          String tag = new String(Base64.encode(mac.doFinal()));
          return tag;
     }
    public static boolean verify(String original,String test, String key) throws IOException, NoSuchAlgorithmException, InvalidKeyException{
        String o = lee(original);
        String t = leeTag(test);
        String n = lee(key);
        byte[] decodedKey = org.bouncycastle.util.encoders.Base64.decode(n);
        SecretKey originalKey = new SecretKeySpec(decodedKey, 0, decodedKey.length, "HmacSHA256");
        String tag1 = generateMAC(o,originalKey);
        String tag2 = generateMAC(t,originalKey);
        return tag1.equals(tag2);
    }
  /*public static void main (String[] args) throws Exception {
    //
    // check args and get plaintext
    String program =  lee("/home/cesargasca/Desktop/18-2/cryptography/proyecto_2/test/modulo.c");
    program = program.replaceAll("(?m)^[ \t]*\r?\n", "");
    String pruebaFALSE = lee("/home/cesargasca/Desktop/18-2/cryptography/proyecto_2/test/break.c");
    byte[] plainText = program.getBytes("UTF8");
    byte[] pruebaBytes = pruebaFALSE.getBytes("UTF8");
    //
    // get a key for the HmacMD5 algorithm
    System.out.println( "\nStart generating key" );
    KeyGenerator keyGen = KeyGenerator.getInstance("HmacSHA256");
    SecretKey SHAkey = keyGen.generateKey();
    System.out.println( "Finish generating key" );
      System.out.println(Base64.getEncoder().encodeToString(SHAkey.getEncoded()));
    //
    // get a MAC object and update it with the plaintext
    Mac mac = Mac.getInstance("HmacSHA256");
    mac.init(SHAkey);
    mac.update(plainText);
    //
    // print out the provider used and the MAC
    //System.out.println( "\n" + mac.getProvider().getInfo() );
    System.out.println( "\nMAC: " );
    
    String tag = Base64.getEncoder().encodeToString(mac.doFinal());
      System.out.println(tag);
    
    String mk = "//" + tag + "\n" + program;
    
    escribe("/home/cesargasca/Desktop/18-2/cryptography/proyecto_2/test/MACmodulo.c",mk);
    String pruebaTRUE = leeTag("/home/cesargasca/Desktop/18-2/cryptography/proyecto_2/test/MACmodulo.c");
    
   // System.out.println("Verify");
    Mac mac2 = Mac.getInstance("HmacSHA256");
    mac2.init(SHAkey);
    mac2.update((pruebaTRUE).getBytes("UTF8"));
    String tag2 = Base64.getEncoder().encodeToString(mac2.doFinal());
      System.out.println("TAGS\n" + tag + "\n" + tag2);
    System.out.println(tag2.equals(tag));
  }*/
}