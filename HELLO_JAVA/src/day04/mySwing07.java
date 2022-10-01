package day04;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JTextField;
import javax.swing.JButton;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.util.Random;

public class mySwing07 extends JFrame {

	private JPanel contentPane;
	private JTextField tfMine;
	private JTextField tfCom;
	private JTextField tfResult;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					mySwing07 frame = new mySwing07();
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
	public mySwing07() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lblMine = new JLabel("나");
		lblMine.setBounds(54, 40, 57, 15);
		contentPane.add(lblMine);
		
		JLabel lblCom = new JLabel("컴");
		lblCom.setBounds(54, 85, 57, 15);
		contentPane.add(lblCom);
		
		JLabel lblResult = new JLabel("결과");
		lblResult.setBounds(54, 135, 57, 15);
		contentPane.add(lblResult);
		
		tfMine = new JTextField();
		tfMine.setBounds(146, 37, 116, 21);
		contentPane.add(tfMine);
		tfMine.setColumns(10);
		
		tfCom = new JTextField();
		tfCom.setColumns(10);
		tfCom.setBounds(146, 82, 116, 21);
		contentPane.add(tfCom);
		
		tfResult = new JTextField();
		tfResult.setColumns(10);
		tfResult.setBounds(146, 132, 116, 21);
		contentPane.add(tfResult);
		
		JButton btn = new JButton("게임하기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myclick();
			}
		});
		btn.setBounds(54, 177, 208, 32);
		contentPane.add(btn);
	}
	
	public void myclick() {
		String mine = tfMine.getText();
		int rnd = new Random().nextInt(3);
		String com = "";
		String result = "";
		
	
		switch(rnd) {
		case 0:
			com = "바위";
			break;
		case 1:
			com = "가위";
			break;
		case 2:
			com = "보";
			break;
		default:
			break;
		}
		
		if(mine.equals(com)) {
			result = "무승부";
		} else if((mine.equals("가위") && com.equals("보"))
					|| (mine.equals("보") && com.equals("바위"))
					|| (mine.equals("바위") && com.equals("가위"))) {
			result = "승리";
		} else {
			result = "패배";
		}
		
		tfCom.setText(com);
		tfResult.setText(result);
	}
}
