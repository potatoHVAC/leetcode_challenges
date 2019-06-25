//------------------------------------------------------------------------------
//  Implement strStr()
//------------------------------------------------------------------------------
// By Daniel Speer
// https://leetcode.com/problems/implement-strstr/
// Completed 6/17/19
//------------------------------------------------------------------------------
//  Solution
//------------------------------------------------------------------------------

fn my_str(haystack: String, needle: String) -> i32 {
    let string:Vec<char> = haystack.chars().collect();
    let target:Vec<char> = needle.chars().collect();
    
    for i in 0..string.len() {
        for j in 0..target.len() {
            if i+j >= string.len() || string[i+j] != target[j] {
                break;
            } else if j == target.len() - 1 {
                return i as i32
            }
        }
    }
    if needle == "" {
        0 as i32
    } else {
        -1 as i32
    }
}

//------------------------------------------------------------------------------
//  Leetcode Driver
//------------------------------------------------------------------------------

impl Solution {
    /// Return the starting index of needle in haystack or -1.
    ///
    /// # Arguments
    /// * :haystack: -> string to check for substrings
    /// * :needle:   -> substring to find in :haystack:
    ///
    /// # Return
    /// index of the start of needle
    pub fn str_str(haystack: String, needle: String) -> i32 {
        my_str(haystack, needle)
    }
}
