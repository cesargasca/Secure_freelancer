
/*import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.io.UnsupportedEncodingException;
import java.security.*;
import java.util.Arrays;
import java.util.Base64;
import java.util.Scanner;
import javax.crypto.*;
//
// Generate a Message Authentication Code
public class MessageAuthenticationCode {
    private String original;
    private String test;
    private String tag;
    private SecretKey key;
    
    public MessageAuthenticationCode(String original, String test) throws NoSuchAlgorithmException{
        this.original= original;
        this.test = test;
        KeyGenerator keyGen = KeyGenerator.getInstance("HmacSHA256");
        this.key = generateRandomKey();
    } 
    
     public MessageAuthenticationCode(String original, String tag, SecretKey k) throws NoSuchAlgorithmException{
        this.original= original;
        this.tag = tag;
        KeyGenerator keyGen = KeyGenerator.getInstance("HmacSHA256");
        this.key = generateRandomKey();
    } 
    
    public static SecretKey generateRandomKey() throws NoSuchAlgorithmException{
        KeyGenerator keyGen = KeyGenerator.getInstance("HmacSHA256");
        SecretKey newkey = keyGen.generateKey();
        return newkey; //genera random key para HmacSHA256
    }
  public static byte[] recuperaLLave() throws IOException{
            Scanner r = new Scanner(System.in);
            String nameFile =  r.nextLine();
            
            return llave;
        }
  
    public MessageAuthenticationCode(String nameOfFile) throws NoSuchAlgorithmException, InvalidKeyException, UnsupportedEncodingException, IOException{
        this.original = nameOfFile;
        this.key = generateRandomKey();
        Mac mac = Mac.getInstance("HmacSHA256");
        mac.init(this.key);
        String program = lee(nameOfFile);
        mac.update(program.getBytes("UTF8")); 
        this.tag = Base64.getEncoder().encodeToString(mac.doFinal()); //tag base64
        escribe("/home/cesargasca/Desktop/crypto/key.txt",Base64.getEncoder().encodeToString(key.getEncoded()));
    }
    
    public boolean verifyMAC() throws IOException{
        String program = lee(original);
        String client_program = leeTag(test);
        client_program = client_program.replaceAll("(?m)^[ \t]*\r?\n", "");
        
        String tag2 = Base64.getEncoder().encodeToString(mac2.doFinal());
        
    }
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
    
  public static void main (String[] args) throws Exception {
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
    pruebaTRUE = pruebaTRUE.replaceAll("(?m)^[ \t]*\r?\n", "");
   // System.out.println("Verify");
    Mac mac2 = Mac.getInstance("HmacSHA256");
    mac2.init(SHAkey);
    mac2.update((pruebaTRUE).getBytes("UTF8"));
    String tag2 = Base64.getEncoder().encodeToString(mac2.doFinal());
      System.out.println("TAGS\n" + tag + "\n" + tag2);
    System.out.println(tag2.equals(tag));
  }
}*/