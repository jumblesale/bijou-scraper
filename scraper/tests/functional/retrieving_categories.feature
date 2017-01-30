Feature: Retrieving a list products from an example category page

  @local
  Scenario: Scraping an example page for categories
    Given I have the example page clothing.html
     when I scrape that page for categories
     then I get the categories:
      | title                 | url                                                 |
      | Shirts                | http://www.farah.co.uk/clothing/shirts              |
      | T-shirts              | http://www.farah.co.uk/clothing/t-shirts            |
      | Polo Shirts           | http://www.farah.co.uk/clothing/polo-shirts         |
      | Knitwear              | http://www.farah.co.uk/clothing/knitwear            |
      | Sweatshirts & Hoodies | http://www.farah.co.uk/clothing/sweatshirts-hoodies |
      | Denim & Trousers      | http://www.farah.co.uk/clothing/denim-trousers      |
      | Outerwear             | http://www.farah.co.uk/clothing/outerwear           |
      | Shorts                | http://www.farah.co.uk/clothing/shorts              |

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
