package com.mycompany.app;

import com.mycompany.app.MasterSeed;

public class App 
{
    public static void main( String[] args )throws InterruptedException
    {
		MasterSeed ms;
		
		for(int i=0; i < 10000; i++){
			System.out.println( "Hello World! Loop: " + i);
			Thread.sleep(10000);
		}
    }
}
