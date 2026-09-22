package akamori.dev;

import com.googlecode.lanterna.input.KeyStroke;
import com.googlecode.lanterna.input.KeyType;
import com.googlecode.lanterna.terminal.DefaultTerminalFactory;
import com.googlecode.lanterna.terminal.Terminal;


import java.io.IOException;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    static void main() {
            try (Terminal terminal = new DefaultTerminalFactory().createTerminal()) {
                // Terminal functionality here
                Card card = new Card(terminal, "spades");
                card.drawCard(new int[]{10, 10});
                terminal.flush();
                while (true){
                    KeyStroke keystroke = terminal.readInput();
                    if (keystroke.getKeyType() == KeyType.Escape) {
                        break;
                    }
                }
            } catch (IOException e) {
                System.out.println("завершение...");
                throw new RuntimeException(e);

            }
    }
}

