import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.lang.*;
import java.util.regex.*;
import java.util.concurrent.*;

public class Solution {
    
    public static void main(String args[]) throws Exception
    {
        BufferedReader br = null;
        FileReader fr = null;
        ExecutorService executor = (ThreadPoolExecutor) Executors.newFixedThreadPool(10);

        try
        {
            fr = new FileReader(args[1]);
            br = new BufferedReader(fr);

            String lineA, lineB;
            String rTypeA, rTypeB;
            String[] prevFields = null, fieldsA, fieldsB;

            while ((lineA = br.readLine()) != null) {
                fieldsA = Parser.parse(lineA);
                rTypeA = fieldsA[0];

                if( prevFields == null && (lineB = br.readLine()) != null)
                {
                    fieldsB = Parser.parse(lineB);
                    rTypeB = fieldsB[0];
                }else{   
                    fieldsB = fieldsA;
                    fieldsA = prevFields;
                    rTypeA = fieldsA[0];
                    rTypeB = fieldsB[0];
                }

                if(rTypeA == "06" && rTypeB == "07"){
                    // create a model and excute the worker
                    SDR sdr = new SDR(fieldsB[0], fieldsB[1], fieldsB[2], fieldsB[3]);
                    DTR dtr = new DTR(fieldsA[0], fieldsA[1], fieldsA[2], fieldsA[3], fieldsA[4], fieldsA[5], sdr);
                    Runnable worker = new WorkerThread(dtr);
                    executor.execute(worker);
                    prevFields = null;

                }else if(rTypeA == "06" && rTypeB == "06"){
                    // create a new model with DTR and excute the worker
                    DTR dtr = new DTR(fieldsA[0], fieldsA[1], fieldsA[2], fieldsA[3], fieldsA[4], fieldsA[5], null);
                    Runnable worker = new WorkerThread(dtr);
                    executor.execute(worker);

                    prevFields = fieldsB;
                }else if(rTypeA == "06"){
                    DTR dtr = new DTR(fieldsA[0], fieldsA[1], fieldsA[2], fieldsA[3], fieldsA[4], fieldsA[5], null);
                    Runnable worker = new WorkerThread(dtr);
                    executor.execute(worker);
                }
            }

            executor.shutdown();
        } catch (IOException e) {

            e.printStackTrace();

        } finally {

            try
            {
                if (br != null)
                    br.close();

                if (fr != null)
                    fr.close();

            } catch (IOException ex) {

                ex.printStackTrace();

            }

        }
    }
}


class WorkerThread implements Runnable {

    private DTR model;

    public WorkerThread(DTR model){
        this.model = model;
    }

    @Override
    public void run() {
        Response response = TransactionProcessor.process(this.model);
        System.out.println( this.model.getCardNumber() +" "+ this.model.getMerchantCode() +" "+ this.model.getAmount() +" " + response.getStatus());
    }
}


class SDR
{
    private int recordType;
    private int transactionCode;
    private String cardNumber;
    private String descriptiom;


    public SDR(String recordType, String transactionCode, String cardNumber, String descriptiom) {
        this.setRecordType(Integer.parseInt(recordType));
        this.setTransactionCode(Integer.parseInt(transactionCode));
        this.setCardNumber(cardNumber);
        this.setDescriptiom(descriptiom);
    }

    public int getRecordType() {
        return this.recordType;
    }

    public void setRecordType(int recordType) {
        this.recordType = recordType;
    }

    public int getTransactionCode() {
        return this.transactionCode;
    }

    public void setTransactionCode(int transactionCode) {
        this.transactionCode = transactionCode;
    }

    public String getCardNumber() {
        return this.cardNumber;
    }

    public void setCardNumber(String cardNumber) {
        this.cardNumber = cardNumber;
    }

    public String getDescriptiom() {
        return this.descriptiom;
    }

    public void setDescriptiom(String descriptiom) {
        this.descriptiom = descriptiom;
    }
}

class DTR
{
  private int recordType;
  private int transactionCode;
  private String cardNumber;
  private int merchantCode;
  private double amount;
  private Date date;
  private SDR sdr;


    public DTR (String recordType, String transactionCode, String cardNumber,
                String merchantCode, String amount, String date, SDR sdr) throws ParseException
    {
        DateFormat format = new SimpleDateFormat("yyyymmdd");
        this.setRecordType(Integer.parseInt(recordType));
        this.setTransactionCode(Integer.parseInt(transactionCode));
        this.setCardNumber(cardNumber);
        this.setMerchantCode(Integer.parseInt(merchantCode));
        this.setAmount(Double.parseDouble(amount));
        this.setDate(format.parse(date));
        this.setSdr(sdr);
    }

    public int getRecordType() {
        return this.recordType;
    }

    public void setRecordType(int recordType) {
        this.recordType = recordType;
    }

    public int getTransactionCode() {
        return this.transactionCode;
    }

    public void setTransactionCode(int transactionCode) {
        this.transactionCode = transactionCode;
    }

    public String getCardNumber() {
        return this.cardNumber;
    }

    public void setCardNumber(String cardNumber) {
        this.cardNumber = cardNumber;
    }

    public int getMerchantCode() {
        return this.merchantCode;
    }

    public void setMerchantCode(int merchantCode) {
        this.merchantCode = merchantCode;
    }

    public double getAmount() {
        return this.amount;
    }

    public void setAmount(double amount) {
        this.amount = amount;
    }

    public Date getDate() {
        return this.date;
    }

    public void setDate(Date date) {
        this.date = date;
    }

    public SDR getSdr() {
        return this.sdr;
    }

    public void setSdr(SDR sdr) {
        this.sdr = sdr;
    }
}

class Response
{
    public String getStatus(){
        //return status of the txn
        return "";
    }
}

class TransactionProcessor
{
    public static Response process(DTR dtr)
    {
        // Processes a transaction from give DTR model.
        // Returns a response whether its a valid or failure of transaction.
        return new Response();
    }
}

class Parser
{
    public static String[] parse(String line){
        String[] fields = null;
        // process DTR or SDR and returns a list of fields. 
        return fields;
    }
}