#-------------------------------------------------------------------------------
#    Add Binary
#-------------------------------------------------------------------------------
# By Daniel Speer
# https://leetcode.com/problems/add-binary/
# Completed 6/20/19
#-------------------------------------------------------------------------------
#    Soluton
#-------------------------------------------------------------------------------

# @param {String} a
# @param {String} b
# @return {String}
def add_binary(str1, str2)
  (str1.to_i(2) + str2.to_i(2)).to_s(2)  
end

#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------

require "test/unit"

class TestSolution < Test::Unit::TestCase

  def test_0_0
    assert_equal('0', add_binary('0','0'))
  end
  def test_0_1
    assert_equal('1', add_binary('0','1'))
  end
  def test_1_1
    assert_equal('10', add_binary('1','1'))
  end
  def test_ex1
    assert_equal('100', add_binary('11','1'))
  end
  def test_ex2
    assert_equal('10101', add_binary('1010','1011'))
  end

end
