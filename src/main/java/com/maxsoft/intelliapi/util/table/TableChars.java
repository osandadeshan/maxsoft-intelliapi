package com.maxsoft.intelliapi.util.table;

/**
 * Project Name : MaxSoft-IntelliAPI
 * Developer    : Osanda Deshan
 * Version      : 1.0.0
 * Date         : 6/30/2018
 * Time         : 3:51 PM
 * Description  :
 **/


class TableChars {

    protected static final char S = '-';

    protected static final char NL = '\n';

    protected static final char P = '+';

    protected static final char D = '=';

    protected static final char VL = '|';

    private final int x;

    private final int y;

    private final char c;

    protected TableChars(int x, int y, char c) {
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
