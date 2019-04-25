# @param {Integer} num_courses
# @param {Integer[][]} prerequisites
# @return {Boolean}

class CourseSchedule

  attr_accessor :course
  
  def initialize(number_of_classes)
    @course = populate(number_of_classes)
  end
  
  def populate(number_of_classes)
    class_list = [*0...number_of_classes].map(num, Node.new(num))
  end

end

class Node
  def initialize(number)
    @number = number
    @
  end
end

def can_finish(num_courses, prerequisites)
    
  
end
