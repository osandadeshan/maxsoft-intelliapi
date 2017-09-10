/**
 * Created by Osanda on 7/18/2017.
 */


class CharsUsedForTable {
    
    protected static final char S = '-';
    
    protected static final char NL = '\n';
    
    protected static final char P = '+';
    
    protected static final char D = '=';
    
    protected static final char VL = '|';

    private final int x;

    private final int y;

    private final char c;

    protected CharsUsedForTable(int x, int y, char c) {
        this.x = x;
        this.y = y;
        this.c = c;
    }

    protected int getX() {
        return x;
    }

    protected int getY() {
        return y;
    }

    protected char getC() {
        return c;
    }

}
