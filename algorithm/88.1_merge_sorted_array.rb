#-------------------------------------------------------------------------------
#    Merge Sorted Array
#-------------------------------------------------------------------------------
# By Daniel Speer
# https://leetcode.com/problems/merge-sorted-array/
# 
#-------------------------------------------------------------------------------
#    Soluton
#-------------------------------------------------------------------------------

# @param {Integer[]} nums1
# @param {Integer} m
# @param {Integer[]} nums2
# @param {Integer} n
# @return {Void} Do not return anything, modify nums1 in-place instead.
def merge(nums1, m, nums2, n)
  insert_pos = m + n - 1
  n -= 1
  m -= 1

  while insert_pos >= 0
    if n == -1
      break
      
    elsif m >= 0
      if nums2[n] >= nums1[m]
        nums1[insert_pos] = nums2[n]
        n -= 1
      else
        nums1[insert_pos] = nums1[m]
        m -= 1
      end
      
    else
      nums1[insert_pos] = nums2[n]
      n -= 1
    end
    
    insert_pos -= 1
  end

  nums1
end

#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------

require "test/unit"

class TestSolution < Test::Unit::TestCase

  def test_1
    assert_equal([1, 2], merge([2, 0], 1, [1], 1))
  end
  def test_2
    assert_equal([1, 2], merge([1, 0], 1, [2], 1))
  end
  def test_3
    assert_equal([2, 2], merge([2, 0], 1, [2], 1))
  end
  def test_4
    assert_equal([1, 1, 2], merge([1, 2, 0], 2, [1], 1))
  end
  def test_5
    assert_equal([1, 1, 2, 2], merge([1, 2, 0, 0], 2, [1, 2], 2))
  end

end
