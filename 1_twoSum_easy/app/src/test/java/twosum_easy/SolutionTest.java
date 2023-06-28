
package twosum_easy;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class SolutionTest {
    private Solution classUnderTest = new Solution();


    @Test void correctAnswer() {
        int[] nums = new int[]{2,7,11,15};
        assertArrayEquals(new int[]{1,0}, classUnderTest.twoSum(nums,9));
    }

    @Test void duplicateNumbers() {
        int[] nums = new int[]{2,3,3,7,10};
        assertArrayEquals(new int[]{2,1}, classUnderTest.twoSum(nums, 6));
    }

    @Test void negativeNumbers() {
        int[] nums = new int[]{-7,1,9,3,5,4};
        assertArrayEquals(new int[]{2,0}, classUnderTest.twoSum(nums, 2));
    }

    @Test void unorderedNumbers() {
        int[] nums = new int[]{7,1,9,3,5,4};
        assertArrayEquals(new int[]{5,0}, classUnderTest.twoSum(nums, 11));
    }

    @Test void noAnswer() {
        int[] nums = new int[]{7,1,9,3,5,4};
        assertArrayEquals(new int[]{}, classUnderTest.twoSum(nums, 100));
    }

    @Test void emptyArray() {
        int[] nums = new int[0];
        assertArrayEquals(new int[]{}, classUnderTest.twoSum(nums, 21));
    }
}
