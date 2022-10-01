package day04;

import java.awt.EventQueue;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JTextField;
import javax.swing.JButton;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class mySwing04 extends JFrame {

	private JPanel contentPane;
	private JTextField tf01;
	private JTextField tf02;
	private JTextField tf03;
	private JTextField tf04;
	private JTextField tf05;
	private JTextField tf06;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					mySwing04 frame = new mySwing04();
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
	public mySwing04() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		tf01 = new JTextField();
		tf01.setBounds(70, 32, 36, 21);
		contentPane.add(tf01);
		tf01.setColumns(10);
		
		tf02 = new JTextField();
		tf02.setColumns(10);
		tf02.setBounds(118, 32, 36, 21);
		contentPane.add(tf02);
		
		tf03 = new JTextField();
		tf03.setColumns(10);
		tf03.setBounds(166, 32, 36, 21);
		contentPane.add(tf03);
		
		tf04 = new JTextField();
		tf04.setColumns(10);
		tf04.setBounds(214, 32, 36, 21);
		contentPane.add(tf04);
		
		tf05 = new JTextField();
		tf05.setColumns(10);
		tf05.setBounds(262, 32, 36, 21);
		contentPane.add(tf05);
		
		tf06 = new JTextField();
		tf06.setColumns(10);
		tf06.setBounds(310, 32, 36, 21);
		contentPane.add(tf06);
		
		JButton btn = new JButton("로또 생성하기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				mylotto();
			}
		});
		btn.setBounds(70, 85, 276, 35);
		contentPane.add(btn);
	}
	public void mylotto() {
		int maxNum = 45;
		
		List<Integer> list = new ArrayList<Integer>();
		
		for(int i=1; i<=maxNum; i++) { 	list.add(i);  }
		
		for(int i=0; i<100; i++) {
			int ran = new Random().nextInt(maxNum);
			
			int temp = list.get(ran);
		    list.add(ran,list.get(0));
		    list.add(0,temp);
		}
		
		tf01.setText(list.get(0)+"");
		tf02.setText(list.get(1)+"");
		tf03.setText(list.get(2)+"");
		tf04.setText(list.get(3)+"");
		tf05.setText(list.get(4)+"");
		tf06.setText(list.get(5)+"");
		
//		int[] list = new int[maxNum];
//		
//		for(int i=1; i<=maxNum; i++) { 	list[i-1] = i;  }
//		
//		for(int i=0; i<100; i++) {
//			int ran = new Random().nextInt(maxNum);
//			
//			int temp = list[ran];
//		    list[ran] = list[0];
//		    list[0] = temp;
//		}
//		
//		
//		tf01.setText(list[0]+"");
//		tf02.setText(list[1]+"");
//		tf03.setText(list[2]+"");
//		tf04.setText(list[3]+"");
//		tf05.setText(list[4]+"");
//		tf06.setText(list[5]+"");
		
	}
}
