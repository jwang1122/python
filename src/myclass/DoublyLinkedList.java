package com.rodney.myproject;

public class DoublyLinkedList {
	Node head; //
	Node tail; 

	public void add(Node node) {
		if(head==null) {
			this.head = node;
			this.tail = node;
		}else {
			node.setPrev(tail);
			tail.setNext(node);
			tail = node;
			node.setNext(null);
		}
	}

	Node previous(Node node) {
		return node.getPrev();
	}
	
	Node next(Node node) {
		return node.getNext();
	}
	
	public void insert(Node node, Node newNode) {
		newNode.setPrev(node);
		newNode.setNext(node.getNext());
		newNode.getNext().setPrev(newNode);
		node.setNext(newNode);
	}
	
	@Override
	public String toString() {
		StringBuffer result = new StringBuffer(); // StringBuilder()
		Node current = head;
		while (current.getNext()!=null) {
			result.append(current.getData()+", ");
			current = current.getNext(); // feature of linked list 
		}
		result.append(current.getData());
		return result.toString();
	}
	
	public static void main(String[] args) {
		Node<Person> node = new Node<Person>(new Teacher("John"));
		DoublyLinkedList list = new DoublyLinkedList();
		list.add(node);
		node = new Node(new Teacher("Rodney"));
		list.add(node);
		Node node1 = new Node(new Teacher("Marco"));
		list.add(node1);
		
		list.insert(node, new Node(new Teacher("Charles"))); // John, Charles, Rodney
		
		System.out.println(list);
	}

}
