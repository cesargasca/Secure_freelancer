/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

package FirmaDigital;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.swing.JOptionPane;

/**
 *
 * @author hidal
 */
public class MySQL {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) throws Exception {
        MySQL db = new MySQL();
        db.MySQLConnection("root", "Alansdfs0", "crypto");
        //System.out.println(db.getPublicKey("HICA9707"));
        //System.out.println(db.getDigitalSignature("HICA9707"));

        db.closeConnection();
    }
    


private static Connection Conexion;
    
    public void MySQLConnection(String user, String pass, String db_name) throws Exception {
        try {
            Class.forName("com.mysql.jdbc.Driver");
            Conexion = DriverManager.getConnection("jdbc:mysql://localhost:3306/" + db_name, user, pass);
            //JOptionPane.showMessageDialog(null, "Se ha iniciado la conexión con el servidor de forma exitosa");
        } catch (ClassNotFoundException ex) {
            Logger.getLogger(MySQL.class.getName()).log(Level.SEVERE, null, ex);
        } catch (SQLException ex) {
            Logger.getLogger(MySQL.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
    

    public void getValues(String table_name) {
        try {
            String Query = "SELECT FROM " + table_name;
            Statement st = Conexion.createStatement();
            java.sql.ResultSet resultSet;
            resultSet = st.executeQuery(Query);
 
            while (resultSet.next()) {
                System.out.println("key: " + resultSet.getString("key"));
            }
 
        } catch (SQLException ex) {
            //JOptionPane.showMessageDialog(null, "Error en la adquisición de datos");
        }
    }
    
    public String getDigitalSignature(String CURP){
        String firma="";
        try {
            String Query = "SELECT * FROM digitalsignature WHERE CURP = '"+CURP+"'";
            System.out.println(Query);
            Statement st = Conexion.createStatement();
            java.sql.ResultSet resultSet;
            resultSet = st.executeQuery(Query);
 
            while (resultSet.next()) {
               firma= resultSet.getString("DigitalSignature");
                
            }
        } catch (SQLException ex) {
           // JOptionPane.showMessageDialog(null, "Error en la adquisición de datos");
        }
        return firma;
    }
    
     public String getPublicKey(String CURP){
        String publicKey="";
        try {
            String Query = "SELECT * FROM public_key WHERE CURP = '"+CURP+"'";
            Statement st = Conexion.createStatement();
            java.sql.ResultSet resultSet;
            resultSet = st.executeQuery(Query);
            
           while (resultSet.next()) {
               publicKey= resultSet.getString("key");
                
            }
        } catch (SQLException ex) {
           // JOptionPane.showMessageDialog(null, "Error en la adquisición de datos");
        }
        return publicKey;
    }
    
    
    public void closeConnection() {
        try {
            Conexion.close();
            System.out.println("Se ha finalizado la conexión con el servidor");
        } catch (SQLException ex) {
            Logger.getLogger(MySQL.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
    
    public void insertData(String table_name, String CURP, String Nombre,String ApellidoP,String ApellidoM,String key,String expira) {
        try {
            java.util.Date d = new java.util.Date();  
            java.sql.Date date2 = new java.sql.Date(d.getTime());
            String Query = "INSERT INTO " + table_name + " VALUES("
                    + "\"" + CURP + "\", "
                    + "\"" + Nombre + "\","
                    + "\"" + ApellidoP + "\","
                    + "\"" + ApellidoM + "\","
                    + "\"" + key + "\","
                    + "\"" + date2 + "\")";
            Statement st = Conexion.createStatement();
            st.executeUpdate(Query);
            //JOptionPane.showMessageDialog(null, "Datos almacenados de forma exitosa");
        } catch (SQLException ex) {
            JOptionPane.showMessageDialog(null, "Error en el almacenamiento de datos");
        }
    }
    
        public void insertData2(String table_name, String CURP, String DigitalSignature) {
        try {
            java.util.Date d = new java.util.Date();  
            java.sql.Date date2 = new java.sql.Date(d.getTime());
            String Query = "INSERT INTO " + table_name + " VALUES("
                    + "\"" + CURP + "\", "
                    + "\"" + DigitalSignature + "\")";
            Statement st = Conexion.createStatement();
            st.executeUpdate(Query);
            //JOptionPane.showMessageDialog(null, "Datos almacenados de forma exitosa");
        } catch (SQLException ex) {
            JOptionPane.showMessageDialog(null, "Error en el almacenamiento de datos");
        }
    }
}

