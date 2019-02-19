/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package MAC;

import static MAC.Verify.escribe;
import java.io.IOException;
import java.security.InvalidKeyException;
import java.security.NoSuchAlgorithmException;
import javax.crypto.KeyGenerator;
import javax.crypto.Mac;
import javax.crypto.SecretKey;
import org.bouncycastle.util.encoders.Base64;

/**
 *
 * @author cesargasca
 */
public class MacGenerator {
    public static void SaveKey(SecretKey SHAkey,String nameOfFile){
         String key = new String(Base64.encode(SHAkey.getEncoded()));
         escribe(concatenateForKey(nameOfFile),key);
    }
    
    public static SecretKey generateKey() throws NoSuchAlgorithmException{
        KeyGenerator keyGen = KeyGenerator.getInstance("HmacSHA256");
        SecretKey SHAkey = keyGen.generateKey();
         return SHAkey;
    }
    
    public static String createTag(String nameOfFile) throws NoSuchAlgorithmException, IOException, InvalidKeyException{
        String program = Verify.lee(nameOfFile);
        Mac mac = Mac.getInstance("HmacSHA256");
        SecretKey key = generateKey();
        SaveKey(key,nameOfFile);
        mac.init(key);
        mac.update(program.getBytes("UTF8"));
        String tag = new String(Base64.encode(mac.doFinal()));
        saveTag(tag,nameOfFile);
        return tag;
    }
    
    public static String concatenateForKey(String nameOfFile){
        int index = 0;
        for(int i = 0 ; i < nameOfFile.length() ; i++){
            if (nameOfFile.charAt(i) == '.'){
                index = i - 1;
                break;
            }   
        }
        String result = nameOfFile.substring(0,index) + "_key.txt";
        System.out.println(result);
        return result;
    }
    
    public static String concatenateForClient(String nameOfFile){
        int index = 0;
        for(int i = 0 ; i < nameOfFile.length() ; i++){
            if (nameOfFile.charAt(i) == '.'){
                index = i - 1;
                break;
            }   
        }
        String result = nameOfFile.substring(0,index) + "_client" + nameOfFile.substring(index, nameOfFile.length());
        System.out.println(result);
        return result;
    }
    
    public static void saveTag(String tag, String nameOfFile) throws IOException{
        String program = Verify.lee(nameOfFile);
         String result = "//" + tag + "\n" + program;
         escribe(concatenateForClient(nameOfFile),result);
    }
}
