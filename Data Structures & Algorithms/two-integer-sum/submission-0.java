class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> numbers = new HashMap<Integer, Integer>();
        for(int i=0; i<nums.length; i++){
            int currentNum = nums[i];
            int remainingTarget = target - nums[i];

            if(numbers.containsKey(remainingTarget)){
                return new int[] {numbers.get(remainingTarget), i};
            }

            numbers.put(currentNum, i);
        }

        return null;
    }
}
