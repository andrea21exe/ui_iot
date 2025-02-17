using System;
using Microsoft.UI.Input;

namespace IotClient;


public partial class MainPage : ContentPage
{
	int count = 0;

	public MainPage()
	{
		InitializeComponent();
		showData();
	}

	private void showData(){
		
		// TODO MODIFICA QUESTI VALORI
		double THRESHOLD = 1;
		string filepath = "C:\\Users\\andre\\Documents\\ui_iot\\IotClient\\file.json";
		// -------------------------

		var elementi = Client.readJson(filepath);
		double valore1 = elementi["Valore 1"];
		double valore2 = elementi["Valore 2"];
		double valore3 = elementi["Valore 3"];

		Value1Label.Text = valore1.ToString();
		Value2Label.Text = valore2.ToString();
		Value3Label.Text = valore3.ToString();


		// TODO cambiare i file path
		if (valore1 > THRESHOLD) {
			img1.Source = "C:\\Users\\andre\\Documents\\ui_iot\\IotClient\\ok.png";
		} else {
			img1.Source = "C:\\Users\\andre\\Documents\\ui_iot\\IotClient\\bad.png";
		}

		if (valore2 > THRESHOLD) {
			img2.Source = "C:\\Users\\andre\\Documents\\ui_iot\\IotClient\\ok.png";
		} else {
			img2.Source = "C:\\Users\\andre\\Documents\\ui_iot\\IotClient\\bad.png";
		}

		if (valore3 > THRESHOLD) {
			img3.Source = "C:\\Users\\andre\\Documents\\ui_iot\\IotClient\\ok.png";
		} else {
			img3.Source = "C:\\Users\\andre\\Documents\\ui_iot\\IotClient\\bad.png";
		}
		// ---------------------------

	}
}

