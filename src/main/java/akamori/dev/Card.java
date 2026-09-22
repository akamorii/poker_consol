package akamori.dev;

import com.googlecode.lanterna.terminal.Terminal;

import java.io.IOException;

public class Card {
    public final Terminal terminal;
    private final Suit suit;
    private final int defaultWidth = 5;
    private final int defaultheight = 3;
    private final int X = 0;
    private final int Y = 1;

    public Card(Terminal terminal, String suit) {
        this.terminal = terminal;
        this.suit = new Suit(suit);
    }

    public void drawCard(int[] position) throws IOException {
        for (int i = position[X]; i < position[X]+defaultWidth; i++) {
            terminal.setCursorPosition(i, position[Y]);
                if (i == position[X]) terminal.putCharacter('╔');
                else if (i == position[X]+defaultWidth-1) terminal.putCharacter('╗');
                else terminal.putCharacter('═');
            }
        for (int i = position[Y]; i < position[Y]+defaultheight; i++){
            terminal.setCursorPosition(position[X], i+1);
            terminal.putCharacter('║');
            terminal.setCursorPosition(position[X]+defaultWidth-1, i+1);
            terminal.putCharacter('║');
        }
        for (int i = position[X]; i < position[X]+defaultWidth; i++) {
            terminal.setCursorPosition(i, position[Y]+defaultheight);
                if (i == position[X]) terminal.putCharacter('╚');
                else if (i == position[X]+defaultWidth-1) terminal.putCharacter('╝');
                else terminal.putCharacter('═');
            }

        }
//        terminal.putCharacter('l');
//        terminal.putCharacter('l');
//        terminal.putCharacter('o');
}
