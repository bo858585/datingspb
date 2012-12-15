from scrapy.spider import BaseSpider
from scrapy.http import FormRequest, Request
from scrapy.selector import XPathSelector

# Search request parameters for main page

search_form_data = { 
	"action": "1",
	"ext_params[users][age][from]": "23",
	"ext_params[users][age][to]": "30",
	"ext_params[users][city]": "101_6755_2992300",
	"ext_params[users][iam]": "M",
	"ext_params[users][lookfor]": "F",
	"ext_params[users][photo]": "on",
	"metros": "",
	"search_type": "",
	"submit.x": "52",
	"submit.y": "16"
}

# Xpath of user profile link on main page     
user_profile_link_xpath = "/html/body/table[2]/tr/td[2]/table[5]/tr/td/a/@href"

# Main search page
main_search_page_url = "http://datingspb.ru/search.php" 

# Page for sending message to user
send_message_to_user_page_url = "http://datingspb.ru/message.php?oid="

class DatingspbSpider(BaseSpider):
    """
    Spider
    """

    name = "datingspb"
    allowed_domains = ["datingspb.ru"]
    start_urls = ["http://datingspb.ru/search.php"]

    def start_requests(self):
        """
        Make search with params on main page
        """   
        try:  
            return [FormRequest(url=main_search_page_url,
                    formdata=search_form_data,
                    callback=self.explore_search_results)]
        except Exception, e:
            print e 
	
    def explore_search_results(self, response):
        """
        Goes to 10 send message to user pages from the search results page
        """
    
        try: 
            selector = XPathSelector(response)

            # Extract 10 user profile links from page 
            for href in selector.select(user_profile_link_xpath).extract():                                         
                try:   
                    # For each link get user oid (identifier)
                    splitted_href = href.replace("&", "=").split("=")             
                    oid_value_index = splitted_href.index("oid") + 1                
                    # Go to send message to user page by using oid
                    yield Request(url=send_message_to_user_page_url + splitted_href[oid_value_index], callback=self.explore_user_pm_page)
	        except Exception, e:
                    print e
                    pass  

        except Exception, e:
            print e 

    def explore_user_pm_page(self, response):
        """
        Goes to personal message to user form page
        """

        try:
            print response
               
        except Exception, e:
            print e 
        

