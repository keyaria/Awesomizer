module HomeHelper

		def book_covers
		clnt = HTTPClient.new
        @coverString = clnt.get_content("https://www.googleapis.com/books/v1/volumes?q=oclc:#{@gb_cover}")
        @coverString = JSON.parse(@coverString)["items"] 
      

end
end