#-------------------------------------------------------------------------------
#    Plus one
#-------------------------------------------------------------------------------
# By Daniel Speer
# https://en.wikibooks.org/wiki/Ruby_Programming/Unit_testing
# Completed 6/20/19
#-------------------------------------------------------------------------------
#    Main Leetcode Input Driver
#-------------------------------------------------------------------------------

# @param {Integer[]} digits
# @return {Integer[]}
def plus_one(digits)
  i = digits.length - 1
  carry = 1
  
  while i >= 0
    sum = digits[i] + carry
    digits[i] = sum % 10
    carry = sum / 10

    i -= 1
    if carry == 0
      i = -1
    end
  end

  digits.unshift(1) if carry == 1
  digits
end

#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------

require "test/unit"

class TestSolution < Test::Unit::TestCase

  def test_zero
    assert_equal([1], plus_one([0]))
  end
  def test_1
    assert_equal([2], plus_one([1]))
  end
  def test_nine
    assert_equal([1,0], plus_one([9]))
  end
  def test_ex1
    assert_equal([1,2,4], plus_one([1,2,3]))
  end
  def test_ex2
    assert_equal([4,3,2,2], plus_one([4,3,2,1]))
  end
  def test_nines
    assert_equal([1,0,0,0], plus_one([9,9,9]))
  end
  def test_nine_and_other
    assert_equal([3,0,0,0], plus_one([2,9,9,9]))
  end
  
end
