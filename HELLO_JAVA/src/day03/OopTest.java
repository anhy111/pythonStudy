package day03;

public class OopTest {
	public static void main(String[] args) {
		Human hum = new Human();
		System.out.println();
		System.out.println(hum.hungry);
		System.out.println(hum.skill_lang);
		
		hum.timegoby();
		hum.momstouch(5);
		System.out.println(hum.hungry);
		System.out.println(hum.skill_lang);
	}
}
