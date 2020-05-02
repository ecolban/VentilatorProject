package screens;

import processing.core.PApplet;
import ventilator.App;

public class Menu {

	static final int startButtonX = 100;
	static final int startButtonY = 200;
	static final int startButtonWidth = 100;
	static final int startButtonHeight = 50;

	public void display(PApplet app) {
		
		app.fill(255);
		app.rect(100, 200, startButtonWidth, startButtonHeight);
		app.fill(0);
		app.text("start", 135, 230);
	}

	public void update() {
		 
	}

	public void onClick(int x, int y) {
		if (x >= startButtonX && y >= startButtonY && x <= startButtonX + startButtonWidth
				&& y <= startButtonY + startButtonHeight) {
			System.out.println("works");
			App.currentState = App.CHART;
		}

	}
}
