//------------------------------------------------------------------------------
//  Remove Element
//------------------------------------------------------------------------------
// By Daniel Speer
// https://leetcode.com/problems/remove-element/
// Completed 6/17/19
//------------------------------------------------------------------------------
//  Solution
//------------------------------------------------------------------------------

fn remove_ele(nums: &mut Vec<i32>, val: i32) -> i32 {
    let mut pointer = 0;
    for i in 0..nums.len() {
        if nums[i] != val {
            nums[pointer] = nums[i];
            pointer += 1
        }
    }

    pointer as i32
}

//------------------------------------------------------------------------------
//  Leetcode Driver
//------------------------------------------------------------------------------

impl Solution {
    pub fn remove_element(nums: &mut Vec<i32>, val: i32) -> i32 {
        remove_ele(nums, val)
    }
}
