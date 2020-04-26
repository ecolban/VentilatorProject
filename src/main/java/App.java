import processing.core.PApplet;

public class App extends PApplet {

    // The argument passed to main must match the class name
    public static void main(String[] args) {
        PApplet.main("App");
    }

    // method used only for setting the size of the window
    public void settings(){
        size(500,500);
    }

    // identical use to setup in Processing IDE except for size()
    public void setup(){
        
    }

    // identical use to draw in Prcessing IDE
    public void draw(){
    	ellipse(50,50,50,50);
    }
}