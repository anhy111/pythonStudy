package day04;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JTextField;
import javax.swing.JLabel;
import javax.swing.JButton;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MySwing03 extends JFrame {

	private JPanel contentPane;
	private JTextField tf1;
	private JTextField tf2;
	private JTextField tf3;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing03 frame = new MySwing03();
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
	public MySwing03() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		tf1 = new JTextField();
		tf1.setBounds(12, 30, 50, 21);
		contentPane.add(tf1);
		tf1.setColumns(10);
		
		tf2 = new JTextField();
		tf2.setBounds(107, 30, 50, 21);
		contentPane.add(tf2);
		tf2.setColumns(10);
		
		JLabel lblNewLabel = new JLabel("+");
		lblNewLabel.setBounds(77, 33, 18, 15);
		contentPane.add(lblNewLabel);
		
		JButton btn = new JButton("=");
		
		btn.setBounds(185, 29, 97, 23);
		contentPane.add(btn);
		
		tf3 = new JTextField();
		tf3.setBounds(294, 30, 58, 21);
		contentPane.add(tf3);
		tf3.setColumns(10);
		
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myclick();
			}
		});
	}
	
	public void myclick() {
		int a = Integer.valueOf(tf1.getText());
		int b = Integer.valueOf(tf2.getText());
		
		tf3.setText(String.valueOf(a + b));
	}
	
}
