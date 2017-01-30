Feature: Retrieving a list products from an example category page

  @local
  Scenario: Scraping an example page for categories
    Given I have the example page clothing.html
     when I scrape that page for categories
     then I get the categories:
      | title                 | url                                                       |
      | Shirts                | http://www.farah.co.uk/clothing/shirts?sz=60              |
      | T-shirts              | http://www.farah.co.uk/clothing/t-shirts?sz=60            |
      | Polo Shirts           | http://www.farah.co.uk/clothing/polo-shirts?sz=60         |
      | Knitwear              | http://www.farah.co.uk/clothing/knitwear?sz=60            |
      | Sweatshirts & Hoodies | http://www.farah.co.uk/clothing/sweatshirts-hoodies?sz=60 |
      | Denim & Trousers      | http://www.farah.co.uk/clothing/denim-trousers?sz=60      |
      | Outerwear             | http://www.farah.co.uk/clothing/outerwear?sz=60           |
      | Shorts                | http://www.farah.co.uk/clothing/shorts?sz=60              |

  @local
  Scenario: Scraping an example category page for product links
  Given I have the example page polo-shirts.html
   when I scrape that page for product links
   then I get the urls:
     | url                                                                                                   |
     | http://www.farah.co.uk/clothing/polo-shirts/the-jude-short-sleeve-polo-shirt-F4KS70E6GP.html          |
     | http://www.farah.co.uk/clothing/polo-shirts/the-randall-herringbone-stripe-polo-shirt-F4KS70B3GP.html |
     | http://www.farah.co.uk/clothing/polo-shirts/the-earlston-long-sleeve-polo-shirt-F4KF60P9GP.html       |
     | http://www.farah.co.uk/clothing/polo-shirts/the-merriweather-long-sleeve-polo-shirt-F4KF40G1GP.html   |
     | http://www.farah.co.uk/clothing/polo-shirts/the-blaney-short-sleeve-polo-shirt-F4KS5050GP.html        |
