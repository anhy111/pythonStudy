package day04;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JTextField;
import javax.swing.JButton;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import javax.swing.JOptionPane;

public class mySwing09 extends JFrame {

	private JPanel contentPane;
	private JTextField tf;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					mySwing09 frame = new mySwing09();
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
	public mySwing09() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 257, 305);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		tf = new JTextField();
		tf.setBounds(29, 24, 170, 21);
		tf.setHorizontalAlignment(JTextField.RIGHT);
		contentPane.add(tf);
		tf.setColumns(10);
		
		JButton btn1 = new JButton("1");
		
		btn1.setBounds(29, 72, 49, 23);
		contentPane.add(btn1);
		
		
		JButton btn2 = new JButton("2");
		
		btn2.setBounds(90, 72, 49, 23);
		contentPane.add(btn2);
		
		JButton btn3 = new JButton("3");
		
		btn3.setBounds(150, 72, 49, 23);
		contentPane.add(btn3);
		
		JButton btn4 = new JButton("4");
		
		btn4.setBounds(29, 105, 49, 23);
		contentPane.add(btn4);
		
		JButton btn5 = new JButton("5");
		
		btn5.setBounds(90, 105, 49, 23);
		contentPane.add(btn5);
		
		JButton btn6 = new JButton("6");
		btn6.setBounds(150, 105, 49, 23);
		contentPane.add(btn6);
		
		JButton btn8 = new JButton("8");
		btn8.setBounds(90, 138, 49, 23);
		contentPane.add(btn8);
		
		JButton btn7 = new JButton("7");
		btn7.setBounds(29, 138, 49, 23);
		contentPane.add(btn7);
		
		JButton btn9 = new JButton("9");
		btn9.setBounds(150, 138, 49, 23);
		contentPane.add(btn9);
		
		JButton btn0 = new JButton("0");
		btn0.setBounds(29, 171, 49, 23);
		contentPane.add(btn0);
		
		JButton btnCall = new JButton("CALL");
		btnCall.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myCall();
			}
		});
		btnCall.setBounds(90, 171, 109, 23);
		contentPane.add(btnCall);
		
		btn1.addMouseListener(new MouseAdapter() { @Override public void mouseClicked(MouseEvent e) {phoneNumber(e);} });
		btn2.addMouseListener(new MouseAdapter() { @Override public void mouseClicked(MouseEvent e) {phoneNumber(e);} });
		btn3.addMouseListener(new MouseAdapter() { @Override public void mouseClicked(MouseEvent e) {phoneNumber(e);} });
		btn4.addMouseListener(new MouseAdapter() { @Override public void mouseClicked(MouseEvent e) {phoneNumber(e);} });
		btn5.addMouseListener(new MouseAdapter() { @Override public void mouseClicked(MouseEvent e) {phoneNumber(e);} });
		btn6.addMouseListener(new MouseAdapter() { @Override public void mouseClicked(MouseEvent e) {phoneNumber(e);} });
		btn7.addMouseListener(new MouseAdapter() { @Override public void mouseClicked(MouseEvent e) {phoneNumber(e);} });
		btn8.addMouseListener(new MouseAdapter() { @Override public void mouseClicked(MouseEvent e) {phoneNumber(e);} });
		btn9.addMouseListener(new MouseAdapter() { @Override public void mouseClicked(MouseEvent e) {phoneNumber(e);} });
		btn0.addMouseListener(new MouseAdapter() { @Override public void mouseClicked(MouseEvent e) {phoneNumber(e);} });
	}

	public void myCall() {
		JOptionPane.showMessageDialog(null, "Calling\n" + tf.getText());
	}
	
	public void phoneNumber(MouseEvent e) {
		JButton btn = (JButton)e.getSource();
		String str_new = btn.getText();
		String str_old = tf.getText();
		tf.setText(str_old + str_new);
	}
	
}
