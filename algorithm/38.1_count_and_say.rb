#-------------------------------------------------------------------------------
#    Count and Say
#-------------------------------------------------------------------------------
# By Daniel Speer
# https://leetcode.com/problems/count-and-say/
# Completed 6/26/19
#-------------------------------------------------------------------------------
#    Soluton
#-------------------------------------------------------------------------------

# @param {Integer} n
# @return {String}
def count_and_say(n)
  def _count_and_say(n, string)
    return string if n == 1

    ans = ""
    i = 0
    while i < string.length
      target = string[i]
      count = 1
      j = i + 1
      while j < string.length and string[j] == target
        count += 1
        j += 1
      end

      ans += count.to_s + target
      i += j - i
    end

    _count_and_say(n - 1, ans)
  end

  _count_and_say(n, "1")
end

#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------

require "test/unit"

class TestSolution < Test::Unit::TestCase

  def test_1
    n = 1
    ans = "1"
    assert_equal(ans, count_and_say(n))
  end
  def test_2
    n = 2
    ans = "11"
    assert_equal(ans, count_and_say(n))
  end
  def test_3
    n = 3
    ans = "21"
    assert_equal(ans, count_and_say(n))
  end
  def test_4
    n = 4
    ans = "1211"
    assert_equal(ans, count_and_say(n))
  end
  def test_5
    n = 5
    ans = "111221"
    assert_equal(ans, count_and_say(n))
  end
  def test_6
    n = 6
    ans = "312211"
    assert_equal(ans, count_and_say(n))
  end
end
