package com.upgrad.phonebook;

//public class PhoneBook {
//
//	public static void main(String[] args) {
//		// TODO Auto-generated method stub
//
//	}
//
//}


import java.util.*;

class Record {    
	String name;  
	long number; 
	int ID;
}

class AddressBook {
	Record[] list;
	
	//declare 'list' as an array in the constructor, remember to declare a big enough array to store all possible IDs
	
	public AddressBook() {
		list = new Record [1000];
	}

	
	public void add(String name, long number, int ID) {
		//Wrap all the details into an object of class Record and add it to the list at the correct index
		// Print: 'Successfully added: contact_name', where contact_name is the name of the contact added
		
		Record r = new Record();
		r.name = name;
		r.number = number;
		r.ID = ID;
		
		list[ID] = r;
		
		System.out.println("Successfully added: " + name);
	}
	public void findByID(int ID) {
		//Check if the ID exists
		//If it doesn't, print: 'No such ID exists'      
		//else Print: 'Name: contact_name Number: contact_number', where contact_name and contact_number are the details of the contact having that ID
		
		if (list[ID] == null) {
			System.out.println("No such ID exists");
			return;
		}
		
		System.out.println("Name: " + list[ID].name + " Number: " + list[ID].number);
	}
	
	public void delete(int ID) {
		//Check if the ID exists
		//If it doesn't, print: 'No such ID exists'      
		//else delete the item in the list having the given ID
		//Print: 'Successfully deleted: contact_name', where contact_name is the name of the contact to be deleted
		
		if (list[ID] == null) {
			System.out.println("No such ID exists");
			return;
		}
		
		System.out.println("Successfully added: " + list[ID].name);
		
		list[ID] = null;
		
	}
	public void printAddressBook() {
		System.out.println("List of contacts:"); 
		// Print the details of all the contacts in the list in the following format:
		//Name: ABC ID: 876 Number: 123456789
		//Note that the above is just an example	      
		
		for (int i=100; i<list.length; i++) {
			if (list[i] == null) continue;
			
			System.out.println("Name: " + list[i].name + " ID: " + list[i].ID + " Number: " + list[i].number);
		}
	}
	
}  

public class PhoneBook {  
	public static void main(String[] args) {  
		AddressBook myContacts = new AddressBook();
	    myContacts.add("John", 9876123450l, 101);
	    myContacts.add("Mellisa", 8360789114l, 560);
	    myContacts.add("Daman",9494149900l, 444);
	    myContacts.findByID(999);
	    myContacts.printAddressBook();
	    myContacts.delete(101);
	    myContacts.add("Gregory",7289880988l, 980);
	    myContacts.printAddressBook();
	    myContacts.findByID(560);
	    myContacts.add("Mary",7205678901l, 670);
	    myContacts.delete(101);
	    myContacts.findByID(670);
	    myContacts.printAddressBook();      
	}  
}