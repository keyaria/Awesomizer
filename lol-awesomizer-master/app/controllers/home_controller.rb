require 'csv' 
class HomeController < ApplicationController
  def index
 
      #  clnt = HTTPClient.new
      #  @aString = clnt.get_content("http://mjc12-dev.library.cornell.edu:3000/list")
         @aString = CSV.read("/app/assets/CSVfile/SDL_Books.csv - SDL_Books.csv.csv")

        
	end

def feed

	#clnt = HTTPClient.new
   # @aString = clnt.get_content("http://mjc12-dev.library.cornell.edu:3000/list")
    @aString = CSV.read("/app/assets/CSVfile/SDL_Books.csv - SDL_Books.csv.csv")
    @objects = JSON.parse @aString


    respond_to do |format|
      format.xml #index.atom.builder
      format.rss
    
    end
end
end



