package com.example.gymtracker;

import android.content.ContentValues;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

import java.text.SimpleDateFormat;
import java.util.Calendar;

public class MainActivity extends AppCompatActivity {

    TextView tv_ppe;
    Button btn_log, btn_reset;
    DatabaseHelper mydb;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        btn_reset = findViewById(R.id.btn_reset);
        btn_reset.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                reset();
            }
        });
        btn_log = findViewById(R.id.btn_log);
        btn_log.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                logWorkout();
            }
        });
        tv_ppe = findViewById(R.id.tv_ppe);

        mydb = new DatabaseHelper(getApplicationContext());
//        mydb.dropTable();
//        mydb.createTable();
        refresh();
    }

    public void reset() {

//        mydb.dropTable();

        mydb.deleteAllData();
        refresh();

    }

    public void logWorkout() {

        //get current date > convert to string as per format > print
        Calendar now = Calendar.getInstance();
        String pattern = "ddMMyy";
        SimpleDateFormat format = new SimpleDateFormat(pattern);
        String nowStr = format.format(now.getTime());
        System.out.println("Today's date: "+ nowStr);

        //get latest date (row) from db
        Cursor res = mydb.getLatestData();
        res.moveToFirst();
        if(res.getCount() != 0) {
            //if there are rows, print latest date
            System.out.println("Date from db: " + res.getString(0));
            //if latest row and today's date is different, insert the row
            if (!res.getString(0).equals(nowStr)) {
                System.out.println("Dates are not equal, db: " + res.getString(0) + " nowStr: " + nowStr);
                boolean isInserted = mydb.insertData(nowStr);
                if (!isInserted)
                    Toast.makeText(getApplicationContext(),"Error logging workout",Toast.LENGTH_LONG);
                refresh();
            }
            System.out.println("Dates are equal, row not added");
        }
        else {
            //if db is empty, insert a row
            System.out.println("db is empty, row inserted for " + nowStr);
            boolean isInserted = mydb.insertData(nowStr);
            if (!isInserted)
                Toast.makeText(getApplicationContext(), "Error logging workout", Toast.LENGTH_LONG);
            refresh();
        }
    }

    public void refresh() {
        int count;
        double ppe, countDouble;
        Cursor res = mydb.getAllData();

        count = res.getCount();
        countDouble = count;
        if(count == 0) {
            Toast.makeText(getApplicationContext(), "No workouts logged", Toast.LENGTH_LONG);
            tv_ppe.setText("No workouts logged");
            return;
        }

        ppe = 30 / countDouble;
        tv_ppe.setText(String.valueOf(ppe));
    }
}
