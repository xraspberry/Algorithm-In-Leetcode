class RecentCounter
  def initialize()
    @counter = []
  end


=begin
    :type t: Integer
    :rtype: Integer
=end
  def ping(t)
    threshold = t - 3000
    while !@counter.empty? and @counter[0] < threshold
      @counter.shift
    end
    @counter.push(t)
    return @counter.size
  end


end

# Your RecentCounter object will be instantiated and called as such:
obj = RecentCounter.new()
param_1 = obj.ping(1000)
