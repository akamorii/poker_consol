package akamori.dev;

import com.googlecode.lanterna.terminal.Terminal;

import java.io.IOException;

public class Card {
    public final Terminal terminal;
    public final Suit suit;
    private final int defaultWidth = 5;
    private final int defaultheight = 3;
    private final int X = 0;
    private final int Y = 1;
    private final int RIGHTUPANGLE = 2;
    private final int LEFTUPANGLE = 0;
    private final int STRAIGHT = 1;
    private final int VERTICALSTRAIGHT = 3;
    private final int LEFTDOWNANGLE = 4;
    private final int RIGHTDOWNANGLE = 5;
// [ ╔ ═ ╗ ║ ╚ ╝ ]
    public Card(Terminal terminal, String suit) throws Suit.IncorrectSuit {
        this.terminal = terminal;
        this.suit = new Suit(suit);
    }

    public void drawCard(int[] position, char[] symbols) throws IOException {
        for (int i = position[X]; i < position[X]+defaultWidth; i++) {
            terminal.setCursorPosition(i, position[Y]);
                if (i == position[X]) terminal.putCharacter(symbols[LEFTUPANGLE]);
                else if (i == position[X]+defaultWidth-1) terminal.putCharacter(symbols[RIGHTUPANGLE]);
                else terminal.putCharacter(symbols[STRAIGHT]);
            }
        for (int i = position[Y]; i < position[Y]+defaultheight; i++){
            terminal.setCursorPosition(position[X], i+1);
            terminal.putCharacter(symbols[VERTICALSTRAIGHT]);
            terminal.setCursorPosition(position[X]+defaultWidth-1, i+1);
            terminal.putCharacter(symbols[VERTICALSTRAIGHT]);
        }
        for (int i = position[X]; i < position[X]+defaultWidth; i++) {
            terminal.setCursorPosition(i, position[Y]+defaultheight);
                if (i == position[X]) terminal.putCharacter(symbols[LEFTDOWNANGLE]);
                else if (i == position[X]+defaultWidth-1) terminal.putCharacter(symbols[RIGHTDOWNANGLE]);
                else terminal.putCharacter(symbols[STRAIGHT]);
            }

        }
//        terminal.putCharacter('l');
//        terminal.putCharacter('l');
//        terminal.putCharacter('o');
}
