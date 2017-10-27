
@books = JSON.parse @aString
builder = Nokogiri::XML::Builder.new do |xml|
xml.root{
  xml.books {
    @books.each do |data|
  data.each do |stuff,text|
end
end
  }
}


end
puts builder.to_xml

