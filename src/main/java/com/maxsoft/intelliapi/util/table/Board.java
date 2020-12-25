package com.maxsoft.intelliapi.util.table;

import java.util.ArrayList;
import java.util.List;

/**
 * Project Name : MaxSoft-IntelliAPI
 * Developer    : Osanda Deshan
 * Version      : 1.0.0
 * Date         : 6/30/2018
 * Time         : 3:51 PM
 * Description  :
 **/

public class Board {

    protected final boolean showBlockIndex;
    protected final int boardWidth;
    private Block initialBlock;
    private final List<TableChars> charsInTableBoarders;
    private String preview;

    public Board(int boardWidth) {
        this.boardWidth = boardWidth;
        this.charsInTableBoarders = new ArrayList<>();
        this.preview = "";
        this.showBlockIndex = false;
        Block.nextIndex = 0;
    }

    public Board setInitialBlock(Block initialBlock) {
        this.initialBlock = initialBlock;
        return this;
    }

    private void rearrangeCoordinates(Block block) {
        Block rightBlock = block.getRightBlock();
        Block belowBlock = block.getBelowBlock();
        if (rightBlock != null && belowBlock == null) {
            block.setRightBlock(rightBlock);
            rearrangeCoordinates(rightBlock);
        } else if (rightBlock == null && belowBlock != null) {
            block.setBelowBlock(belowBlock);
            rearrangeCoordinates(belowBlock);
        } else if (rightBlock != null) {
            int rightIndex = rightBlock.getIndex();
            int belowIndex = belowBlock.getIndex();
            int blockIdDiff = rightIndex - belowIndex;
            if (blockIdDiff > 0) {
                block.setRightBlock(rightBlock);
                if (blockIdDiff == 1) {
                    block.setBelowBlock(belowBlock);
                    rearrangeCoordinates(rightBlock);
                } else {
                    rearrangeCoordinates(rightBlock);
                    block.setBelowBlock(belowBlock);
                }
                rearrangeCoordinates(belowBlock);
            } else if (blockIdDiff < 0) {
                blockIdDiff *= -1;
                block.setBelowBlock(belowBlock);
                if (blockIdDiff == 1) {
                    block.setRightBlock(rightBlock);
                    rearrangeCoordinates(belowBlock);
                } else {
                    rearrangeCoordinates(belowBlock);
                    block.setRightBlock(rightBlock);
                }
                rearrangeCoordinates(rightBlock);
            }
        }
    }

    public Board build() {
        if (charsInTableBoarders.isEmpty()) {
            buildBlock(initialBlock);
            dumpCharrsFromBlock(initialBlock);

            int maxY = -1;
            int maxX = -1;
            for (TableChars charsInTableBoarder : charsInTableBoarders) {
                int testY = charsInTableBoarder.getY();
                int testX = charsInTableBoarder.getX();
                if (maxY < testY) {
                    maxY = testY;
                }
                if (maxX < testX) {
                    maxX = testX;
                }
            }
            String[][] dataPoints = new String[maxY + 1][boardWidth];
            for (TableChars tableChars : charsInTableBoarders) {
                String currentValue = dataPoints[tableChars.getY()][tableChars.getX()];
                String newValue = String.valueOf(tableChars.getC());
                if (currentValue == null || !currentValue.equals("+")) {
                    dataPoints[tableChars.getY()][tableChars.getX()] = newValue;
                }
            }

            for (String[] dataPoint : dataPoints) {
                for (String point : dataPoint) {
                    if (point == null) {
                        point = String.valueOf(TableChars.S);
                    }
                    preview = preview.concat(point);
                }
                preview = preview.concat(String.valueOf(TableChars.NL));
            }
        }

        return this;
    }

    public String getPreview() {
        build();
        return preview;
    }

    private void buildBlock(Block block) {
        if (block != null) {
            block.build();
            buildBlock(block.getRightBlock());
            buildBlock(block.getBelowBlock());
        }
    }

    private void dumpCharrsFromBlock(Block block) {
        if (block != null) {
            charsInTableBoarders.addAll(block.getChars());
            dumpCharrsFromBlock(block.getRightBlock());
            dumpCharrsFromBlock(block.getBelowBlock());
        }
    }

    private void invalidateBlock(Block block) {
        if (block != null) {
            block.invalidate();
            invalidateBlock(block.getRightBlock());
            invalidateBlock(block.getBelowBlock());
        }
    }
}
