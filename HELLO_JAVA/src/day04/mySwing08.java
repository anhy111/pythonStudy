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

public class mySwing08 extends JFrame {

	private JPanel contentPane;
	private JTextField tfFirst;
	private JTextField tfLast;
	private JTextArea ta;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					mySwing08 frame = new mySwing08();
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
	public mySwing08() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 344, 436);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lblFirst = new JLabel("첫별수");
		lblFirst.setBounds(45, 42, 57, 15);
		contentPane.add(lblFirst);
		
		JLabel lblLast = new JLabel("끝별수");
		lblLast.setBounds(45, 100, 57, 15);
		contentPane.add(lblLast);
		
		tfFirst = new JTextField();
		tfFirst.setBounds(167, 39, 116, 21);
		contentPane.add(tfFirst);
		tfFirst.setColumns(10);
		
		tfLast = new JTextField();
		tfLast.setColumns(10);
		tfLast.setBounds(167, 97, 116, 21);
		contentPane.add(tfLast);
		
		JButton btn = new JButton("별 출력하기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				samclick();
			}
		});
		btn.setBounds(48, 136, 235, 28);
		contentPane.add(btn);
		
		ta = new JTextArea();
		ta.setBounds(45, 176, 235, 198);
		contentPane.add(ta);
	}
	
	public void myclick() {
		int first = Integer.parseInt(tfFirst.getText());
		int last = Integer.parseInt(tfLast.getText());
		String star = "";
		
//		int row = last - first;
//		for(int i=0; i<=row; i++) {
//			for(int j=0; j<first+i; j++) {
//				star += "*";
//			}
//			star += "\n";
//		}
		
//		for(int i=0; i<=last; i++) {
//			if(i < first) {
//				continue;
//			}
//			for(int j=0; j<=last; j++) {
//				if(j >= i) {
//					break;
//				}
//				star += "*";
//			}
//			star += "\n";
//		}
		
		for(int i=first; i<=last; i++) {
			for(int j=0; j<i; j++) {
				star += "*";
			}
			star += "\n";
		}
		
		ta.setText(star);
	}
	
	public void samclick() {
		String a = tfFirst.getText();
		String b = tfLast.getText();
		
		int aa = Integer.parseInt(a);
		int bb = Integer.parseInt(b);
		
		String txt = "";
		for(int i=aa; i<=bb; i++) {
			txt += drawStar(i);
		}
		ta.setText(txt);
	}
	
	public String drawStar(int cnt) {
		String ret = "";
		for(int i=0; i<cnt; i++) {
			ret += "*";
		}
		
		ret += "\n";
		return ret;
	}
}
