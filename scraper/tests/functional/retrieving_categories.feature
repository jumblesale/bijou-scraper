Feature: Retrieving a list cateogires from an example page

  Scenario: Scraping an example page for categories
    Given I have the example page clothing.html
     when I scrape that page for categories
     then I get the categories:
      | title                 | url                                                        |
      | Shirts                | http://www.farah.co.uk/clothing/shirts                     |
      | T-shirts              | http://www.farah.co.uk/clothing/t-shirts                   |
      | Polo Shirts           | http://www.farah.co.uk/clothing/polo-shirts                |
      | Knitwear              | http://www.farah.co.uk/clothing/knitwear                   |
      | Sweatshirts & Hoodies | http://www.farah.co.uk/clothing/sweatshirts-hoodies        |
      | Denim & Trousers      | http://www.farah.co.uk/clothing/denim-trousers             |
      | Outerwear             | http://www.farah.co.uk/clothing/outerwear                  |
      | Shorts                | http://www.farah.co.uk/clothing/shorts                     |
