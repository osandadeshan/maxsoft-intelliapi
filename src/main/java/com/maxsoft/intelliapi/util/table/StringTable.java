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

public final class StringTable {

    public final static int GRID_NON = 13;
    public final static int GRID_COLUMN = 15;
    private final Board board;
    private final List<String> headersList;
    private final List<List<String>> rowsList;
    private final List<Integer> colWidthsList;
    private final List<Integer> colAlignsList;
    private final int headerHeight;
    private final int rowHeight;
    private final int gridMode;
    private Block initialTableBlock;

    public StringTable(Board board, int tableWidth, List<String> headersList, List<List<String>> rowsList) {
        this.board = board;
        if (tableWidth <= 0) {
            throw new RuntimeException("Board width must be large than zero. " + tableWidth + " given.");
        }
        if (headersList.size() <= 0) {
            throw new RuntimeException("Header size must be large than zero. " + 0 + " found.");
        } else {
            this.headersList = headersList;
        }
        for (int i = 0; i < rowsList.size(); i++) {
            List<String> row = rowsList.get(i);
            if (row.size() != headersList.size()) {
                throw new RuntimeException("Size(" + row.size() + ") of the row(" + i + ") and header size("
                        + headersList.size() + ") are not equal");
            }
        }
        this.rowsList = rowsList;
        this.colWidthsList = new ArrayList<>();
        int avgWidthOfCol = (tableWidth - (headersList.size() + 1)) / headersList.size();
        int availableForExtend = (tableWidth - (headersList.size() + 1)) % headersList.size();
        for (int i = 0; i < headersList.size(); i++, availableForExtend--) {
            int finalWidth = avgWidthOfCol + (availableForExtend > 0 ? 1 : 0);
            this.colWidthsList.add(finalWidth);
        }
        this.colAlignsList = new ArrayList<>();
        List<String> firstRow = rowsList.get(0);
        for (String cell : firstRow) {
            int alignMode;
            try {
                Long.parseLong(cell);
                alignMode = Block.DATA_MIDDLE_RIGHT;
            } catch (NumberFormatException e0) {
                try {
                    Integer.parseInt(cell);
                    alignMode = Block.DATA_MIDDLE_RIGHT;
                } catch (NumberFormatException e1) {
                    try {
                        Double.parseDouble(cell);
                        alignMode = Block.DATA_MIDDLE_RIGHT;
                    } catch (NumberFormatException e2) {
                        alignMode = Block.DATA_MIDDLE_LEFT;
                    }
                }
            }
            this.colAlignsList.add(alignMode);
        }
        headerHeight = 1;
        rowHeight = 1;
        gridMode = GRID_COLUMN;
    }

    public int getGridMode() {
        return gridMode;
    }

    public Block tableToBlocks() {
        for (int i = 0; i < headersList.size(); i++) {
            String headerValue = headersList.get(i);
            int columnWidth = colWidthsList.get(i);
            Block block = new Block(board, columnWidth, headerHeight, headerValue);
            block.allowGrid(getGridMode() != GRID_NON);
            int alignIndex = colAlignsList.get(i);
            block.setDataAlign(alignIndex);
            if (initialTableBlock == null) {
                initialTableBlock = block;
            } else {
                initialTableBlock.getMostRightBlock().setRightBlock(block);
            }
        }
        if (getGridMode() != GRID_COLUMN) {
            for (List<String> row : rowsList) {
                Block rowStartingBlock = initialTableBlock.getMostBelowBlock();
                for (int j = 0; j < row.size(); j++) {
                    String rowValue = row.get(j);
                    int columnWidth = colWidthsList.get(j);
                    Block block = new Block(board, columnWidth, rowHeight, rowValue);
                    block.allowGrid(getGridMode() != GRID_NON);
                    int alignIndex = colAlignsList.get(j);
                    block.setDataAlign(alignIndex);

                    if (rowStartingBlock.getBelowBlock() == null) {
                        rowStartingBlock.setBelowBlock(block);
                    } else {
                        rowStartingBlock.getBelowBlock().getMostRightBlock().setRightBlock(block);
                    }
                }
            }
        } else {
            for (int i = 0; i < headersList.size(); i++) {
                String columnData = "";
                for (List<String> strings : rowsList) {
                    String rowData = strings.get(i);
                    columnData = columnData.concat(rowData).concat("\n");
                }
                Block block = new Block(board, colWidthsList.get(i), rowsList.size(), columnData);
                int alignIndex = colAlignsList.get(i);
                block.setDataAlign(alignIndex);
                if (initialTableBlock.getBelowBlock() == null) {
                    initialTableBlock.setBelowBlock(block);
                } else {
                    initialTableBlock.getBelowBlock().getMostRightBlock().setRightBlock(block);
                }
            }
        }
        return initialTableBlock;
    }
}
