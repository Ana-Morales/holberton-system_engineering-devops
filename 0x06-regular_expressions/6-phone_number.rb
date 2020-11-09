#!/usr/bin/env ruby
puts ARGV[0].scan(/\A[0-9][0-9]{9}\z/).join
