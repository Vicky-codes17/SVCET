import javafx.application.Application;
import javafx.stage.Stage;

public class FirstGUI extends Application
{
	public static void main(String[] args)
	{
		launch(args);
	}
	
	@Override
	public void start(Stage primaryStage)
	{
		primaryStage.setTitle("Welcome to SVCET");

		primaryStage.show();
	}
}