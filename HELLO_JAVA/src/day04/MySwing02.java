package day04;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JButton;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;

public class MySwing02 extends JFrame {

	private JPanel contentPane;
	JLabel lbl;
	
	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing02 frame = new MySwing02();
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
	public MySwing02() {
		
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		lbl = new JLabel("100");
		lbl.setBounds(46, 46, 57, 15);
		contentPane.add(lbl);
		
		JButton btn = new JButton("decrease");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mousePressed(MouseEvent e) {
				int count = Integer.valueOf(lbl.getText());
				count--;
				lbl.setText(String.valueOf(count));
			}
		});
		btn.setBounds(159, 42, 97, 23);
		contentPane.add(btn);
	}

	public void myclick() {
		String a = lbl.getText();
		int aa = Integer.parseInt(a);
		aa--;
		lbl.setText(aa+"");
	}
}
