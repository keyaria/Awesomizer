#!usr/bin/env ruby

require 'rubygems'
require 'wiringpi'

gpio = WiringPi::GPIO.new

led = 1

gpio.mode led, OUTPUT

loop do
	puts "loop..."
	sleep 1
	gpio.write led, 1
	sleep 1
	gpio.write led, 0
end
