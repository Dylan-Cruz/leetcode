package twosum_easy;

import java.util.Map;
import java.util.HashMap;

/**
 * https://leetcode.com/problems/two-sum/
 * 
 * 1. Two Sum
 * Given an array of integers nums and an integer target, return indices of the
 * two numbers such that they add up to target.
 * You may assume that each input would have exactly one solution, and you may
 * not use the same element twice.
 * You can return the answer in any order.
 * 
 * 
 * Example 1:
 * 
 * Input: nums = [2,7,11,15], target = 9
 * Output: [0,1]
 * Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
 * 
 * Example 2:
 * 
 * Input: nums = [3,2,4], target = 6
 * Output: [1,2]
 * 
 * Example 3:
 * 
 * Input: nums = [3,3], target = 6
 * Output: [0,1]
 * 
 * 
 * 
 * Constraints:
 * 
 * 2 <= nums.length <= 104
 * -109 <= nums[i] <= 109
 * -109 <= target <= 109
 * Only one valid answer exists.
 * 
 */

public class Solution {
	public int[] twoSum(int[] nums, int target) {
		/*
		 * iterate over nums
		 * check if the compliment is in the hash map
		 * if not, add it to the map where the compliment is the key and the index is the value
		 * if so, return the indices
		 * if no match is found, return an empty array
		 */
		Map<Integer, Integer> complimentToIndexMap = new HashMap<>();

		for (int i = 0; i < nums.length; i++) {
			int compliment = target - nums[i];
			if (complimentToIndexMap.containsKey(compliment)) {
				return new int[] { i, complimentToIndexMap.get(compliment) };
			} else {
				complimentToIndexMap.put(nums[i], i);
			}
		}

		return new int[0];
	}

	public static void main(String[] args) {
		System.out.println("Run tests with 'gradle test'.");
	}
}
