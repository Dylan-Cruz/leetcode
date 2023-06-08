package leetcode;

class Solution {
    public int maximumPopulation(int[][] logs) {
        // make array of size 101 since it's the size of the timespan constraint
        int[] populations = new int[101];

        // create the timeline of births and deaths for the timespan where the array
        // position is the year and the value is the number of additions for that year
        for (int log[] : logs) {
            populations[log[0]-1950]++;
            populations[log[1]-1950]--;
        }

        // reference values to track the earliest year of the greatest population
        int year = 1950;
        int max = populations[0];

        // track in place by year the number of people alive
        for (int i = 1; i < 101; i++) {
            populations[i] += populations[i-1];
            if (populations[i] > max) {
                max = populations[i];
                year = i+1950;
            }
        }

        return year;
    }
}

// time complexity: O(n) - linear time
// space complexity: O(101)