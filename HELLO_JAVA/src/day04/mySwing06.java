package day04;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JTextField;
import javax.swing.JButton;
import javax.swing.JTextArea;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class mySwing06 extends JFrame {

	private JPanel contentPane;
	private JTextField tfDan;
	private JTextArea ta;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					mySwing06 frame = new mySwing06();
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
	public mySwing06() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 307, 398);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lbl = new JLabel("출력 단수");
		lbl.setBounds(41, 41, 57, 15);
		contentPane.add(lbl);
		
		tfDan = new JTextField();
		tfDan.setBounds(148, 38, 91, 21);
		contentPane.add(tfDan);
		tfDan.setColumns(10);
		
		JButton btn = new JButton("출력하기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myclick();
			}
		});
		btn.setBounds(41, 66, 198, 31);
		contentPane.add(btn);
		
		ta = new JTextArea();
		ta.setBounds(41, 107, 198, 218);
		contentPane.add(ta);
	}
	
	public void myclick() {
		int dan = Integer.valueOf(tfDan.getText());
		StringBuilder builder = new StringBuilder();
		
		builder.append(dan + "단을 출력합니다. \n");
		
		for(int i=1; i<=9; i++) {
			builder.append(String.format("%s * %s = %s\n",dan,i,dan*i));
		}
		
		ta.setText(builder.toString());
	}
}
