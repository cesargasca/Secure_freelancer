package FirmaDigital;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.security.Security;

import org.bouncycastle.crypto.AsymmetricBlockCipher;
import org.bouncycastle.crypto.engines.RSAEngine;
import org.bouncycastle.crypto.params.AsymmetricKeyParameter;
import org.bouncycastle.crypto.util.PrivateKeyFactory;
import org.bouncycastle.crypto.util.PublicKeyFactory;

import sun.misc.BASE64Decoder;

public class RSADecryptFile {
    /*
    public static void main(String[] args)
    {

        String privateKeyFilename = null;
        String encryptedFilename = null;
        String outputFilename = null;

        RSADecryptFile rsaDecryptFile = new RSADecryptFile();

        privateKeyFilename = "public.txt";
        //privateKeyFilename = "private.txt";

        encryptedFilename = "encriptado.txt";
        outputFilename = "desencriptado.txt";
        rsaDecryptFile.decrypt(privateKeyFilename, encryptedFilename, outputFilename);

    }*/

    public String getDecrypted(String publicKeyr,String encrypted){
        String value = "";
         try {

            Security.addProvider(new org.bouncycastle.jce.provider.BouncyCastleProvider());

            String key = publicKeyr;
             System.out.println("llave publica: "+key);
            BASE64Decoder b64 = new BASE64Decoder();
            AsymmetricKeyParameter publicKey = 
                (AsymmetricKeyParameter) PublicKeyFactory.createKey(b64.decodeBuffer(key));
            AsymmetricBlockCipher e = new RSAEngine();
            e = new org.bouncycastle.crypto.encodings.PKCS1Encoding(e);
            e.init(false, publicKey);

            
            byte[] messageBytes = hexStringToByteArray(encrypted);

            int i = 0;
            int len = e.getInputBlockSize();
            while (i < messageBytes.length)
            {
                if (i + len > messageBytes.length)
                    len = messageBytes.length - i;

                byte[] hexEncodedCipher = e.processBlock(messageBytes, i, len);
                value = value + new String(hexEncodedCipher);
                i += e.getInputBlockSize();
            }


            System.out.println("decrypted: "+value);


        }
        catch (Exception e) {
            System.out.println(e);
        }
         
        return value;
    }
    /*
    private void decrypt (String privateKeyFilename, String encryptedFilename, String outputFilename){

        try {

            Security.addProvider(new org.bouncycastle.jce.provider.BouncyCastleProvider());

            String value = "";
            String key = readFileAsString(privateKeyFilename);
            BASE64Decoder b64 = new BASE64Decoder();
            AsymmetricKeyParameter privateKey = 
                (AsymmetricKeyParameter) PublicKeyFactory.createKey(b64.decodeBuffer(key));
            AsymmetricBlockCipher e = new RSAEngine();
            e = new org.bouncycastle.crypto.encodings.PKCS1Encoding(e);
            e.init(false, privateKey);

            String inputdata = readFileAsString(encryptedFilename);
            byte[] messageBytes = hexStringToByteArray(inputdata);

            int i = 0;
            int len = e.getInputBlockSize();
            while (i < messageBytes.length)
            {
                if (i + len > messageBytes.length)
                    len = messageBytes.length - i;

                byte[] hexEncodedCipher = e.processBlock(messageBytes, i, len);
                value = value + new String(hexEncodedCipher);
                i += e.getInputBlockSize();
            }


            System.out.println(value);

            BufferedWriter out = new BufferedWriter(new FileWriter(outputFilename));
            out.write(value);
            out.close();


        }
        catch (Exception e) {
            System.out.println(e);
        }
    }
    */
    public static String getHexString(byte[] b) throws Exception {
        String result = "";
        for (int i=0; i < b.length; i++) {
            result +=
                Integer.toString( ( b[i] & 0xff ) + 0x100, 16).substring( 1 );
        }
        return result;
    }

    public static byte[] hexStringToByteArray(String s) {
        int len = s.length();
        byte[] data = new byte[len / 2];
        for (int i = 0; i < len; i += 2) {
            data[i / 2] = (byte) ((Character.digit(s.charAt(i), 16) << 4)
                    + Character.digit(s.charAt(i+1), 16));
        }
        return data;
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