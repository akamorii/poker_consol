package akamori.dev;

import java.util.Arrays;

public class Suit {
    public final String[] suits = new String[]{"spades", "hearts", "diamonds", "clubs" };
    public final String currentSuit;

    public class IncorrectSuit extends Exception {

        public IncorrectSuit() {
            super();
        }

        // Конструктор с сообщением об ошибке
        public IncorrectSuit(String message) {
            super(message);
        }
    }

    public Suit(String currentSuit) throws IncorrectSuit {
        this.currentSuit = currentSuit;
        if (Arrays.asList(suits).contains(currentSuit));
        else throw new IncorrectSuit("this suit does not exist");

    }

    public char[] getCardElements() {
        switch (this.currentSuit) {
            case "spades":
                return new char[]{'╔', '═', '╗', '║', '╚', '╝'};
            case "hearts":
                return new char[]{'@','@','@','@','@','@'};
        }

        return new char[]{0};
    }
}
