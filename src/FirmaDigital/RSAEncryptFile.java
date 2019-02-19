package FirmaDigital;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.security.Security;

import org.bouncycastle.crypto.AsymmetricBlockCipher;
import org.bouncycastle.crypto.engines.RSAEngine;
import org.bouncycastle.crypto.params.AsymmetricKeyParameter;
import org.bouncycastle.crypto.util.PublicKeyFactory;
import org.bouncycastle.crypto.util.PrivateKeyFactory;


import sun.misc.BASE64Decoder;

public class RSAEncryptFile {
    /*
    public static void main(String[] args)
    {

        String publicKeyFilename = null;
        String inputFilename = null;
        String encryptedFilename = null;

        RSAEncryptFile rsaEncryptFile = new RSAEncryptFile();

        //publicKeyFilename = "public.txt";
        publicKeyFilename = "private.txt";
        inputFilename = "hash.txt";
        encryptedFilename = "encriptado.txt";
        rsaEncryptFile.encrypt(publicKeyFilename, inputFilename, encryptedFilename);

    }*/
    
    public String getEncrypted(String privateKeyFilename,String mensaje){
        String value = "";
         try {

            Security.addProvider(new org.bouncycastle.jce.provider.BouncyCastleProvider());

            
            String key = readFileAsString(privateKeyFilename);
            BASE64Decoder b64 = new BASE64Decoder();
            AsymmetricKeyParameter privateKey = 
                (AsymmetricKeyParameter) PrivateKeyFactory.createKey(b64.decodeBuffer(key));
            AsymmetricBlockCipher e = new RSAEngine();
            e = new org.bouncycastle.crypto.encodings.PKCS1Encoding(e);
            e.init(true, privateKey);
            //e.init(true, publicKey);


            
            byte[] messageBytes = mensaje.getBytes();
            int i = 0;
            int len = e.getInputBlockSize();
            while (i < messageBytes.length)
            {
                if (i + len > messageBytes.length)
                    len = messageBytes.length - i;

                byte[] hexEncodedCipher = e.processBlock(messageBytes, i, len);
                value = value + getHexString(hexEncodedCipher);
                i += e.getInputBlockSize();
            }
            //System.out.println("encrypted: "+value);  
        }
        catch (Exception e) {
            System.out.println(e);
        }
        return value;
    }
    /*
    private void encrypt (String publicKeyFilename, String inputFilename, String encryptedFilename){

        try {

            Security.addProvider(new org.bouncycastle.jce.provider.BouncyCastleProvider());

            String value = "";
            String key = readFileAsString(publicKeyFilename);
            BASE64Decoder b64 = new BASE64Decoder();
            AsymmetricKeyParameter publicKey = 
                (AsymmetricKeyParameter) PrivateKeyFactory.createKey(b64.decodeBuffer(key));
            AsymmetricBlockCipher e = new RSAEngine();
            e = new org.bouncycastle.crypto.encodings.PKCS1Encoding(e);
            e.init(true, publicKey);
            //e.init(true, publicKey);


            String inputdata = readFileAsString(inputFilename);
            byte[] messageBytes = inputdata.getBytes();
            int i = 0;
            int len = e.getInputBlockSize();
            while (i < messageBytes.length)
            {
                if (i + len > messageBytes.length)
                    len = messageBytes.length - i;

                byte[] hexEncodedCipher = e.processBlock(messageBytes, i, len);
                value = value + getHexString(hexEncodedCipher);
                i += e.getInputBlockSize();
            }

            System.out.println(value);
            BufferedWriter out = new BufferedWriter(new FileWriter(encryptedFilename));
            out.write(value);
            out.close();
           
        }
        catch (Exception e) {
            System.out.println(e);
        }
    }*/

    public static String getHexString(byte[] b) throws Exception {
        String result = "";
        for (int i=0; i < b.length; i++) {
            result +=
                Integer.toString( ( b[i] & 0xff ) + 0x100, 16).substring( 1 );
        }
        return result;
    }
    
    private static String readFileAsString(String filePath)
    throws java.io.IOException{
        StringBuffer fileData = new StringBuffer(1000);
        BufferedReader reader = new BufferedReader(
                new FileReader(filePath));
        char[] buf = new char[1024];
        int numRead=0;
        while((numRead=reader.read(buf)) != -1){
            String readData = String.valueOf(buf, 0, numRead);
            fileData.append(readData);
            buf = new char[1024];
        }
        reader.close();
        System.out.println(fileData.toString());
        return fileData.toString();
    }

}