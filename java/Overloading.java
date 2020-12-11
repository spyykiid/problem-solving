public class Overloading{

	public void calMethod(String x){
		System.out.println(x+" double method");
	}
	// public void calMethod(long x){
	// 	System.out.println(x+" long method");	
	// }

	public static void main(String[] args){
		Overloading ol = new Overloading();
		double b = 1.0;
		ol.calMethod(b);
	}
}