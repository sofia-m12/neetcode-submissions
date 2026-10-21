class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] indices = {0,1};
        if(nums.length == 2){
            return indices;
        }
        //int[] indices = new int[2];
        for(int i = 0;i<nums.length;i++){
            for(int j = i+1;j<nums.length;j++){
                if(target == (nums[i]+nums[j]) && i!=j){
                    //Assigning to array because it can't be appended to(its not an ArrayList)
                    indices[0] = i;
                    indices[1] = j;
                    break;
                }
            }
        }
        return indices;
    }
}
