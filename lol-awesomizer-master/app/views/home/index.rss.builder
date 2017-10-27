    @objects = JSON.parse @aString
    @objects.sort_by! { | h | h["timestamp"] }.reverse!


xml.instruct! :xml, :version=>"1.0"
xml.rss(:version=>"2.0") {
        
  xml.channel {
          
    xml.title('The Awesomizer')
    xml.link('http://awesome.library.cornell.edu')
    xml.description('Awesome stuff at Cornell University Library')
    xml.language('en-us')
    @objects.each do |data|
      xml.title( data["title"] )
      xml.link( 'http://newcatalog.library.cornell.edu/catalog/' + data["bibid"].to_s)
      xml.description ( data["title"] + ' / ' + data["author"] + ' / Votes:' + data["votes"].to_s )
    end
          
  }
}


