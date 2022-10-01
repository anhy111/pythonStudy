package day04;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JTextField;
import javax.swing.JButton;
import javax.swing.JTextArea;
import javax.swing.SwingConstants;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.util.Random;

public class mySwing10 extends JFrame {

	private JPanel contentPane;
	private JTextField tf;
	String com = "123";
	JTextArea ta;
	private JButton btnReset;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					mySwing10 frame = new mySwing10();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the frame.
	 */
	public mySwing10() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 324, 438);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lbl = new JLabel("세자리수");
		lbl.setBounds(58, 40, 54, 15);
		contentPane.add(lbl);
		
		tf = new JTextField();
		tf.setHorizontalAlignment(SwingConstants.CENTER);
		tf.setBounds(134, 37, 116, 21);
		contentPane.add(tf);
		tf.setColumns(10);
		
		JButton btn = new JButton("맞추기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myclick();
			}
		});
		btn.setBounds(58, 80, 116, 23);
		contentPane.add(btn);
		
		ta = new JTextArea();
		ta.setBounds(58, 129, 192, 240);
		contentPane.add(ta);
		
		btnReset = new JButton("리셋");
		btnReset.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myReset();
			}
		});
		btnReset.setBounds(175, 80, 85, 23);
		contentPane.add(btnReset);
		
		setCom();
	}
	
	public void myReset() {
		ta.setText("");
		tf.setText("");
		setCom();
	}
	
	public void setCom() {
		int[] arr10 = new int[]{0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
		
		for(int i=0; i<100; i++) {
			int ran = new Random().nextInt(10);
			
			int a = arr10[0];
			int b = arr10[ran];
			
			arr10[ran] = a;
			arr10[0] = b;
		}
		
		com = "" + arr10[0] + arr10[1] + arr10[2];
		System.out.println("com:" + com);
	}
	
	public int getStrike(String com, String mine) {
//		int strike = 0;
//		for(int i=0; i<com.length(); i++) {
//			if(com.charAt(i) == mine.charAt(i)) {
//				strike++;
//			}
//		}
		
		int cnt = 0;
		String c1 = com.substring(0,1);
		String c2 = com.substring(1,2);
		String c3 = com.substring(2,3);
		
		String m1 = mine.substring(0,1);
		String m2 = mine.substring(1,2);
		String m3 = mine.substring(2,3);
		
		if(c1.equals(m1)) cnt++;
		if(c2.equals(m2)) cnt++;
		if(c3.equals(m3)) cnt++;
		
		
		return cnt;
	}
	
	public int getBall(String com, String mine) {
//		int ball = 0;
//		
//		for(int i=0; i<com.length(); i++){
//			for(int j=0; j<mine.length(); j++) {
//				if(com.charAt(i) == mine.charAt(j) && i != j) {
//					ball++;
//					break;
//				}
//			}
//		}
		
		int cnt = 0;
		String c1 = com.substring(0,1);
		String c2 = com.substring(1,2);
		String c3 = com.substring(2,3);
		
		String m1 = mine.substring(0,1);
		String m2 = mine.substring(1,2);
		String m3 = mine.substring(2,3);
		
		if(c1.equals(m2) || c1.equals(m3)) cnt++;
		if(c2.equals(m1) || c2.equals(m3)) cnt++;
		if(c3.equals(m1) || c3.equals(m2)) cnt++;
		
		return cnt;
	}
	
	public void myclick() {
		String str_old = ta.getText();
		
		String mine = tf.getText();
		int s = getStrike(com, mine);
		int b = getBall(com, mine);
		
		String str_new = mine + " " + s +"S " + b + "B\n";
		
		ta.setText(str_old + str_new);
		tf.setText("");
		
		if(s == 3) {
			JOptionPane.showMessageDialog(null, mine + "을 맞췄습니다.");;
		}
	}
	
	
	
	
}
























