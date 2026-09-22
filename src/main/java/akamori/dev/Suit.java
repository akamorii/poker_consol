package akamori.dev;

public class Suit {
    public final String[] suits = new String[]{"spades", "hearts", "diamonds", "clubs" };
    public final String currentSuit;

    public Suit(String currentSuit) {
        this.currentSuit = currentSuit;
    }
}
