import java.util.Arrays;

public class Solution {

    // empty constructor, better explicit than implicit
    public Solution() {

    }

    // manipulate two pointers from front and back
    private int[] moveElementToBack(int[] array, int element) {
        int pointerOne = 0;
        int pointerTwo = array.length - 1;

        while (pointerOne < array.length) {

            while ((array[pointerOne] == element) && (pointerTwo > pointerOne)) {

                if (array[pointerOne] == element && array[pointerTwo] != element) {
                    int originalPointerOne = array[pointerOne];
                    int originalPointerTwo = array[pointerTwo];

                    array[pointerOne] = originalPointerTwo;
                    array[pointerTwo] = originalPointerOne;
                }
                pointerTwo -= 1;
            }

            pointerOne += 1;
        }

        return array;
    }

    public static void main(String[] args) {
        // making new object to encapsulate everything inside of it
        Solution solution = new Solution();

        // array to work on
        int[] arrayToChange = { 2, 1, 2, 2, 2, 3, 4, 2 };

        // element to move
        int elementToMove = 2;

        // prints original array for user to see what it started with
        System.out.println("original: " + Arrays.toString(arrayToChange));

        // runs the moving element to back method and saves the array into
        int[] results = solution.moveElementToBack(arrayToChange, elementToMove);

        // prints out the results for the user to see
        System.out.println("result: " + Arrays.toString(results));

    }

}
